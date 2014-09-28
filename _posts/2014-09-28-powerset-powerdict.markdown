---
layout: post
title:  "powerset & powerdict"
date:   2014-09-28 15:32:34
categories: python itertools
---

Really nice to be able to list all combinations of a set or a dictionary.
For example if you are testing a database update and want to check invariants
under all possible updates.

<script src="https://gist.github.com/Jim-Holmstroem/d6df644ba4062f02e59d.js"></script>

Usage
-----

{% highlight python %}
from __future__ import print_function
test = print
map(
    test,
    powerdict({'a': 1, 'b': 2, 'c': 3})
)
{% endhighlight %}

Note
----
It also runs the test with an empty dictionary, and thereby catching the trivial case.
