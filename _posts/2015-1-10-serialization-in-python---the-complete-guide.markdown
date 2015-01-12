---
layout: post
title: "Serialization in Python - The Complete Guide [WIP]"
date: 2015-1-10 17:10
categories: python
---

Serialization (pickling in pytho) and deserialization of objects is an
essential part for distributed and parallel computing.

When working with libraries such as [joblib](https://github.com/joblib/joblib)
or the builtin
[multiprocessing](https://docs.python.org/2/library/multiprocessing.html)
one of the most common problems issues is that the object you are trying to
have as input is not serializable.

This guide is intended to be a walk-through of pythons world of serialization.

Initial code
------------

~~~python
from cPickle import dumps, loads
import numpy as np
import pandas as pd

id = lambda x: loads(dumps(x))
unpickable = lambda x: x
~~~

``cPickle`` is an optimized and commonly used pickle module in python
but this guide shouldn't be bound to ``cPickle`` but it makes no guarantees if
you are using the default ``pickle`` module or any other pickler.

We will also be using [numpy](http://www.numpy.org/) and [pandas](http://pandas.pydata.org/)
as well as look at how they deal with serialization.

If the serialization works properly the ``id`` function should actually
be the identity function. It basically just pickles the input object and loads
it again to see that everything worked properly and that it was recieved
correctly on the other side.

``unpickable`` will be used as an unpickable object for demonstration purposes.

This guide will use ``python-2.7``.

Note that the expression to be tested through loaddump will mostly just be
stated and it is up to the read to run it through ``loaddump``. This is due to
brevity.

Instances of Built-in Types
---------------------------
Instances of built-in

* [numeric](https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex)
* [sequence](https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange)
* [set](https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset)
* [mapping](https://docs.python.org/2/library/stdtypes.html#mapping-types-dict)
 is supported.

~~~python
1
1L
1.0
complex(1, 1)
'test'
u'test'
[1, 2, 3]
(1, 2, 3)
bytearray(1024)
xrange(16)
{1}
frozenset({1})
{1: 1}
~~~

Except for ``buffer`` and ``memoryview`` objects

~~~python
buffer(bytearray(1024), 0, 16)
loaddump(memoryview(bytearray(1024)))
~~~

TODO why is this reasonable?

Note that all instances of sequence type will recursivly serialize all the elements
and thus all the elements must be pickable.

Iterators
---------

Modules
-------
TODO these are by full name (as a few other things, for example functions but we will come back to those later)

Classes
-------


Class Instances
---------------
All attributes needs to be pickable.

see get/setstate later to see how to override this behaviour or just to see how
it works under the hood. TODO proper name of get/setstate

TODO reference to how it does default.

Functions
---------

inner functions

Methods
-------
~~~python
class A(object):
    def f(self, x):
        return x
~~~

Bounded methods

~~~python
A().f
~~~

Unbounded methods:

~~~python
A.f
~~~

Higher-order functions
----------------------
Functions that operates on other functions, for example ``functools.partial`` or
``functools.wraps`` and has a functions as result.
These are in many contexts in python called _decorators_.

~~~python
def twice(f):
    def f_twice(x):
        return f(f(x))

    return f_twice
~~~

and it is used liked this, to hash 1337 twice:

~~~python
twice(hash)(1337)
~~~

However ``twice(hash)`` is not pickable even if ``hash`` is, this is because
``twice(hash)`` is an ``f_twice`` with the ``f`` in the expression
``return f(f(x))`` fixed (it is in the functions so called _closure_) to ``hash``.

This is due to that ``f_twice`` is out of scope, i.e. there
is no name for it outside the scope of ``twice``.

How to fix it:

~~~python
class twice(object):
    def __init__(self, f):
        self.f = f
    def __call__(self, x):
        return self.f(self.f(x))
~~~

It works as long as ``f`` is serializable, but the function ``twice`` looks
much better and has less boilerplate then the class ``twice``.

One can do something similar by returning classes (not as common but occurs from
time to time):

~~~python
def f(t):
    class A(object):
        def f(self):
            return t
    return A
~~~

It is basically the same problem for ``f(t)`` and the same solution.
This is very much related to ``Metaclasses``.

Metaclasses
-----------
Works the same way as for classes, since it is classes for classes.
TODO try it!!

Files
-----

Miscellaneous
-------------
type
None
Ellipsis
memoryviews
contextmanagers


Dealing with Injection
----------------------
A really useful way of writing testable and general code is by injecting all
the "externals" when initializing an object.
This has the side-effect that everythin injected must also be serializable.

~~~python
class twice(object):
    def __init__(self, f):
        self.f = f
    def __call__(self, x):
        return self.f(self.f(x))

class squaretwice(object):
   def __call__(self, x):
       return np.square(np.square(x))
~~~

``twice(square)`` will be serializable only if ``square`` is serializable
since all attributes will be serialized (default behaviour of picklers).


TODO what gets loaded from the pickle dump and what actually gets loaded from the code itself (the module)


Default arguments
-----------------

~~~python
class A(object):
    def __init__(self, f=unpickable):
        pass

def f(g=unpickable):
    return g
~~~

Now why is there no problem pickling the class ``A``, an instance of ``A`` nor
``f``.

The default argument is located in

~~~python
show above
~~~

It will be created when the module is loaded and thus it does not need to among
the information pickled.


Changing context
----------------
~~~python
def f():
    return 1337

f_dump = dumps(f)
del f  # remove it from our context
f = loads(f_dump)
~~~

TODO! dig deeper into this


Override the pickling
---------------------

* ``__getstate__`` returns a pickable object representing the state
* ``__setstate__`` receives the above object and reconstructs the state from it

TODO example which isn't pickable but can be made so via get/set


Proposal to pickle simple lambdas
---------------------------------

~~~python
from collections import namedtuple
from types import LambdaType, CodeType

class Code(object):
    State = namedtuple(
        'State',
        (
            'argcount',
            'nlocals',
            'stacksize',
            'flags',
            'codestring',
            'constants',
            'names',
            'varnames',
            'filename',
            'name',
            'firstlineno',
            'lnotab',
        )
    )
    def __init__(self, code):
        self.code = code

    def __getatttr__(self, name):
        return getattr(self.code, name)

    def __getstate__(self):
        state = Code.State(
            argcount=self.co_argcount,
            nlocals=self.co_nlocals,
            stacksize=self.co_stacksize,
            flags=self.co_flags,
            codestring=self.co_code,
            constants=self.co_consts,
            names=self.co_names,
            varnames=self.varnames,
            filename=self.co_filename,
            name=self.co_name,
            firstlineno=self.co_firstlineno,
            lnotab=self.co_lnotab,
        )

        return state

    def __setstate__(self, state):
        self.code = types.CodeType(
            argcount=state.argcount,
            nlocals=state.nlocals,
            stacksize=state.stacksize,
            flags=state.flags,
            codestring=state.codestring,
            constants=state.constants,
            names=state.names,
            varnames=state.varnames,
            filename=state.filename,
            name=state.name,
            firstlineno=state.firstlineno,
            lnotab=state.lnotab,
            freevars=(),  # TODO are these needed for np/pd to work?
            cellvars=(),
        )

class Lambda(object):
    State = namedtuple(
        'State',
        (
            'code',
            'name',
            'argdefs',
            'context',
        )
    )

    def __init__(self, lambda_, context={}):
        self.lambda_ = lambda_
        self.context = context

    def __getatttr__(self, name):
        return getattr(self.lambda_, name)

    def __getstate__(self):
        state = Lambda.State(
            code=Code(self.func_code),
            name=self.func_name,
            argdefs=self.func_defaults,
            context=self.context,
        )

        return state

    def __setstate__(self, state):
        self._lambda = types.LambdaType(
            code=state.code,
            globals=state.context,
            name=state.name,
            argdefs=state.argdefs,
            closure=None,  # TODO is this needed for np/pd to work?
        )

Lambda(lambda x: x)
~~~

TODO test the above code!!

The above code is two fully transparent wrappers for ``code`` and ``lambda``-objects which
are (in simpler cases) pickleable despite ``code`` and ``lambda``-objects in themself
not being so by design choice.
The boilerplate code is mainly because some of the initialization arguments
are not named as their corresponding attributes
(``constants/consts`` ``argdef/defaults`` ``codestring/code``)


TODO "does not support variables defined outside the block"
how does it support np.mean(x-x.mean()) (np global in this)
Lambda.__init__(self, lambda_, context={'np': np, 'pd', pd}):  # will it be necessary to have commonly used modules like this (in other words are they considered "global", verify

Note that if we would include global then everything in ``globals()``
(the global scope) must be pickable which seldom is the case.

Ensuring picklability
---------------------

Always have something like this in your tests

~~~python
from nose.tools import assert_equal
def test_loaddump(o):
assert_equal(
    loaddump(o),
    o
)
~~~

It does not catch everything but it is better than nothing.

Remark: make  sure that the equals operator is always fully implemented and
that two objects with different state (except for ``id()`` and such ofc) cannot
be equal.


Serialization problems between different machines
-------------------------------------------------
different versions of the same library give som concrete examples.

Serialization problems with big libraries
-----------------------------------------
pandas df.name
pandas.rollingmean


Serialization weirdness from builtin
------------------------------------

~~~python
loaddump('{}:{}'.format)
~~~

~~~python
TypeError: expected string or Unicode object, NoneType found
~~~

Pickle differences between python 2 and 3
-----------------------------------------


Summary
-------
Some objects are not serializable by the very nature of the object itself, for
example ...
But for other objects it doesn't make as much sense, for example ...
Serialization is many times overlooked even in big libraries like pandas.
