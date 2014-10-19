---
layout: post
title:  "Conditional of Gaussian distribution"
date:   2014-10-19 18:01:00
categories: probability
---

Problem
-------

Given $(X, Y)\in N(\mu, \Lambda)$ find
$Y|X=x$.

Gaussian density
----------------

$$
\begin{equation}
    \label{eq:gaussiandefinition}
    f_{N(\mu, \Lambda)}(x) =
        \left(\frac{1}{2\pi}\right)^{n/2} \frac{1}{\sqrt{|\Lambda|}} e^{
            -\frac{
                1
            }{
                2
            }
            (x-\mu)'\Lambda^{-1}(x-\mu)
        }
\end{equation}
$$

Solution
--------

Symbols used

$$
\begin{equation}
    E[X] = \mu_X,\quad
    Var[X] = \sigma_x^2,\quad
    \rho = Corr(X, Y) = \frac{Cov(X, Y)}{\sigma_X\sigma_Y}
\end{equation}
$$

In our case we have (by definition)

$$
\begin{equation}
    \Lambda = \begin{pmatrix}
                  \sigma_X^2 & \rho\sigma_X\sigma_Y \\
        \rho\sigma_X\sigma_Y &           \sigma_Y^2
    \end{pmatrix}
\end{equation}
$$

and the inverse is

$$
\begin{equation}
    \Lambda^{-1} = \frac{1}{1-\rho^2}\begin{pmatrix}
        \frac{1}{\sigma_X^2} & -\frac{\rho}{\sigma_X\sigma_Y} \\
        -\frac{\rho}{\sigma_X\sigma_Y} & \frac{1}{\sigma_Y^2}
    \end{pmatrix}
\end{equation}
$$

From definition of conditional distribution and the definition
of gaussian density \eqref{eq:gaussiandefinition} we get

$$
\begin{align}
    f_{Y|X=x}(y) &= \frac{f_{X, Y}(x, y)}{f_X(x)} \nonumber \\
                 &= \frac{
                    \frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}}
                    e^{
                        -\frac{1}{2(1-\rho^2)}
                        \left(
                            \left(\frac{x-\mu_X}{\sigma_X}\right)^2
                            -2\rho\frac{(x-\mu_X)(y-\mu_Y)}{\sigma_X\sigma_Y}
                            +\left(\frac{y-\mu_Y}{\sigma_Y}\right)^2
                        \right)
                    }
                }{
                    \frac{1}{\sqrt{2\pi}\sigma_X}
                    e^{-\frac{1}{2}\left(
                        \frac{x-\mu_X}{\sigma_X}
                    \right)^2}
                } \nonumber \\
               &= \frac{1}{\sqrt{2\pi}\sigma_Y\sqrt{1-\rho^2}}
                e^{
                    -\frac{1}{2(1-\rho^2)}
                        \left(
                            \left(\frac{x-\mu_X}{\sigma_X}\right)^2\rho^2
                            -2\rho\frac{(x-\mu_X)(y-\mu_Y)}{\sigma_X\sigma_Y}
                            +\left(\frac{y-\mu_Y}{\sigma_Y}\right)^2
                        \right)
                } \nonumber \\
               &= \frac{1}{\sqrt{2\pi}\sigma_Y\sqrt{1-\rho^2}}
                e^{
                    -\frac{1}{2\sigma_Y^2(1-\rho^2)}\left(
                        y-\mu_Y-\rho\frac{\sigma_Y}{\sigma_X}(x-\sigma_X)
                    \right)^2
                } \nonumber \\
               &= f_{
                    N\left(
                        \mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(x-\sigma_X),\,
                        \sigma_Y^2(1-\rho^2)
                    \right)
                }(y) \nonumber \\
                & \Box
\end{align}
$$
