---
layout: post
title:  "Double Expectation"
date:   2014-10-14 11:09:00
categories: probability
---

Theorem - Double Expectation
-------
$$
    E[Y] = E[E[Y|X]]
$$

Proof
-----

One can see the conditional expectation $E[Y|X]$ as a Borel function $H_Y(X)$,
where $Y$ and how to condition it (and expect, but that is always the same) is encoded into it.
$H_Y$ takes a random variable (r.v.) $X$ (prior) and returns the expectation of $Y$
conditioned on $X$ which is also a random variable.

The signature for $H_Y$ can most easily be seen by considering:
A r.v. by definition is $X : \Omega_X \rightarrow C_X$
where $C_X$ stands for the codomain of $X$.

So for the Borel function we should have the signature

$$
    \begin{equation}
        H_Y: (\Omega_X \rightarrow C_X) \rightarrow (\Omega_X \rightarrow C_{E[Y]} = C_Y)
    \end{equation}
$$

Which holds since

$$
    \begin{equation}
        H_Y(X)(x) \in C_Y\quad \forall x\in\Omega_X
    \end{equation}
$$

is both valid and always true.

To relate to functional programming: it's an "higher order"-function.

$$
    \begin{align}
        E[E[Y|X]]
            &= E[H_Y(X)]\bigg|_{H_Y(X) = E[Y|X]} \nonumber \\
            &= \sum\limits_x H_Y(x) p_X(x) \bigg|_{H_Y(X) = E[Y|X]} \nonumber \\
            &= \sum\limits_x E[Y|X=x] p_X(x) \nonumber \\
            &= \sum\limits_x \left(
                \sum\limits_y y p_{Y|X=x}(y)
            \right) p_X(x) \nonumber \\
            &= \sum\limits_x \left(
                \sum\limits_y y p_{Y|X=x}(y) p_X(x)
            \right) \nonumber \\
            &= \sum\limits_x \left(
                \sum\limits_y y p_{X, Y}(x, y)
            \right) \nonumber \\
            &= \sum\limits_y \left(
                \sum\limits_x y p_{X, Y}(x, y)
            \right) \nonumber \\
            &= \sum\limits_y y \left(
                \sum\limits_x p_{X, Y}(x, y)
            \right) \nonumber \\
            &= \sum\limits_y y
                p_Y(y)
            \nonumber \\
            &= E[Y] \nonumber \\
            & \Box
    \end{align}
$$

