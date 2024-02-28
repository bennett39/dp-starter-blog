---
title: "Overdesigning your code leads to underperformance"
description:
date: '2024-02-28T12:00:00.000Z'
categories: []
keywords: []
slug: overdesign-underperform
---

Often, that brilliant design idea or fancy new tool isn’t speeding things up. It’s slowing you down.

This is especially true for tools designed to be used at scale. They deliberately introduce complexity in order to add scalability.

But if you’re not at that scale yet, you don’t need the tool.

Adding complexity often seems like it’ll be faster/better. But until you test your assumption, you can’t really be sure!

This is true for database indices, parallelization, caching, data pipelines, and a ton of other moments working as a developer.

We assume that the cool, new architecture will be better! If you run with that assumption, you risk introducing unneeded complexity into your application. A far simpler solution could be just as performant, if not more.

The lesson is to build the simple version first, then test your assumptions about the more complex version.

Often, the simple version is fast enough & able to handle what you need. Don’t overdesign at the outset.

Then, when your simple solution reaches the limits of its scalability, find the bottleneck and optimize for the bottleneck.
