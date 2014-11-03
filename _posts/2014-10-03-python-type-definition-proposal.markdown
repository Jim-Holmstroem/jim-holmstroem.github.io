---
layout: post
title: "Python Type Definition Proposal"
date: 2014-11-03 10:51:26
categories: python
---

[WIP]

A proposal for Python type definition inspired by Haskell.

Usage
-----

Inline to aid the comming-back-next-month scenario

~~~ python
books = map(get_address_book, people)  # :: [{name :: str: number :: str}]
alternative_books = map(get_address_book, people)  # :: [{str: str}]
~~~

A deeper understanding of the datatype for the arguments and returned value

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
documentation ``books is a list of integers`` you have a compact and stringent
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
``T1 -> T2``: A _function_ which takes an element of type ``T1`` and returns ``T2``.

Tuple
=====
``(T1, T2)``: A _tuple_ with the inner types ``T1`` and ``T2``. Extends to
``()``, ``(T1, )``, ``(T1, T2)``, ``(T1, T2, T3)``, ``(T1, ..., Tn)``.

Sequence
========
``[T]``: A _sequence_ with elements of type ``T``.
See note about sequences under "Work needed to be done".

Set
===
``{T}``: A _set_ with elements of type ``T``.

Dictionary
==========
``{T1: T2}``: A _dictionary_ with keys of type ``T1`` and values of type ``T2``.

Grouping
========
``(T)``: Grouping works as in mathematics, the expression inside the grouping
is evaluated first. Used for non-associative operations like ``->``.

Example; decorator :: (T -> int) -> (T -> float)

Atomic
======
``bool``: ``bool``, ``types.BooleanType``.

``int``: ``int``, ``types.IntType``.

``str``: ``basestring``

``None``:  ``types.NoneType``

Polymorphic
-----------
``enumerate :: [T] -> [(count :: int, T)]`` Where T and the other T is of any
but the same type.

Pragmatic usage
---------------
Stop with names instead of types all the way down
``service_hooks :: {service: [hook]}``, remember readability is key.


Extensions to numpy/pandas datatypes
------------------------------------


Work needed to be done
----------------------
iterator/sequence/list (consumption)
[]'

multi line definitions, and haskell

~~~ python
f :: T -> [T]
    where T = [int]
~~~

ordereddict frozenset and other atomic like stuff?

str vs. basestring vs. u''


Type examples from the standard library
---------------------------------------

int
enumerate
partial
