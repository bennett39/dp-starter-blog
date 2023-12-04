---
title: The hard-to-learn skill senior engineers have in common
description: Problem solving starts with representing the problem well
date: '2023-12-04T16:04:30.015Z'
categories: []
keywords: []
slug: data-modeling
---

There's a skill you use all the time as a developer, increasingly as you get more senior. But it's rarely explicitly taught & takes experience to learn well.

Getting good at it makes you much more effective at your job. Being bad at it can limit your career.

I'm talking about data modeling - taking a real-world problem & turning it into software concepts.

Most often data modeling takes the form of "How are we going to store & query these things?" Database considerations (though there are other data modeling problems outside database structure).

I can't give a whole crash course on data modeling in this one post. But here's a helpful heuristic I wish someone had told me years ago:

- *Entities* model things in the real world that can be uniquely identified
- *Attributes* are characteristics of an entity (e.g. name, category, age)
- *Relationships* are the connections between entities

For your first draft of the data model for a given problem, think what are the entities? What attributes do the entities have? How are they related?

Your entities become your tables in the database. The attributes are the columns in those tables. And the relationships are foreign keys.

There's more to it than that & it's not always that simple. But a lot of the time it is! And this simple heuristic is nearly always helpful.
