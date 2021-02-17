---
layout: page
title: About
description: Personal information
keywords: Mingyue Huo
comments: true
menu: About
permalink: /about/
---
欢迎来到我的博客，我会在这里分享关于声音的有趣话题！
Hi, welcome to my personal blog! I will write down my thoughts on interesting topics, especially about human speech and other sounds. Feel free to contact me via email if you have any comments on my blogs.  
ようこそ！（おもに）音と声についての個人的な感想を記録しているブログです！よろしくね！

## Profile
My name is Mingyue Huo (霍明月). I am a first-year master student at University of Illinois at Urbana-Champaign, department of East Asian Languages and Cultures. I received my bachelor's degree of Japanese and International Economics from Shanghai International Studies University (上海外国语大学). 
<ul>
{% for website in site.data.social %}
<li>{{website.sitename }}：<a href="{{ website.url }}" target="_blank">@{{ website.name }}</a></li>
{% endfor %}
{% if site.url contains 'foolishhmy.com' %}
</li>
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
