---
layout: page
title: About
description: Personal information
keywords: Mingyue Huo
comments: true
menu: About
permalink: /about/
---
*“In all things of nature there is something of the marvelous.”*
                              *--Aristotle, Parts of Animals*


## Profile
一个小菜鸟的博客，试图记录和分享关于声音、语言和音乐的有趣话题. Welcome to my personal blog! I will write down my thoughts on interesting topics about human speech, music and signal processing. Feel free to contact me via email if you have any comments. 

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
