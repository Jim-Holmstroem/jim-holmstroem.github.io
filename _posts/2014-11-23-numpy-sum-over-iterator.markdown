---
layout: post
title: "np.sum(imap(identity, range(10))) weirdness"
date: 2014-11-23 10:37:16
categories: numpy
---

I stumbled on something rather unexpected in numpy the other day when I, lazy as
I am, wrote an iterator using ``itertools`` and the code somewhere down the line
tried to ``np.sum`` it.


Dependencies
------------
I'm using ``numpy-1.9.1`` and ``python2.7``, I haven't looked this issue with other versions.


Small Example
-------------

With ``identity = lambda x: x``, ``N_10 = range(10)`` we get

|   | ``sum(.)``  | ``np.sum(.)``  |
|---|:-:|:-:|
| ``map(identity, N_10)`` | ``45``  | ``45`` |
| ``imap(identity, N_10)``| ``45``  | ``<itertools.imap at 0x2c28610>`` |


Down the rabbit hole
--------------------

It seems that it's not only the ``np.sum`` that posses this unintuitive behaviour
with iterators, but also ``np.min``, ``np.max`` among others.

I wrote some code to try all ``numpy`` functions with an iterator and see what
happens.

~~~ python
from __future__ import print_function, division
import numpy as np
from itertools import *
from functools import *
import inspect

it = lambda: imap(lambda x: x, range(10))
def all_functions(module):
    return filter(
        inspect.isfunction,
        map(
            partial(getattr, module),
            sorted(dir(module))
        )
    )

fs = all_functions(np)

def tryprint(a):
    try:
        print(a)
    except:
        pass

def tryapply(f, g=it):
    try:
        return f, f(g())
    except:
        return f, "FAILED"

not_failed = lambda (f, f_return): f_return != "FAILED"

map(
    tryprint,  # NOTE something returned didn't have a proper __repr__ (otherwise just print)
    filter(
        not_failed,
        map(
            tryapply,
            fs
        )
    )
)

~~~

The relevant output:
[gist link](https://gist.github.com/Jim-Holmstroem/00758f5ebe0d2bd7537e)

Grouping by "type" and filtering out the irrelevant functions

Shape
-----
~~~ python
(<function alen at 0x7fda5dd459b0>, 1)
(<function ndim at 0x7fda5dd45b18>, 0)
(<function shape at 0x7fda5dd45320>, ())
(<function size at 0x7fda5dd45c08>, 1)

~~~

The problem probably originates from the shape of the iterator being interpreted
as ``np.shape(imap(.)) = ()`` i.e. the degenerate case of ``np.ndarray``. This
similarly to ``np.array(0)``. Whould have been more expected if it was interpreted
as a python list.

Passthrough
-----------
~~~ python
(<function all at 0x7fda5dd456e0>, <itertools.imap object at 0x7fda5b002210>)
(<function alltrue at 0x7fda5dd455f0>, <itertools.imap object at 0x7fda5b002250>)
(<function amax at 0x7fda5dd458c0>, <itertools.imap object at 0x7fda5b002310>)
(<function amin at 0x7fda5dd45938>, <itertools.imap object at 0x7fda5b002390>)
(<function any at 0x7fda5dd45668>, <itertools.imap object at 0x7fda5b0023d0>)
(<function amax at 0x7fda5dd458c0>, <itertools.imap object at 0x2f68c50>)
(<function maximum_sctype at 0x7fda60d4a230>, <itertools.imap object at 0x2f68950>)
(<function nansum at 0x7fda5d9bacf8>, <itertools.imap object at 0x2f68f10>)
(<function prod at 0x7fda5dd45a28>, <itertools.imap object at 0x2f7b110>)
(<function product at 0x7fda5dd45500>, <itertools.imap object at 0x2f7b410>)
(<function sometrue at 0x7fda5dd45578>, <itertools.imap object at 0x2d2f410>)
(<function sum at 0x7fda5dd45488>, <itertools.imap object at 0x3026d90>)

~~~

By the looks of it the degenerate case isn't handled properly.

The ``all`` and ``any``-family is working better than in ``numpy-1.8`` and handles integers properly (but not iterators, even if we would interpret it as an object)
[stackoverflow question](http://stackoverflow.com/questions/16426547/numpy-all-with-integer-arguments-returns-an-integer)

``reduce(op, .)``-family (which is all passthroughs except sctype) propably has a special case for the degenerate case (being identity).
They should act the same in the degenerate case going from ``((id(op) op a_0) op a_1)...`` to ``id(op) op a_0``.
Where ``id(op)`` is the identity element of the group ``<R, op>``. If this would have been the case the
application of an iterator would fail (which is better).

``maximum_sctype`` does not return a type.


Number
------
~~~ python
(<function argmax at 0x7fda60d76e60>, 0)
(<function argmin at 0x7fda60d76ed8>, 0)
(<function argsort at 0x7fda60d76de8>, 0)
(<function nanargmax at 0x7fda5d9bac80>, 0)
(<function nanargmin at 0x7fda5d9bac08>, 0)
(<function rank at 0x7fda5dd45b90>, 0)

~~~

``arg*``-family propably has a special case for the degenerate case.
``arg*`` doesn't make much sense in the degenerate case, compare ``np.argmax(4, axis=0)`` with ``np.argmax([4], axis=0)``.
The degenerate's index-space is zero-dimensional so it should return ``()`` additionally it doesn't even have an axis (not even ``axis=0``).

No comment on ``rank``.

Boolean
-------
~~~ python
(<function iscomplex at 0x7fda5d9919b0>, False)
(<function iscomplexobj at 0x7fda5d991aa0>, False)
(<function isreal at 0x7fda5d991a28>, True)
(<function isrealobj at 0x7fda5d991b18>, True)
(<function isscalar at 0x7fda5dd47ed8>, False)
(<function issctype at 0x7fda60d4a320>, False)
(<function iterable at 0x7fda5d9a52a8>, 1)

~~~

What constitutes something to be ``real`` or ``realobj``? If ``imap`` is interpreted as an object it's not real (otherwise it is (in this case)).

Off-topic: ``iterable`` should be ``isiterable`` and have a boolean codomain.

Cumulation
----------
~~~ python
(<function cumprod at 0x7fda5dd45aa0>, array([<itertools.imap object at 0x7fda5b002c50>], dtype=object))
(<function cumproduct at 0x7fda5dd457d0>, array([<itertools.imap object at 0x7fda5afae050>], dtype=object))
(<function cumsum at 0x7fda5dd45758>, array([<itertools.imap object at 0x7fda5afae110>], dtype=object))
(<function gradient at 0x7fda5d9b2398>, [])

~~~

``gradient`` is interpreting the ``imap`` as an object.
The ``cumop``-family has the same issues as ``reduce(op, .)``.

Complex
-------
~~~ python
(<function imag at 0x7fda5d991938>, array(0, dtype=object))
(<function real at 0x7fda5d9918c0>, array(<itertools.imap object at 0x2d2f0d0>, dtype=object))
(<function real_if_close at 0x7fda5d991c80>, array(<itertools.imap object at 0x2d2f150>, dtype=object))

~~~

This behaviour is really unintuitive and probably is caused by ``isreal``'s unintuitive behaviour.


Array with ``dtype=imap``
-------------------------
~~~ python
(<function asanyarray at 0x7fda60d6e5f0>, array(<itertools.imap object at 0x7fda5b002450>, dtype=object))
(<function asarray at 0x7fda60d6e578>, array(<itertools.imap object at 0x7fda5b002590>, dtype=object))
(<function asarray_chkfinite at 0x7fda5d9b21b8>, array(<itertools.imap object at 0x7fda5b002610>, dtype=object))
(<function ascontiguousarray at 0x7fda60d6e668>, array([<itertools.imap object at 0x7fda5b002690>], dtype=object))
(<function asfortranarray at 0x7fda60d6e6e0>, array([<itertools.imap object at 0x7fda5b0026d0>], dtype=object))
(<function asmatrix at 0x7fda5d9b38c0>, matrix([[<itertools.imap object at 0x7fda5b002790>]], dtype=object))
(<function atleast_1d at 0x7fda5dd645f0>, array([<itertools.imap object at 0x7fda5b002890>], dtype=object))
(<function atleast_2d at 0x7fda5dd64aa0>, array([[<itertools.imap object at 0x7fda5b002950>]], dtype=object))
(<function atleast_3d at 0x7fda5dd64b18>, array([[[<itertools.imap object at 0x7fda5b0029d0>]]], dtype=object))
(<function broadcast_arrays at 0x7fda5d9b7aa0>, [array(<itertools.imap object at 0x7fda5b002a90>, dtype=object)])
(<function copy at 0x7fda5d9b2320>, array(<itertools.imap object at 0x7fda5b002b50>, dtype=object))
(<function diagflat at 0x7fda5d997aa0>, array([[<itertools.imap object at 0x7fda5afae290>]], dtype=object))
(<function asmatrix at 0x7fda5d9b38c0>, matrix([[<itertools.imap object at 0x7fda5afae410>]], dtype=object))
(<function msort at 0x7fda5d9b3140>, array(<itertools.imap object at 0x2f68e90>, dtype=object))
(<function ravel at 0x7fda5dd45230>, array([<itertools.imap object at 0x2f7b610>], dtype=object))
(<function require at 0x7fda60d6e758>, array(<itertools.imap object at 0x2d2f190>, dtype=object))
(<function sort at 0x7fda60d76d70>, array(<itertools.imap object at 0x33a7890>, dtype=object))
(<function squeeze at 0x7fda5dd450c8>, array(<itertools.imap object at 0x30cbd90>, dtype=object))
(<function transpose at 0x7fda60d76c08>, array(<itertools.imap object at 0x3026d10>, dtype=object))
(<function unique at 0x7fda5d753c08>, array([<itertools.imap object at 0x3026bd0>], dtype=object))

~~~

All of these functions is handling ``imap`` as an object and therefor operating as the degenerate case.
For some of which the degenerate case is unintuitive in itself.


Array with ``dtype=number``
---------------------------
~~~ python
(<function argwhere at 0x7fda60d6e848>, array([[0]]))
(<function column_stack at 0x7fda5d9bd5f0>, array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]))
(<function dstack at 0x7fda5d9bd668>, array([[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]]))
(<function hstack at 0x7fda5dd64c08>, array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
(<function indices at 0x7fda5dd47de8>, array([], shape=(10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9), dtype=int64))
(<function nonzero at 0x7fda5dd452a8>, (array([0]),))
(<function ones_like at 0x7fda60d6e398>, array(1, dtype=object))
(<function vstack at 0x7fda5dd64b90>, array([[0],
       [1],
       [2],
       [3],
       [4],
       [5],
       [6],
       [7],
       [8],
       [9]]))
(<function vstack at 0x7fda5dd64b90>, array([[0],
       [1],
       [2],
       [3],
       [4],
       [5],
       [6],
       [7],
       [8],
       [9]]))
(<function zeros_like at 0x7fda60d6e2a8>, array(0, dtype=object))

~~~

``argwhere`` and ``nonzero`` is handling it as the degenerate case.

``*_like``-family is handling it as the degenerate case.

The ``stack``-family works as one should expect (if ``imap`` is interpreted as an list).

``indices`` is iterating through the iterator interpreting it as a list, however is this
case compared to (all?) other the argument isn't data but instead a list of index dimensions.

Summary
------

``np.array(it())`` returns ``array(<itertools.imap object at 0x2f45490>, dtype=object)``

Contract of return type in documentation not guaranteed.

Note
----
Realized when I was done that some functions wheren't registering as functions by ``inspection.isfunction``,
one exapmle being ``np.minimum``. I should (if I have the time to) redo this analysis.
