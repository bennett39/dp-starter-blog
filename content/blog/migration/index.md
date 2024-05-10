---
title: "Migration is always the hardest part"
description:
date: '2024-05-10T12:00:00.000Z'
categories: []
keywords: []
slug: migration
---

We had a big release this week that the whole team has been working on. A lot is changing about how the app is structured.

Here's the thing: It was relatively easy to write the code for the new features we wanted to support. With newly created test cases, everything works great!

The hardest part of the whole project was creating a migration strategy from the old way the app worked & how our data was structured, to the new way.

We wanted a seamless transition for our users. Jobs & tasks that were in progress should have all their data in the correct state in the new version of the app.

I've done several of these big releases in my career, now. Migration has always been the hardest part!

Here are a few guidelines that make it easier:
- Make small changes, whenever possible. The smaller the migration, the less room there is for mistakes.
- Plan for the migration from day 1. It shouldn't be an afterthought.
- Start developing the migration well ahead of the release date. Take a snapshot of production data & use that to build the migration, if possible, not just test jobs.
