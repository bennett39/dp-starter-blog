---
title: '3 approaches to technical debt'
description: Hint - You don't always have to fix it
date: '2023-12-27T16:04:30.015Z'
categories: []
keywords: []
slug: tech-debt
---

There are three approaches to technical debt:

1. Ignore it
2. Tackle it right now
3. Add it to the backlog for prioritization

Great engineers know the difference between these options and when to pick each. Indeed, a big part of working as a senior engineer is about triage - developing good judgement about what's worth fixing & when.

Including ignoring some issues! Sometimes you just ignore technical debt that isn’t causing harm at the moment. Optimizing something that isn’t broken or a bottlneck can be a waste of time.

If it’s a small lift or you can see a clear answer, then tackling it in a current PR is okay. No need to go through a big process to do a small fix. Often, it's best to fix a problem when you see it and already have the context to resolve it. But great engineers also don't take a long time on a huge refactor without talking to their team first.

Adding debt to the backlog creates some work scoping/writing/refining. That work can be worth it for bigger tech debt items that are tricky to resolve but blocking progress on other projects. The benefit is the whole team gets to decide whether and when we need to tackle this problem. It's a tradeoff, since writing a ticket, refining it, and waiting for it to get prioritized into a sprint takes much more time.

As you can see, there are tradeoffs to each. Ignoring issues can be a good approach, but it can also come back to bite you. Fixing issues right away is often quickest, but it means spending in-sprint time on a refactor that wasn't planned. On the other hand, adding tech debt to the backlog lets the whole team plan & prioritize the work, but it's the slowest option, often leading to languishing tech debt in the backlog.

Which option you pick depends on the problem, your abilities, and your team's velocity & culture. Getting good at these judgement calls is a hallmark of a senior engineer.
