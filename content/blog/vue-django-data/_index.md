---
title: Use Python & Django Data Inside Your Vue App
description: Two approaches to passing data
date: '2021-03-11T20:28:39.218Z'
categories: []
keywords: []
slug: /@bennettgarner/use-python-django-data-inside-your-vue-app-9565637b3b95
---

![](/Users/bennettgarner/Repos/medium-export-4b46aa4e91f20dbf349cd1ed9133a2978c8dcbbd9f7d7b84cef20f84ed36ffda/posts/md_1643327843943/img/1__lgunwCjBIZvosxo5W3HHQg.png)

I recently got a good [question from a reader](https://medium.com/@diegogaona/hi-bennet-thanks-for-your-great-articles-a66813b5e617):

> Using Vue CLI, how we can use Django data in Vue? Suppose I have a pandas dataframe or dictionary I want to pass to the Vue app, how to do it?

### Two Approaches to Passing Data

If you’re using [Vue with Django](https://medium.com/@diegogaona/hi-bennet-thanks-for-your-great-articles-a66813b5e617) as I’ve described, there are two ways to pass data to your components:

1\. [Expose an API for your data](https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c) and use `fetch` or `axios` inside your Vue component. (Usually inside the `mounted()` method)

2\. Pass the data in via the Django view/template and then set it as a prop on your vue component. For instance

def my\_view(request):  
    data = build\_your\_data()  
    return render(request, ‘test.html’, {‘data’: data}

Then in `test.html`:

<div id=”app”>  
  <my-component data={{ data }}>  
</div>

And your Vue component:

<template>  
  {{ data }}  
</template>  
  

<script>  
module.exports = {  
  props: \[‘data’\]  
}  
</script>

### Like what you’ve read here?

I share my best content with my email list for free.

[Join 500 other developers currently in my email series.](https://sunny-architect-5371.ck.page/0a60026a5d)