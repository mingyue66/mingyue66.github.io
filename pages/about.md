---
layout: page
title: About
description: Personal information
keywords: Mingyue Huo
comments: true
menu: About
permalink: /about/
---
In all things of nature there is something of the marvelous. --Aristotle, Parts of Animals


## Profile
欢迎来到我的博客，我会在这里分享关于声音的有趣话题！ Hi, welcome to my personal blog! I am Mingyue, a graduate student at University of Illinois at Urbana-Champaign. Super interested in linguisitcs, especially about sound. I will write down my thoughts on interesting topics about human speech, signal processing, etc. Feel free to contact me via email if you have any comments on my blogs. 

<ul>
{% for website in site.data.social %}
<li>{{website.sitename }}：<a href="{{ website.url }}" target="_blank">@{{ website.name }}</a></li>
{% endfor %}
{% if site.url contains 'foolishhmy.com' %}

{% endif %}
</ul>


## Skills

{% for skill in site.data.skills %}
### {{ skill.name }}
<div class="btn-inline">
{% for keyword in skill.keywords %}
<button class="btn btn-outline" type="button">{{ keyword }}</button>
{% endfor %}
</div>
{% endfor %}
