---
title: "Dealing with task saturation"
description:
date: '2024-01-23T12:00:00.000Z'
categories: []
keywords: []
slug: task-saturation
---

I love airplanes & all things aviation. Recently, I was reading about the top causes of accidents for general aviation pilots. One of the main factors in accidents is the pilot's task saturation.

Task saturation refers to having too many things to do at once. You get overwhelmed & make poor judgments.

As software developers, we're not flying airplanes thousands of feet above the ground. But we do face task saturation! When you're responding to a production outage or there's a customer-facing bug you need to resolve ASAP.

It's easy to become saturated. So, what can we learn from pilots?

## Make a plan

The safest approach is to triage your tasks & do the most important things first. In aviation, they have a saying to help pilots remember:

> Aviate, navigate, communicate

Most importantly, keep the plane in the air and flying level. Then, figure out where you are and where you want to go. Lastly, communicate your intentions.

For us developers, that might take the form of stabilize, diagnose, and communicate. For instance:

- Get the app running again by reverting or deploying an old image
- Figure out your initial guess of what happened & where we might need to go
- Communicate about what you did

These can & should happen rapidly. You can start the process of reverting the bad code with a good guess at what happened and then immediately communicate about it. But they should happen in order of importance.

We can't entirely eliminate task saturation, but having a plan for when stressful events arise goes a long way.
