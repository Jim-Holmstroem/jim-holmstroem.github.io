---
layout: post
title:  "The Algebra of Data Types"
date:   2015-01-30 18:00:00
categories: programming type-theory
---

This post is based on the first half of the presentation given in [Algebra of Algebraic Data Types](https://www.youtube.com/watch?v=YScIPA8RbVE) (highly recommended).

Running
-------
The mathematics behind all this is not restricted in anyway to Haskell, any language with algebraic data types will do. The presentation uses Haskell and so will this post.

To be able to run the examples have these pragmas
{% highlight haskell %}
{-# LANGUAGE EmptyDataDecls
           , TypeOperators #-}
{% endhighlight %}

or run ghci with
{% highlight bash %}
ghci -XEmptyDataDecls -XTypeOperators
{% endhighlight %}

Introduction
------------
An algebra is simply put: _symbols_, _operations_ on the symbols and _laws_ for the operations.

In the case of the algebra of data types

1. Symbols: Types `((), Int, Bool, ...)`
2. Operations: Type constructors `(Maybe, Either, ...)`. Constructs a new type from other types.
3. Laws: `(((),x) = x, ...)`. Equivalences between different types.

The equivalence in the laws will be semantic equivalence since different types are always structurally different, but they can still mean the same thing (semantic).

Building up the Algebra
-----------------------
Now it's time to build up the algebra in the same way as we are used to in for example the algebra of integers (the easiest algebra to have an analog to).

Cardinality
===========
The below stated things actually preserves the structure under the function _cardinality_ of the type (i.e. the number of values of the type). This means that cardinality of the type `|.|` is an homomorphism.

`|.|` being an homomorphism means that this holds:
{% highlight haskell %}
|x :+ y| = |x| + |y|
{% endhighlight %}
where `+` is any binary integer operation and `:+` is the corresponding operation for types.
For example, this means that adding two types of size `M` and `N` will result in a type of size `M + N`.
Since the cardinality is an homomorphism we have several implications, one of them is that the unit for the operations must be mapped to the corresponding unit.
For example the cardinality of `Unit` is `|Unit| = 1` where both left and right hand side is the unit for multiplication for types and integers respectively.
But also that rules for operations on integers must hold for the corresponding operations on types with it's cardinality, more on this later.
This can be hard to wrap your head around, but just have it the back of your head when continuing and it will all fall into place.

Important Symbols
=================
The data type representing the important _1_ (one)
{% highlight haskell %}
data Unit = Unit -- 1
{% endhighlight %}
this type has one value represented by `Unit`. In haskell it is already defined and mostly represented as `()`.
For example, this is the type returned when there is nothing to return, this since functions most return something in able to be evaluated (Ex. `IO ()`).

The data type to represent the important _0_ (zero)
{% highlight haskell %}
data Void -- 0
{% endhighlight %}
this data type `Void` requires the extension _EmptyDataDecls_ and has no value.


Important Operations
====================
This requires the extension `TypeOperators`

Data type addition is defined as
{% highlight haskell %}
data a :+ b = AddL a | AddR b
data Either a b = Left a | Right b  -- already built-in
{% endhighlight %}
`:+` says that you either have an `a` or `b` and if it's an `a` you tagged it with `AddL` and if it's `b` you tagged it with `AddR`. The tagging is important for pattern matching to work.
This operation is the same as the built-in `Either` which is redefined just below the `:+` so that equivalence is clearer.

The size of `a :+ b` will be the sum of the sizes of `a` and `b`, so for example `Bool :+ Bool` will be of size `4` with the possible values: `AddL False, AddL True, AddR False, AddR True`.


{% highlight haskell %}
data a :* b = Mul a b
-- data (a,b) = (a,b)  -- pair, built-in, not actually executable but easy to think of
{% endhighlight %}
`:*` corresponds to the Cartesian product often denoted with $\times$

$$
\begin{equation}
    \label{eq:cartesian}
    A \times B = \left\{ (a, b): a \in A, b \in B \right\}
\end{equation}
$$

and in haskell this is called _pair_ and is denoted by `(,)`.

Examples of Laws
================
The stated laws will not run, it is just to showcase the laws.
`~=` will be used since the types are not structurally equal but only have a semantic equality (yes, a bit fuzzy), basically the left and right hand side has the same meaning.

{% highlight haskell %}
Either Void x ~= x  -- 0 + x = x
(Void,x) ~= Void  -- 0 * x = 0
((),x) ~= x  -- 1 * x = x
{% endhighlight %}

Symmetry laws
{% highlight haskell %}
Either a b ~= Either b a  -- x + y = y + x
(x,y) ~= (y,x)  -- x * y = y * x
{% endhighlight %}


Functions
=========
One of haskells defining properties is that functions are also types, so you can have function types.

A function is simply a mapping between a domain and codomain (range).
The number of possible functions between `a` and `b` is ${|b|}^{|a|}$ so it seems to be reasonable to use the codomain to the power of the domain as a representation for functions. Haskell uses `a -> b` to denote a function from `a` to `b`.

{% highlight haskell %}
data a :^ b = Fun a b
-- data a -> b = a -> b
{% endhighlight %}


Function laws
=============
Now it gets really interesting

{% highlight haskell %}
a -> () ~= ()  -- 1^a = 1
{% endhighlight %}
this is the function that only returns the unit (i.e. returns no information since you already know the return value).

{% highlight haskell %}
() -> a ~= a  -- a^1 = a
{% endhighlight %}
since this doesn't have an argument it only thing it can be is a constant function. This law states that constant function and a constant has the same meaning.

{% highlight haskell %}
a -> (b,c) ~= (a -> b, a -> c)  -- (b*c)^a = b^a*c^a
{% endhighlight %}
which states that a function returning a pair might as well be a pair of functions returning each of the elements of the pair. *mind blown*


{% highlight haskell %}
(a,b) -> c ~= a -> b -> c  -- c^(b*a) = (c^b)^a
{% endhighlight %}
which states that a function mapping a pair to a value is the same as a function with two arguments (or with currying in mind, a function taking a value from `a` and returning a function of type `b -> c` which takes an argument of type `b` and returns a value of type `c`)
And again it's just a matter on how you seen on things, they still have the same semantic meaning, one has two arguments explicitly and the for the other one the arguments are packed into a pair (structural difference).

Recursive Data Types
--------------------
Recursive definition of a list
{% highlight haskell %}
data List x = () |  (x, (List x))  -- L(x) = 1 + x * L(x)
data List' x = Nil | Cons x (List' x)  -- as usually defined
{% endhighlight %}

If we try to solve it for `List x` denoted $L$ (the definition above is shorted down to $L = 1 + xL$ for brevity)

$$
\begin{equation}
    \begin{aligned}
        L & = 1 + xL \\
        L & = 1 + x(1 + xL) \\
        L & = 1 + x + x^2(1+xL) \\
          & ...\\
        L & = 1 + x + x^2 + x^3 + x^4 + ...
    \end{aligned}
\end{equation}
$$

The result when read out is that $L$ is either empty (`1`) or (`+`) is one element from `x` or (`+`) has 2 elements from `x` or ... and so on and so on.
Which is basically what a list is `() | (x,()) | (x,(x,())) | ...`


A more complicated example is a tree, which can be defined by
{% highlight haskell %}
data Tree x = () | (Tree x, x, Tree x)  -- T(x) = 1 + T(x) x T(x) = 1 + x T(x)^2
data Tree' x = Tip | Node (Tree' x) x (Tree' x)  -- as usually defined
{% endhighlight %}

Doing the same type of manipulation as before with trees instead of lists

$$
\begin{equation}
    \begin{aligned}
        T &= 1 + xT^2 \\
        xT^2 - T + 1 &= 0 \\
        T &= \frac{1 - \sqrt{1-4x}}{2x} \\
        T &= 1 + x + 2x^2 + 5x^3 + 14x^4 + ...
    \end{aligned}
\end{equation}
$$

Keep in mind that we are still working with types and type algebra so the second order solution (3rd line) doesn't make much sense, however if you look up the power-series expansion (4th line) for it it makes sense.

It states that a tree is either:

0. Empty (`1`)
1. A single element of type `x`
2. 2 different trees of size 2
3. 5 different trees of size 3
4. 14 different trees of size 4
5. ... and so on and so on

Which amazingly corresponds to the number of different trees for the given size. *mind blown*
Note that the product with integers in the power-series expansion is the same as saying addition `N` times. Ex. $2x^2 = x^2 + x^2$, i.e. these to elements or these two elements.

To be less abstract we can take a look at Tree Bool, T(2) in the equations above you can count how many Trees there is with Bool as inner type and are of size say 3 which is $5\cdot 2^3=40$.


Still Hungry for Types?
-----------------------
Go and watch the second half of the presentation on which this post is based [Algebra of Algebraic Data Types](https://www.youtube.com/watch?v=YScIPA8RbVE).
