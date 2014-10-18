---
layout: post
title:  "List of generating functions"
date:   2014-10-18 15:16:00
categories: probability
---

Couldn't find any list of generating functions for distributions so I started
compiling my own. (They will be filled in as they appear in the wild)

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
    g_{X}(t) \overset{def}{=} E[t^X] = \begin{cases}
        \sum t^k p_X(k) &\quad X\, \text{discrete} \\
        \int t^k f_X(k) dx &\quad X\, \text{continuous} \\
    \end{cases}
\end{equation}
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
                            &= (pt + (1-p))^n \nonumber \\
                            &= ((t-1)p + 1)^n
\end{align}
$$


