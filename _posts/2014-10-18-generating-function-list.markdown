---
layout: post
title:  "List of generating functions"
date:   2014-10-18 15:16:00
categories: probability
---

Couldn't find any list of generating functions for distributions on the Internet
so I started compiling my own.
(They will be filled in as they appear in the wild)

Definition
----------

We use the simpler notation for the generating function of $X\in F$

$$
\begin{equation}
    g_{X}(t) \overset{\text{def}}{=} g_{F}(t)
\end{equation}
$$

And by definition the moment generating function is

$$
\begin{equation}
    g_{X}(t) \overset{def}{=} E[t^X] =
        \sum t^k p_X(k)
\end{equation}
$$

The random variables $X$ are in all cases $\mathbb{Z}_{\ge 0}$

Sum
---
$X_i$ are independent random variables.

$$
\begin{equation}
    g_{(\sum X_i)}(t) = E[t^{\sum X_i}] = E\left[\prod t^{X_i} \right] = \prod E[t^{X_i}] = \prod g_{X_i}(t)
\end{equation}
$$

Scale
-----

$$
\begin{equation}
    g_{aX}(t) = E[t^{aX}] = E[(t^a)^X] = g_{X}(t^a)
\end{equation}
$$

Translation
-----------

$$
\begin{equation}
    g_{X+b}(t) = E[t^{X+b}] = E[t^Xt^b] = E[t^X]t^b = g_{X}(t)t^b
\end{equation}
$$

Dirac
-----

$$
\begin{align}
    g_{\delta(a)}(t) &= \sum\limits_{k\in\mathbb{Z}_{\ge 0}} \delta(a)(k) t^k \nonumber \\
                     &= \sum\limits_{k\in\mathbb{Z}_{\ge 0}} \delta_a(k) t^k \nonumber \\
                     &= t^a \nonumber \\
\end{align}
$$

Poission
--------
$$
\begin{align}
    g_{\text{Po}(m)}(t) &= \sum\limits_{k\in\mathbb{Z}_{\ge 0}} \text{Po}(m)(k)t^k \nonumber \\
                        &= \sum\limits_{k\in\mathbb{Z}_{\ge 0}} e^{-m}\frac{m^k}{k!}t^k \nonumber \\
                        &= e^{-m}\sum\limits_{k\in\mathbb{Z}_{\ge 0}} \frac{(mt)^k}{k!} \nonumber \\
                        &= e^{-m}e^{mt} \nonumber \\
                        &= (e^{t-1})^m
\end{align}
$$

Binomial
--------
$$
\begin{align}
    g_{\text{Bin}(n, p)}(t) &= \sum\limits_{k=0}^n \text{Bin}(n, p)(k)t^k \nonumber \\
                            &= \sum\limits_{k=0}^n \binom{n}{k} p^k(1-p)^{n-k}t^k \nonumber \\
                            &= \sum\limits_{k=0}^n \binom{n}{k} (pt)^k(1-p)^{n-k} \nonumber \\
                            &= (pt + (1-p))^n
\end{align}
$$

Geometric
---------
$$
\begin{align}
    g_{\text{Ge}(p)}(t) &= \sum\limits_{k\in\mathbb{Z}_{\ge 0}} \text{Ge}(p)(k) t^k \nonumber \\
                        &= \sum\limits_{k\in\mathbb{Z}_{\ge 0}} p(1-p)^k t^k \nonumber \\
                        &= p\sum\limits_{k\in\mathbb{Z}_{\ge 0}} ((1-p)t)^k \nonumber \\
                        &= \frac{p}{1-(1-p)t}, \quad |t| < \frac{1}{1-p}
\end{align}
$$
