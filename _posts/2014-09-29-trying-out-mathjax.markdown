---
layout: post
title:  "Trying out MathJax"
date:   2014-09-28 15:32:34
categories: mathjax
---

Used the samples from [mathjax.org demo] [mathjax] with proper code indentations
and wrapping them in latex-equations.

References to the equations:
\eqref{eq:lorenz},
\eqref{eq:cauchy},
\eqref{eq:cross},
\eqref{eq:choose},
\eqref{eq:ramanujan},
\eqref{eq:rogers},
\eqref{eq:maxwell},


The Lorenz Equations
--------------------

$$
\begin{equation}
    \label{eq:lorenz}
    \begin{aligned}
        \dot{x} & = \sigma(y-x) \\
        \dot{y} & = \rho x - y - xz \\
        \dot{z} & = -\beta z + xy
    \end{aligned}
\end{equation}
$$

The Cauchy-Schwarz Inequality
-----------------------------

$$
\begin{equation}
    \label{eq:cauchy}
    \left(
        \sum_{k=1}^n a_k b_k
    \right)^2
    \leq
    \left(
        \sum_{k=1}^n a_k^2
    \right)
    \left(
        \sum_{k=1}^n b_k^2
    \right)
\end{equation}
$$

A Cross Product Formula
-----------------------

$$
\begin{equation}
    \label{eq:cross}
    \mathbf{V}_1 \times \mathbf{V}_2 =
    \begin{vmatrix}
        \mathbf{i}                    & \mathbf{j}                    & \mathbf{k} \\
        \frac{\partial X}{\partial u} & \frac{\partial Y}{\partial u} & 0 \\
        \frac{\partial X}{\partial v} & \frac{\partial Y}{\partial v} & 0
    \end{vmatrix}
\end{equation}
$$

Probability of getting $k$ heads when flipping $n$ coins
--------------------------------------------------------

$$
\begin{equation}
    \label{eq:choose}
    P(E) = {n \choose k} p^k (1-p)^{n-k}
\end{equation}
$$

An Identity of Ramanujan
------------------------

$$
\begin{equation}
    \label{eq:ramanujan}
    \frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac{2\pi}{5}}} =
    1+\frac{
        e^{-2\pi}
    }{
        1+\frac{
            e^{-4\pi}
        }{
            1+\frac{
                e^{-6\pi}
            }
            {
                1+\frac{e^{-8\pi}} {1+\ldots}
            }
        }
    }
\end{equation}
$$

A Rogers-Ramanujan Identity
---------------------------

$$
\begin{equation}
    \label{eq:rogers}
    1 + \frac{q^2}{(1-q)} + \frac{q^6}{(1-q)(1-q^2)} + \cdots =
    \prod_{j\in\mathbb{Z}_{\ge 0}}\frac{1}{(1-q^{5j+2})(1-q^{5j+3})},
    |q|\lt 1
\end{equation}
$$

Maxwell's Equations
-------------------

$$
\begin{equation}
    \label{eq:maxwell}
    \begin{aligned}
        \nabla \times \vec{\mathbf{B}} - \frac{\partial\vec{\mathbf{E}}}{c\partial t}   & = \frac{4\pi\vec{\mathbf{j}}}{c} \\
        \nabla \cdot \vec{\mathbf{E}}                                                   & = 4 \pi \rho \\
        \nabla \times \vec{\mathbf{E}}\, + \frac{\partial\vec{\mathbf{B}}}{c\partial t} & = \vec{\mathbf{0}} \\
        \nabla \cdot \vec{\mathbf{B}}                                                   & = 0
    \end{aligned}
\end{equation}
$$

Finally, while display equations look good for a page of samples the ability to mix math and text in a paragraph is also important. This expression $\sqrt{3x-1}+(1+x)^2$ is an example of an inline equation.  As you see, MathJax equations can be used this way as well, without unduly disturbing the spacing between lines.


[mathjax]: http://www.mathjax.org/demos/tex-samples/ 'Mathjax Demo'


The code looks neat
-------------------

I disregarded the code that renders the above code because I will
not make this post a [Quine] [quine].

<!-- The code inside highlight markdown is just a copy of the code above header "The code looks neat" -->
{% highlight latex%}

---
layout: post
title:  "Trying out MathJax"
date:   2014-09-28 15:32:34
categories: mathjax
---

Used the samples from [mathjax.org demo] [mathjax] with proper code indentations
and wrapping them in latex-equations.

References to the equations:
\eqref{eq:lorenz},
\eqref{eq:cauchy},
\eqref{eq:cross},
\eqref{eq:choose},
\eqref{eq:ramanujan},
\eqref{eq:rogers},
\eqref{eq:maxwell},


The Lorenz Equations
--------------------

$$
\begin{equation}
    \label{eq:lorenz}
    \begin{aligned}
        \dot{x} & = \sigma(y-x) \\
        \dot{y} & = \rho x - y - xz \\
        \dot{z} & = -\beta z + xy
    \end{aligned}
\end{equation}
$$

The Cauchy-Schwarz Inequality
-----------------------------

$$
\begin{equation}
    \label{eq:cauchy}
    \left(
        \sum_{k=1}^n a_k b_k
    \right)^2
    \leq
    \left(
        \sum_{k=1}^n a_k^2
    \right)
    \left(
        \sum_{k=1}^n b_k^2
    \right)
\end{equation}
$$

A Cross Product Formula
-----------------------

$$
\begin{equation}
    \label{eq:cross}
    \mathbf{V}_1 \times \mathbf{V}_2 =
    \begin{vmatrix}
        \mathbf{i}                    & \mathbf{j}                    & \mathbf{k} \\
        \frac{\partial X}{\partial u} & \frac{\partial Y}{\partial u} & 0 \\
        \frac{\partial X}{\partial v} & \frac{\partial Y}{\partial v} & 0
    \end{vmatrix}
\end{equation}
$$

Probability of getting $k$ heads when flipping $n$ coins
--------------------------------------------------------

$$
\begin{equation}
    \label{eq:choose}
    P(E) = {n \choose k} p^k (1-p)^{n-k}
\end{equation}
$$

An Identity of Ramanujan
------------------------

$$
\begin{equation}
    \label{eq:ramanujan}
    \frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac{2\pi}{5}}} =
    1+\frac{
        e^{-2\pi}
    }{
        1+\frac{
            e^{-4\pi}
        }{
            1+\frac{
                e^{-6\pi}
            }
            {
                1+\frac{e^{-8\pi}} {1+\ldots}
            }
        }
    }
\end{equation}
$$

A Rogers-Ramanujan Identity
---------------------------

$$
\begin{equation}
    \label{eq:rogers}
    1 + \frac{q^2}{(1-q)} + \frac{q^6}{(1-q)(1-q^2)} + \cdots =
    \prod_{j\in\mathbb{Z}_{\ge 0}}\frac{1}{(1-q^{5j+2})(1-q^{5j+3})},
    |q|\lt 1
\end{equation}
$$

Maxwell's Equations
-------------------

$$
\begin{equation}
    \label{eq:maxwell}
    \begin{aligned}
        \nabla \times \vec{\mathbf{B}} - \frac{\partial\vec{\mathbf{E}}}{c\partial t}   & = \frac{4\pi\vec{\mathbf{j}}}{c} \\
        \nabla \cdot \vec{\mathbf{E}}                                                   & = 4 \pi \rho \\
        \nabla \times \vec{\mathbf{E}}\, + \frac{\partial\vec{\mathbf{B}}}{c\partial t} & = \vec{\mathbf{0}} \\
        \nabla \cdot \vec{\mathbf{B}}                                                   & = 0
    \end{aligned}
\end{equation}
$$

Finally, while display equations look good for a page of samples the ability to mix math and text in a paragraph is also important. This expression $\sqrt{3x-1}+(1+x)^2$ is an example of an inline equation.  As you see, MathJax equations can be used this way as well, without unduly disturbing the spacing between lines.


[mathjax]: http://www.mathjax.org/demos/tex-samples/ 'Mathjax Demo'

{% endhighlight %}

[quine]: http://en.wikipedia.org/wiki/Quine_%28computing%29
