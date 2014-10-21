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
    \label{eq:generatingfunctiondefinition}
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
    g_{(\sum X_i)}(t) \overset{\eqref{eq:generatingfunctiondefinition}}{=} E[t^{\sum X_i}] = E\left[\prod t^{X_i} \right] = \prod E[t^{X_i}] \overset{\eqref{eq:generatingfunctiondefinition}}{=} \prod g_{X_i}(t)
\end{equation}
$$

Scale
-----

$$
\begin{equation}
    g_{aX}(t) \overset{\eqref{eq:generatingfunctiondefinition}}{=} E[t^{aX}] = E[(t^a)^X] \overset{\eqref{eq:generatingfunctiondefinition}}{=} g_{X}(t^a)
\end{equation}
$$

Translation
-----------

$$
\begin{equation}
    g_{X+b}(t) \overset{\eqref{eq:generatingfunctiondefinition}}{=} E[t^{X+b}] = E[t^Xt^b] = E[t^X]t^b \overset{\eqref{eq:generatingfunctiondefinition}}{=} g_{X}(t)t^b
\end{equation}
$$

Evaluate $p_X(k)$
-----------------

$$
\begin{align}
    \frac{d^k}{k!dt^k}g_X(t=0) &\overset{\eqref{eq:generatingfunctiondefinition}}{=} \frac{d^k}{k!dt^k}E[t^X]\Bigg|_{t=0} \nonumber \\
                             &= \frac{d^k}{k!dt^k}\sum_{k'} t^{k'} p_X(k') \Bigg|_{t=0} \nonumber \\
                             &= \frac{1}{k!}\sum_{k'} p_X(k') \frac{d^k}{dt^k} t^{k'} \Bigg|_{t=0} \nonumber \\
                             &= \frac{1}{k!}\sum_{k'} p_X(k') \frac{k'!}{(k'-k)!}t^{k'-k} \Bigg|_{t=0} \nonumber \\
                             &= \frac{1}{k!}\sum_{k'} p_X(k') \frac{k'!}{(k'-k)!}0^{k'-k} \nonumber \\
                             &= \frac{1}{k!}\sum_{k'} p_X(k') \frac{k'!}{(k'-k)!}\delta(k'-k) \nonumber \\
                             &= \frac{1}{k!}\sum_{k'=k} p_X(k') \frac{k'!}{(k'-k)!}\delta(k'-k) \nonumber \\
                             &= \frac{1}{k!} p_X(k) \frac{k!}{0!} \cdot 1 \nonumber \\
                             &= p_X(k)

\end{align}
$$

Dirac
-----

$$
\begin{align}
    g_{\delta(a)}(t) &\overset{\eqref{eq:generatingfunctiondefinition}}{=} \sum\limits_{k\in\mathbb{Z}_{\ge 0}} \delta(a)(k) t^k \nonumber \\
                     &= \sum\limits_{k\in\mathbb{Z}_{\ge 0}} \delta_a(k) t^k \nonumber \\
                     &= t^a
\end{align}
$$

Poission
--------

$$
\begin{align}
    g_{\text{Po}(m)}(t) &\overset{\eqref{eq:generatingfunctiondefinition}}{=} \sum\limits_{k\in\mathbb{Z}_{\ge 0}} \text{Po}(m)(k)t^k \nonumber \\
                        &= \sum\limits_{k\in\mathbb{Z}_{\ge 0}} e^{-m}\frac{m^k}{k!}t^k \nonumber \\
                        &= e^{-m}\sum\limits_{k\in\mathbb{Z}_{\ge 0}} \frac{(mt)^k}{k!} \nonumber \\
                        &= e^{-m}e^{mt} \nonumber \\
                        &= (e^{t-1})^m = e^{m(t-1)}
\end{align}
$$

Binomial
--------

$$
\begin{align}
    g_{\text{Bin}(n, p)}(t) &\overset{\eqref{eq:generatingfunctiondefinition}}{=} \sum\limits_{k=0}^n \text{Bin}(n, p)(k)t^k \nonumber \\
                            &= \sum\limits_{k=0}^n \binom{n}{k} p^k(1-p)^{n-k}t^k \nonumber \\
                            &= \sum\limits_{k=0}^n \binom{n}{k} (pt)^k(1-p)^{n-k} \nonumber \\
                            &= (pt + (1-p))^n \label{eq:binomial}
\end{align}
$$


Bernoulli
---------

$$
\begin{align}
    g_{\text{Be}(p)} &= g_{\text{Bin}(n=1, p)} \nonumber \\
                     &\stackrel{\eqref{eq:binomial}}{=} pt + (1-p)
\end{align}
$$

Geometric
---------

$$
\begin{align}
    g_{\text{Ge}(p)}(t) &\overset{\eqref{eq:generatingfunctiondefinition}}{=} \sum\limits_{k\in\mathbb{Z}_{\ge 0}} \text{Ge}(p)(k) t^k \nonumber \\
                        &= \sum\limits_{k\in\mathbb{Z}_{\ge 0}} p(1-p)^k t^k \nonumber \\
                        &= p\sum\limits_{k\in\mathbb{Z}_{\ge 0}} ((1-p)t)^k \nonumber \\
                        &= \frac{p}{1-(1-p)t}, \quad |t| < \frac{1}{1-p}
\end{align}
$$

First Success
------------

$$
\begin{align}
    g_{\text{Fs}(p)}(t) &\overset{\eqref{eq:generatingfunctiondefinition}}{=} \sum\limits_{k\in\mathbb{Z}_{\ge 1}} \text{Fs}(p)(k) t^k \nonumber \\
                        &= \sum\limits_{k\in\mathbb{Z}_{\ge 1}} p(1-p)^{k-1} t^k \nonumber \\
                        &= \frac{p}{1-p}\sum\limits_{k\in\mathbb{Z}_{\ge 1}} ((1-p)t)^k \nonumber \\
                        &= \frac{p}{1-p}\left(\sum\limits_{k\in\mathbb{Z}_{\ge 0}} ((1-p)t)^k - 1\right) \nonumber \\
                        &= \frac{p}{1-p}\left(\frac{1}{1-(1-p)t} - 1\right),\quad |(1-p)t|<1 \nonumber \\
                        &= \frac{p}{1-p} \frac{1-(1-(1-p)t)}{1-(1-p)t} \nonumber \\
                        &= \frac{pt}{1-(1-p)t},\quad |(1-p)t|<1
\end{align}
$$
