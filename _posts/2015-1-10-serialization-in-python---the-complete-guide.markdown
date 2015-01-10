---
layout: post
title: "Serialization in Python - The Complete Guide"
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

``cPickle`` is an optimized pickler module in python and
I think ``cPickle`` is one of the most commonly used pickler in data science,
but this guide shouldn't be bound to ``cPickle`` but I make no guarantees if
you are using the default ``pickle`` module or any other pickler.

We will also be using [numpy](http://www.numpy.org/) and [pandas](http://pandas.pydata.org/)
as well as look at how they deal with serialization.

If the serialization works properly the ``id`` function should actually
be the identity function. It basically just pickles the input object and loads
it again to see that everything worked properly and that it was recieved
correctly on the other side.

``unpickable`` will be used as an unpickable object for demonstration purposes.

Also I will use ``python-2.7``

Instances of Built-in Types
---------------------------
Instances of built-in

* [numeric](https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex)
* [sequence](https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange)
* [set](https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset)
* [text sequence]()
* [mapping]()

-types is supported.

For example

~~~python

~~~

Modules
-------

Classes
-------

Class Instances
---------------

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

Files
-----

memoryviews
-----------

contextmanagers
---------------


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

get/setstate


Serialization problems with big libraries
-----------------------------------------
pandas df.name
pandas.rollingmean


Pickle differences between python 2 and 3
-----------------------------------------

Summary
-------
Some objects are not serializable by the very nature of the object itself, for
example ...
But for other objects it doesn't make as much sense, for example ...
Serialization is many times overlooked even in big libraries like pandas.
