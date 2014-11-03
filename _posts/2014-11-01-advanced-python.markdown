---
layout: post
title: "Advanced Python"
date: 2014-11-03 09:43:24
categories: python
---

[WIP]

functions
=========


classes
=======


memory
======
memoryview/buffer
gc/refcount
__slots__



#http://docs.python-guide.org/en/latest/writing/gotchas/
#http://stackoverflow.com/a/531327/905596

memoryview/buffer
-----------------

garbage collect
---------------

descriptor
----------

variable bounding
-----------------

local/global/free-variable
--------------------------
function.__closure__ #the functions free variables (read only)


mro (new vs. old)
-----------------

metaclasses
-----------
http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example

function attributes
-------------------

method attributes
-----------------
im_self
im_func

execution model
---------------

global/nonlocal
---------------
"lexical scoping"
with global
```
i = 0
def main():
    def on_key(keycode):
        global i
        i += 1
```

python2 without global
```python
def main():
    state = {'i': 0}
    def on_key(keycode):
        state["i"] += 1
```

python3 without global (using nonlocal)
```python
def main():
    i = 0
    def on_key(keycode):
        nonlocal i
        i += 1
```

late closure binding
--------------------
map(lambda f: f(2), map(lambda i: lambda x: i * x, range(5)))
map(lambda f: f(2), [lambda x: i * x for i in range(5)])
map(lambda f: f(2), [lambda x, i=i: i * x for i in range(5)])

#should use partial instead


blabla
------
def f_cached(x, _cache={}):
    if x not in _cache:
        _cache[x] = f(x)
    return _cache[x]


__slots__
---------

itertools/functools
-------------------

execution/data-model
--------------------
#coincides with other stuff as well


__new__
-------


defaultdict
-----------

defaultdict
-----------
defaultdict(int)
defaultdict(str)
defaultdict(A) :: {_: A}



>>> a = 256
>>> b = 256
>>> a is b
True
>>> c = 257
>>> d = 257
>>> c is d
False

descriptor
----------
https://docs.python.org/2/howto/descriptor.html

type
----
type('A', (object,), {'a': 1})


yield from
----------
python 3

yield and recieve
-----------------
PEP342

__subclasshook__ & ABCMeta.register
-----------------------------------

decorator syntax limitations
----------------------------
https://groups.google.com/forum/#!topic/python-ideas/GhBc2vxkDlE


weakref
-------
http://pymotw.com/2/weakref/
used for caches among other things


nested with
-----------

hash(1) == hash(1.0)
--------------------

unbound vs bound method
-----------------------



