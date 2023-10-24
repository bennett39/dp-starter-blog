---
title: Testing Django Admin Commands
description: Make sure your commands don’t break
date: '2021-09-27T11:04:30.731Z'
categories: []
keywords: []
slug: /@bennettgarner/testing-django-admin-commands-36b7d1ebefe2
---

![](/Users/bennettgarner/Repos/medium-export-4b46aa4e91f20dbf349cd1ed9133a2978c8dcbbd9f7d7b84cef20f84ed36ffda/posts/md_1643327843943/img/1__j5QuhIq67F0P3gmcbOxrOg.png)

[Commands in Django](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/) allow you to write scripts for your application that you can run from the command line, using `manage.py`. Recently, I needed to write unit tests for custom Django commands.

This is the quick guide I wish I’d found first thing…

### Why test custom commands?

Custom Django admin commands are meant to be useful helper scripts that automate certain processes. They can start tasks, create users, check for issues, or anything else you might want them to do.

If you don’t use commands heavily or they’re just simple helpers for use in development, then you might not need to write unit tests for them.

However, my team uses custom commands to automate complex processes, start background [worker tasks](https://medium.com/swlh/python-developers-celery-is-a-must-learn-technology-heres-how-to-get-started-578f5d63fab3), and create sandbox users on our application. We use custom commands heavily. Additionally, because they rely on other code in our application, they’re prone to breaking whenever the underlying structure is refactored.

For those reasons, we need unit tests for custom commands.

### Unit Tests for Django Admin Commands

It turns out that writing tests for a Django admin command is fairly easy (even if the steps are slightly buried in the documentation).

[**Testing tools | Django documentation | Django**  
docs.djangoproject.com](https://docs.djangoproject.com/en/2.2/topics/testing/tools/#management-commands "https://docs.djangoproject.com/en/2.2/topics/testing/tools/#management-commands")[](https://docs.djangoproject.com/en/2.2/topics/testing/tools/#management-commands)

Django provides a `call_command()` function in `django.core.management` that allows you to programmatically trigger a command from within your Python code.

So, in order to test a command:

### Things to Note

1.  We captured `stdout` with a `StringIO` instance. That means you can do something like, `self.assertIn('Expected output', out.getvalue())`
2.  We can provide `args` and `kwargs` to the command using a list and a dictionary respectively
3.  Once you’ve called the command, it’s up to you to add assertions below about the state of your application after the command has run

### Hope that helps!

Have questions about how to test Django admin commands? Send me an email or leave a comment below!

### Like what you’ve read here?

I share my best content with my email list for free.

[Join 500 other developers currently in my email series.](https://sunny-architect-5371.ck.page/0a60026a5d)