---
title: Is it really random?
date: '2024-11-07T12:00:00.000Z'
categories: []
keywords: []
slug: really-random
---

I was using Python's [random](https://docs.python.org/3/library/random.html) library today, when I started getting the same numbers in a row for a random integer.

In all likelihood, it was just a fluke - luck wanted me to see those numbers a few times in a row. But it planted a seed!

I could test if random.randint() really is behaving with an equal distribution over the long run...

[26 lines of Python later](https://gist.github.com/bennett39/ac323e17acdcccd66fad3c8487eb3af8), I have a fun little toy program that let me try it out myself.

Want to know whether the random library tends toward even distributions in the long run (i.e. 1,000,000+ iterations)? Download the code and play with it yourself!
