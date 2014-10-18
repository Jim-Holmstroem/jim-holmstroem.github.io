---
layout: post
title:  "List of generating functions"
date:   2014-10-18 15:16:00
categories: probability
---

Couldn't find any list of generating functions for distributions so I started
compiling my own. (They will be filled in as they appear in the wild)


Poission
--------
$$
\begin{align}
    g_{\text{Po}(m)}(t) &= \sum\limits_{k\in\mathbb{Z}_{\ge 0}} e^{-m}\frac{m^k}{k!}t^k \nonumber \\
                        &= e^{-m}\sum\limits_{k\in\mathbb{Z}_{\ge 0}} \frac{(mt)^k}{k!} \nonumber \\
                        &= e^{-m}e^{mt} \nonumber \\
                        &= (e^{t-1})^m
\end{align}
$$

Binomial
--------
$$
\begin{align}
    g_{\text{Bin}(n, p)}(t) &= \sum\limits_{k=0}^n \binom{n}{k} p^k(1-p)^{n-k}t^k \nonumber \\
                            &= \sum\limits_{k=0}^n \binom{n}{k} (pt)^k(1-p)^{n-k} \nonumber \\
                            &= (pt + (1-p))^n \nonumber \\
                            &= ((t-1)p + 1)^n
\end{align}
$$