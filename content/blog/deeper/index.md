---
title: How do I go deeper?
description: I received some emails asking how do you practically go one level deeper
date: '2023-11-25T16:04:30.015Z'
categories: []
keywords: []
slug: deeper
---

On Wednesday, I published a post stating that [software is all about abstraction](https://daily.developerpurpose.com/abstraction/). I suggested that you should try to go one level deeper to understand the layers you're building on top of.

I received some emails asking how do you practically go one level deeper? Could I give an example?

Sure:
- Assume you're a frontend engineer working in React. That's open source, so you could go read the React source code. So is the Node runtime & webpack/babel, those are other tools to play around with. Come to think of it, learn how JavaScript is executed by digging into [JS engines](https://en.wikipedia.org/wiki/JavaScript_engine).
- If you're a data scientist working in Python, then check out the source code and documentation for the libraries you use often like Pandas & Numpy. Learn how the C API works in Python & how numpy uses it. What about learning about how your big data is stored, even digging into the physical storage strategies.
- For mobile developers, there is tons to learn about how devices process & store information. Dig into the libraries you depend on. I'm not a mobile developer, so I don't even know what I don't know! I'm sure there are ways you can optimize performance by understanding the fundamentals of the runtime & limitations of devices.
- Working in robotics, you could spend a lifetime learning about how the code you write turns into electrical impulses that control the robot's motion. Modern robotics is often at the intersection of computer vision, which introduces even more complexity to dive into!

Basically, what are you building? When you build anything with code, you're relying on something else. It's guaranteed.

Learn about the things you're relying on. Then learn about what they're relying on. Rinse and repeat forever, because you'll never know it all!
