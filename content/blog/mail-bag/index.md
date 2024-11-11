---
title: Mail bag
date: '2024-11-11T12:00:00.000Z'
categories: []
keywords: []
slug: mail-bag
---

I have a couple reader emails that I haven't responded to. Seems like a good opportunity to share out with the group!


> "It is almost impossible to generate a random number on any language."

Thanks for pointing that out. I'm aware that random numbers aren't purely random & if you know the seed you can even deterministically predict the next results. That's why they're referred to as pseudo-random numbers.

That said, today's algorithms are really good. Python uses a [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) while numpy has a preference for [PCG](https://en.wikipedia.org/wiki/Permuted_congruential_generator).

Notice that the code in [my last post](https://daily.developerpurpose.com/really-random/) isn't asking whether the number is truly random/deterministic. Instead, I wondered if there are even distributions of results over the long term.

If you run the code, you'll find that the standard Python implementation of pseudo-random numbers does indeed tend toward even distribution of results. There are much more rigorous ways to measure that than my crude experiment, however! See Wikipedia for Mersenne Twisters: "Passes numerous tests for statistical randomness, including the [Diehard tests](https://en.wikipedia.org/wiki/Diehard_tests) and most, but not all of the [TestU01](https://en.wikipedia.org/wiki/TestU01) tests."


> "pseudo random. dont rely on crappy rnd functions/implementations for production"

I've already covered the "pseudo random" comment above. As for "crappy," I think the mathemeticians behind Mersenne Twisters & PCG would like to speak with you...

As for relying on them in production, it really depends what you're using them for! Should you do highly sensitive cryptography with pseudo-random numbers? No! (Though you probably shouldn't be doing your own cryptography at all...)

Can you use Python's `random` library to seed some test jobs with random inputs in your testing account? Of course!

Be careful before you jump to conclusions about how I was using the random library!


> "We are paying several times more for our cloud deployment than we did for our physical colos, but we are also operating with a much smaller team than we used to."

I wrote about how the [cloud might not be better](https://daily.developerpurpose.com/cloud-better/), and the conclusion was that there's no right answer for everyone. You have to run your own numbers.

But at least do yourself the service of running the numbers! I wonder if the increased cloud costs are really worth the savings in worker hours.

Obviously building and operating your own server racks is going to add overhead. But there are also in between options like more slimmed down cloud offerings at Digital Ocean or using managed data center racks like Deft.

I'm just saying that cloud shouldn't always be the de facto choice.


> "What a strange read. You recommend doing less but say nothing about how. But how do you decide what to not do?"

This was in response to my writing on [mental load](https://daily.developerpurpose.com/mental-load/).

I can't tell you exactly what you should do less of. I don't know your life. But I do know that our culture tends to be additive... That is to say that when we have a problem we want to add on more things to solve it.

For example, when you feel stressed, go for a run, book a massage, or see a therapist. When you want to get a promotion, you take on more projects, speak up in meetings, and lobby your boss.

One possibility, though, is to _subtract_. Feeling stressed? Find the stressors in your life & aim to reduce or eliminate them. Want a promotion? Focus on 1-2 impactful projects & deliver really high quality.

Your to-do list will already never get fully done. So, try taking things off your list, rather than adding to it.

--

A great wrap up note from Sean D.:

> Three related stoic quotes I remind myself of daily:
> 1. You can't learn what you already know
> 2. You don't have to have an opinion
> 3. Never be heard complaining; even to yourself

