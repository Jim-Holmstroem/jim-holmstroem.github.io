---
layout: post
title: "Numpy ndarray from function"
date: 2014-11-06 22:42:35
categories: python
---

~~~ python
X = Y = np.arange(4)
A = np.frompyfunc(
    lambda x, y: f(x, y), 2, 1
).outer(
    X,
    Y,
).astype(np.float64)  # a_xy = f(x, y) \forall x \in X, y \in Y
~~~

which results in $A_{xy} = f(x, y) \quad\forall x\in X, y\in Y$

really nice to have when evaluating
$E\left\[X(s)\cdot X(t)\right\] = e^{-|t-s|}$ between a few points

~~~ python
X = np.arange(64)  # all X points
autocorr = np.frompyfunc(lambda s, t: np.exp(-np.abs(t, s))).outer

Sigma_XX = autocorr(X, X).astype(np.float64)
~~~
