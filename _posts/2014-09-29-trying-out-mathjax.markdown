---
layout: post
title:  "Trying out MathJax"
date:   2014-09-28 15:32:34
categories: latex math mathjax
---
<style TYPE="text/css">
    code.has-jax {font: inherit; font-size: 100%; background: inherit; border: inherit;}
</style>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [['$','$'], ['\\(','\\)']],
            displayMath: [['$$','$$'], ['\\[','\\]']],
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'], // removed 'code' entry
            processEscapes: false,
        },
        TeX: { equationNumbers: {autoNumber: "AMS"} }
    });
    MathJax.Hub.Queue(function() {
        var all = MathJax.Hub.getAllJax(), i;
        for(i = 0; i < all.length; i += 1) {
            all[i].SourceElement().parentNode.className += ' has-jax';
        }
    });
</script>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

Trying out inline equation, equation \eqref{eq:equation}, multiline equation \eqref{eq:multiline} and cases \eqref{eq:cases}.

Inline
------
Pre $E = mc^2$ post.

Equation
--------
\begin{equation}
    \label{eq:equation}
    E = mc^2
\end{equation}

Split
-----
$$
\begin{equation}
    \label{eq:multiline}
    \begin{split}
        A &=& B \\
          &=& C
    \end{split}
\end{equation}
$$

Cases
-----
$$
\begin{equation}
    \label{eq:cases}
    f(n) = \begin{cases} n/2 &\mbox{if } n \equiv 0 \\
    (3n +1)/2 & \mbox{if } n \equiv 1 \end{cases} \pmod{2}
\end{equation}
$$
