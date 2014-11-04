---
layout: post
title: "Python Type Definition Proposal"
date: 2014-11-03 10:51:26
categories: python
---

A proposal for Python type definition inspired by Haskells algebraic data types.
By using the representative power of algebra to define types in Python one attains
a low clutter view of the composed types for variables/arguments and return types.

It's not claiming to be able to represent any composed type (yet), but that is
not the main goal of it.

Usage
-----
Inline to aid the coming-back-next-month scenario

~~~ python
books = map(get_address_book, people)  # :: [{name :: str: number :: str}]
alternative_books = map(get_address_book, people)  # :: [{str: str}]
~~~

A deeper understanding of the datatype for the arguments and returned value from
the documentation.

~~~ python
def foo(books):
    """Documentation about the function/method as usual.

    Arguments
    ---------
    books :: [{name :: str: number :: str}]
        Documentation about the variable as usual.

    Returns
    -------
    n_contacts :: [int]
        Documentation about the variable as usual.
    """

    return map(len, books)
~~~

This compared to, if any type definition at all, for example the
``numpy`` standard way of doing it.

~~~ python
def foo(books):
    """Documentation about the function/method as usual.

    Arguments
    ---------
    books : list
        Documentation about the variable as usual.

    Returns
    -------
    n_contacts : list
        Documentation about the variable as usual.
    """

    return map(len, books)
~~~

Instead of thinking for your own, or writing it down in plain text in the
documentation ``n_books is a list of integers`` you have a compact and stringent
way to write composed types that minimizes the mental clutter.

Operators
---------

Is of type
==========
``N :: T``: The name N _is of type_ T

Or
==
``T1 | T2``: It is either of type T1 _or_ T2, which tells that the code must
be guarded for both types.
Associative operation which makes ``T1 | T2 | T3 | ...`` unambiguous.
An useful (and unfortunately common) use is ``T|None``, i.e. nullable.

Function
========
``T -> R``: A _function_ which takes one argument of type ``T`` and
returns a value of type ``R``.
For other number of arguments 0 to n: ``-> R`` (or ``*() -> R``), ``T -> R`` (or ``*(T1, ) -> R``), ``*(T1, T2) -> R``,
``*(T1, T2, ..., Tn) -> R``.
The syntax for this is still under consideration, see notes on "Work needed to be done".

Tuple
=====
``(T1, T2)``: A _tuple_ with the inner types ``T1`` and ``T2``. Extends to
``()``, ``(T1, )``, ``(T1, T2)``, ``(T1, T2, T3)``, ``(T1, ..., Tn)``.

Sequence
========
``[E]``: A _sequence_ with elements of type ``E``.
See note about sequences under "Work needed to be done".

Set
===
``{E}``: A _set_ with elements of type ``E``.

Dictionary
==========
``{K: V}``: A _dictionary_ with keys of type ``K`` and values of type ``V``.

Grouping
========
``(T)``: Grouping works as in mathematics, the expression inside the grouping
is evaluated first. Used for non-associative operations like ``->``.

Example: ``decorator :: (T -> int) -> (T -> float)``

Atomic
======
``bool``: ``bool``, ``types.BooleanType``.

``int``: ``int``, ``types.IntType``.

``float``: ``float``, ``types.FloatType``.

``str``: ``basestring``.

``None``:  ``types.NoneType``.

Polymorphic
-----------
``enumerate :: [T] -> [(count :: int, T)]`` Where ``T`` and the other ``T`` is of any
and the same type. Could also be used for non-functions ``zip(a, a) :: [(T, T)]``

Pragmatic usage
---------------
Stop with names instead of types all the way down
``service_hooks :: {service: [hook]}``, remember readability is key.

Extensions to numpy datatypes
-----------------------------
Add the dimensions of the ndarray, in Haskell the ``ndarray``
would be parameterized type.
Either you have the parameters to be the size in integers
(represented by a letter which in turn represents the dimension,
as often done in mathematics)
or the name of the dimension directly.

``timeseries :: ndarray(M, T)``

``timeseries :: ndarray(feature, time)``

``runs :: ndarray(run, feature, time)``

It's much easier to verify by eye that you are by for example
``np.sum(runs, axis=0)``
actually summing all the runs, or by indexing
``first_feature = runs[:, 0, :]``
actually getting the first feature for all runs and times.

One could also add the ``dtype`` when it's a non-float64.
``timeseries_count :: ndarray(M, T, dtype=int)``

~~~ python
def features(data):
    """description

    Arguments
    ---------
    data :: ndarray(time)
        description

    Returns
    -------
    features :: ndarray(feature, time)
        description

    """

    return ...

~~~

~~~ python
def nan_feature_count(data):
    """description

    Arguments
    ---------
    data :: ndarray(feature, time)
        description

    Returns
    -------
    features :: ndarray(time, dtype=int)
        description

    """

    return ...

~~~

Work needed to be done
----------------------

Be able to define properties
``bisect :: *(Sorted [T], T) -> (index :: int)``

Handle the consumption difference between iterator and list (or if it doesn't matter)

Be able to breakout common or long parts out of a definition

~~~ python
dict_utils.reduce :: *([D], reducer :: [V] -> V) -> D
    where D = {K: V}
~~~

``ordereddict``, ``frozenset`` and other standard data types with properties.
``Ordered {K: V}``, ``Frozen {E}``.

Default arguments ``randint :: (seed :: int<0>) -> int``, default
arguments with "Not set" i.e. ``None``.

``*args``, ``**kwargs``

For example ``isinstance`` and ``type`` where you are supposed to use a tuple
with variable length. ``(T, ...)``

A mark to differentiate pure (no side-effects) with unpure (side-effects).

Deal with ``types.EllipsisType``, ``types.ClassType``, ``types.TypeType``

if NaN is a possible value for numpy array
``ndarray(feature|NaN, time)``.

Type definition examples from the standard library
--------------------------------------------------

``enumerate :: [T] -> [(int, T)]``

``int :: int -> int``

``sorted :: [T] -> [T]``

``sort :: [T] -> None``

``zip :: *([T1], ..., [Tn]) -> [(T1, ..., Tn)]``

``partial :: (T1 ... -> R) -> T1 -> (... -> R)``

``all :: [T] -> bool``

``chr :: int -> str``

``cmp :: *(T, T) -> bool``

~~~ python
def groupby(iterable, keyfunc=None):
    """groupby description is put here.

    Arguments
    ---------
    iterable :: [T]
        iterable description is put here.

    keyfunc :: T -> K
        keyfunc description is put here.

    Returns
    -------
    grouping :: [(K, [T])]
        grouping description is put here.

    """

~~~

``itertools.takewhile :: *((T -> bool), [T]) -> [T]``

``itertools.combinations :: *([T], repeat :: int) -> [(T, ...)]``

``reduce :: *(*(T, T) -> T, [T]) -> T``
