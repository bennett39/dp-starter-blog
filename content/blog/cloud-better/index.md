---
title: Is the cloud really better?
date: '2024-10-24T12:00:00.000Z'
categories: []
keywords: []
slug: cloud-better
---

We've given so much of our lives over to the cloud. And in software engineering, nearly everything runs on the cloud.

It really feels like the cloud is the default. If you have a giant external hard drive where you keep all your photos, you're an outlier. Same goes for startup tech, if you're hosting your web app on-premise you're also an outlier.

I've been at small and big companies where I get to see the monthly AWS or GCP bill. It's huge! So, what are we paying for?

The promise of the cloud was scalability, security, and cost. Let's tackle those one at a time.
- Most apps have predictable usage patterns and don't need infinite scalability. With a little buffer, you can roughly estimate how much load you can expect.
- Security of servers has become much easier to manage. There's not some magical, mystical art of security that's too hard to learn. You can host your own servers while following a few best practices.
- It's pretty clear from [recent case studies](https://world.hey.com/dhh/we-have-left-the-cloud-251760fb) that the cloud is much more expensive than hosted solutions for many applications.

Now, I would not call myself an expert in cloud vs hosted solutions. And there are some very real times when cloud solutions make sense (an early product where you don't want to sink time into infra, massive products that really do need huge swings in scalability, mission critical software that really requires 99.99999% uptime). But I do think it's worth at least questioning whether the cloud is worth the premium we're paying for it.

What's more, we suffer as developers from the janky experience most cloud providers offer us. One look at the AWS admin panel will make you want to cry. We understand less about how our applications work because how AWS works is a black box to most of us.

"Is the cloud really better?" - that's the question I'd encourage you to ask. It may really be better for you! But do your own reasoning.
