---
title: "Reinforcement learning produces faster algorithms"
description:
date: '2024-02-09T12:00:00.000Z'
categories: []
keywords: []
slug: alphadev-sorting
---

A little something different. After a few days away from the daily email, I came across this story today...

Most developers know about merge sort or bubble sort. But have you heard about AlphaDev sort?

Researchers at [Google built AlphaDev](https://deepmind.google/discover/blog/alphadev-discovers-faster-sorting-algorithms/) - a machine learning algorithm - to optimize assembly code of common algorithms.

The summary: they found a way to make sorting faster. This has the potential to be a big deal, since we rely on sorting all the time as developers.

It's worth reading the article, but the basic story is the ML algorithm writes lines of assembly code. The code runs and the algorithm learns whether the code sorted correctly and how fast it worked. For small arrays, the new assembly code AlphaDev generated is 70% faster.

Over many iterations, AlphaDev found novel approaches to sorting that simplify the assembly code that gets executed. Under the hood, AlphaDev's new sorting algorithm powers [some sorting functions in C++](https://reviews.llvm.org/D118029).

To me, this is the real promise of machine learning when it comes to coding. AI won't be stealing your job, but it will be optimizing algorithms for well-understood problems. Places where a small improvement can have ripple effects across the entire industry.
