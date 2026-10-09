#!/usr/bin/env python3
"""Render GitHub Pages using only the Python standard library."""
from datetime import date
from html import escape
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
profile=json.loads((ROOT/'content/profile.json').read_text())
papers=json.loads((ROOT/'content/publications.json').read_text())
style_version=hashlib.sha256((ROOT/'stylesheet.css').read_bytes()).hexdigest()[:10]
def esc(s): return escape(str(s),quote=True)
def link(u,n): return f'<a href="{esc(u)}">{esc(n)}</a>'
def links(items): return ' <span aria-hidden="true">/</span> '.join(link(u,n) for n,u in items.items())
def project_keywords(p):
    if not p.get('keywords'): return ''
    tags=''.join(f'<li>{esc(k)}</li>' for k in p['keywords'])
    return f'<ul class="keywords" aria-label="Project keywords">{tags}</ul>'
def project_figure(p,prefix=''):
    f=p.get('figure')
    if not f: return ''
    path=prefix+f['path']
    # Frame the paper figure without altering the source pixels; whitespace only.
    return f'''<figure class="project-figure">
<a class="figure-link" href="{esc(path)}" target="_blank" rel="noopener" aria-label="Open {esc(p['name'])} Figure {f['number']} at full resolution">
<svg viewBox="{esc(f['viewbox'])}" role="img" aria-label="{esc(f['alt'])}" xmlns="http://www.w3.org/2000/svg">
<image href="{esc(path)}" width="{f['width']}" height="{f['height']}" />
</svg></a>
<figcaption>{esc(f['caption'])} <a href="{esc(path)}" target="_blank" rel="noopener">View full figure ↗</a></figcaption>
</figure>'''
def highlighted_project(p):
    return f'''<article class="highlighted-project" id="highlight-{esc(p['id'])}">
<h3>{link(p['links']['Paper'],p['name'])}</h3>
<p class="project-subtitle">{esc(p['subtitle'])}</p>
<p class="project-description">{esc(p['text'])}</p>
{project_keywords(p)}
{project_figure(p)}
<p class="paper-links">{links(p['links'])}</p>
</article>'''
def paper(p):
    authors=[]
    for a in p['authors']:
        s=esc(a)+('*' if a in p.get('equal_contribution',[]) else '')
        authors.append(f'<strong>{s}</strong>' if a==profile['name'] else s)
    url=p['links'].get('Paper') or p['links'].get('arXiv') or p['links'].get('PDF')
    title=link(url,p['title']) if url else esc(p['title'])
    resources=f'<p class="paper-links">{links(p["links"])}</p>' if p['links'] else ''
    return f'<li class="paper" id="paper-{esc(p["id"])}"><h3>{title}</h3><p class="authors">{", ".join(authors)}</p><p class="venue">{esc(p["venue"])}</p>{resources}</li>'
def render(route,title,content):
    prefix='../' if route else ''
    nav=[]
    for slug,label in [('', 'Home'),('publications','Publications'),('projects','Projects'),('cv','CV')]:
        href=prefix+(slug+'/' if slug else './')
        active=' aria-current="page"' if slug==route else ''
        nav.append(f'<a href="{href}"{active}>{label}</a>')
    tag='h1' if not route else 'p'
    page_title=f'{title} | {profile["name"]}' if route else f'{profile["name"]} · {profile["chinese_name"]}'
    description=profile['description'] if not route else f'{title} of Mingyue Huo, PhD candidate at UIUC working on speech and multimodal AI.'
    canonical='https://mingyue66.github.io/'+(route+'/' if route else '')
    updated=date.fromisoformat(profile['updated']).strftime('%B %-d, %Y')
    html=f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>{esc(page_title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{esc(page_title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{canonical}">
  <link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}stylesheet.css?v={style_version}">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="site">
    <header class="site-header">
      <{tag} class="site-name"><a href="{prefix}./">Mingyue Huo <span lang="zh">霍明月</span></a></{tag}>
      <nav aria-label="Main navigation">{' '.join(nav)}</nav>
    </header>
    <main id="main">
{content}
    </main>
    <footer class="site-footer">
      <span>Last updated: <time datetime="{profile['updated']}">{updated}</time></span>
      <a href="mailto:{profile['email']}">Get in touch</a>
    </footer>
  </div>
</body>
</html>
'''
    dest=ROOT/route/'index.html'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(html)
def home():
    bio='\n'.join(f'<p>{esc(p)}</p>' for p in profile['bio'])
    interests=''.join(f'<li>{esc(p)}</li>' for p in profile['interests'])
    highlights=''.join(highlighted_project(next(p for p in profile['projects'] if p['id']==id)) for id in profile['highlights'])
    contacts=links({'Google Scholar':profile['scholar'],'GitHub':profile['github'],'LinkedIn':profile['linkedin'],profile['email']:'mailto:'+profile['email']})
    return f'''<section class="intro" aria-label="About Mingyue">
<img class="portrait" src="assets/portrait.jpg" width="164" height="198" alt="Mingyue Huo by the waterfront" fetchpriority="high">
{bio}
<p class="availability">{esc(profile['availability'])} {link('mailto:'+profile['email'],'Please get in touch.')}</p>
<p class="contact-links">{contacts}</p>
</section>
<section class="section" aria-labelledby="research-title"><h2 id="research-title">Research Interests</h2><ul class="plain-list">{interests}</ul></section>
<section class="section" aria-labelledby="news-title"><h2 id="news-title">Recent News</h2>
<ul class="news-list">
<li><time datetime="2026-09">Sep 2026</time><span>New preprints from my Netflix internship: {link('https://arxiv.org/abs/2609.34582','SpeechCritic')} and {link('https://arxiv.org/abs/2609.36979','Louder, Longer, Livelier')} on human-aligned speech evaluation.</span></li>
<li><time datetime="2026-09">Sep 2026</time><span>Received the {link('https://linguistics.illinois.edu/news/2026-09-01/congratulations-grad-student-award-and-grant-recipients','UIUC Graduate College Dissertation Completion Fellowship')} for 2026–2027.</span></li>
<li><time datetime="2026-07">Jul 2026</time><span>{link('https://aclanthology.org/2026.acl-long.1938/','TagSpeech')} presented as a main-conference oral at ACL 2026.</span></li>
</ul></section>
<section class="section" aria-labelledby="highlights-title"><div class="section-heading"><h2 id="highlights-title">Highlighted Projects</h2>{link('projects/','All projects →')}</div>{highlights}</section>'''
def publications():
    years=sorted({p['year'] for p in papers},reverse=True)
    groups=''.join(f'<section class="publication-year" aria-labelledby="year-{y}"><h2 id="year-{y}">{y}</h2><ul class="paper-list">'+''.join(paper(p) for p in papers if p['year']==y)+'</ul></section>' for y in years)
    return f'''<h1>Publications</h1><p class="page-intro">Papers, preprints, and manuscripts, grouped by publication year. My name is bolded; * indicates equal contribution. See {link(profile['scholar'],'Google Scholar')}.</p>
<nav class="year-nav" aria-label="Publication years">{' '.join(link('#year-'+str(y),str(y)) for y in years)}</nav>{groups}'''
def projects():
    items=''.join(f'<article class="project" id="{esc(p["id"])}"><h2>{esc(p["name"])}</h2><p class="project-subtitle">{esc(p["subtitle"])}</p><p>{esc(p["text"])}</p>{project_keywords(p)}{project_figure(p,"../")}<p class="paper-links">{links(p["links"])}</p></article>' for p in profile['projects'])
    return '<h1>Projects</h1><p class="page-intro">Research systems, open-source work, and demos for speech and audio understanding.</p>'+items
def cv():
    cv_version=hashlib.sha256((ROOT/profile['cv']).read_bytes()).hexdigest()[:10]
    cv_url='../'+profile['cv']+'?v='+cv_version
    edu=''.join(f'<li><div><strong>{esc(p["degree"])}</strong><p>{esc(p["school"])}</p></div><span class="date">{esc(p["date"])}</span></li>' for p in profile['education'])
    exp=''.join(f'<li><div><strong>{esc(p["company"])}</strong><p>{esc(p["role"])}</p><p class="muted">{esc(p["text"])}</p></div><span class="date">{esc(p["date"])}</span></li>' for p in profile['experience'])
    awards=''.join(f'<li><div>{esc(p["name"])}</div><span class="date">{esc(p["date"])}</span></li>' for p in profile['awards'])
    service=''.join(f'<li>{esc(p)}</li>' for p in profile['service'])
    return f'''<h1>Curriculum Vitae</h1><p class="page-intro">A short overview of my education, research experience, and service.</p>
<p>{link(cv_url,'Download CV (PDF) ↓')} <span class="muted">· {esc(profile['cv_updated'])}</span></p>
<section class="section"><h2>Education</h2><ul class="record-list">{edu}</ul></section>
<section class="section"><h2>Industry Research</h2><ul class="record-list">{exp}</ul></section>
<section class="section"><h2>Selected Awards</h2><ul class="record-list awards">{awards}</ul></section>
<section class="section"><h2>Community Service</h2><ul class="plain-list">{service}</ul></section>'''
if __name__=='__main__':
    assert len({p['id'] for p in papers})==len(papers),'Duplicate publication IDs'
    assert all(profile['name'] in p['authors'] for p in papers),'Unexpected author'
    render('','Home',home())
    render('publications','Publications',publications())
    render('projects','Projects',projects())
    render('cv','CV',cv())
    print(f'Rendered four static pages and {len(papers)} publications.')
