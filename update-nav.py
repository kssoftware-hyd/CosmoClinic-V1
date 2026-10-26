#!/usr/bin/env python3
"""Patch every .html in this folder (and treatments/) : Gallery dropdown + Blogs link,
taller logo, custom.css and extras.js. Safe to run more than once.
Usage:  python3 update-nav.py            (run from the site root)"""
import re, sys, pathlib

def patch(t, current=None):
    m = re.search(r'href="((?:\.\./)?)css/style\.css"', t)
    p = m.group(1) if m else ''
    # footer: add Blogs after Testimonials
    if True:
        t = re.sub(r'(<a href="(?:\.\./)?testimonials\.html">Testimonials</a>)(<a href="(?:\.\./)?contact\.html">Contact Us</a>)',
                   lambda x: x.group(1) + '<a href="%sblogs.html">Blogs</a>' % p + x.group(2), t)
    # header: Gallery + Testimonials -> Gallery dropdown + Blogs
    def nav(x):
        act = x.group(2) or x.group(4)
        btn = ' class="ddbtn active"' if act else ' class="ddbtn"'
        blog = ' class="active"' if current == 'blogs.html' else ''
        return ('<div class="dd"><button%s aria-expanded="false" aria-haspopup="true">Gallery ▾</button><div class="ddmenu">'
                '<a href="%sgallery.html">Clinic Gallery</a><a href="%stestimonials.html">Testimonials</a></div></div>'
                '<a href="%sblogs.html"%s>Blogs</a>') % (btn, p, p, p, blog)
    t = re.sub(r'<a href="((?:\.\./)?)gallery\.html"( class="active")?>Gallery</a><a href="((?:\.\./)?)testimonials\.html"( class="active")?>Testimonials</a>(?=<a href="[^"]*contact\.html"[^>]*>Contact</a>)',
               lambda x: nav(type('M', (), {'group': lambda s, i: x.group(i)})()), t)
    t = t.replace('alt="Cosmo Clinic International logo" width="64" height="64"', 'alt="Cosmo Clinic International logo" width="92" height="92"')
    if 'css/custom.css' not in t:
        t = t.replace('</head>', '<link rel="stylesheet" href="%scss/custom.css"></head>' % p, 1)
    if 'js/extras.js' not in t:
        t = t.replace('</body>', '<script src="%sjs/extras.js" defer></script></body>' % p, 1)
    t = re.sub(r'<meta name="theme-color" content="#[0-9a-fA-F]{6}">', '<meta name="theme-color" content="#1a948b">', t)
    return t

if __name__ == '__main__':
    root = pathlib.Path('.')
    for f in list(root.glob('*.html')) + list(root.glob('treatments/*.html')):
        s = f.read_text(encoding='utf-8')
        n = patch(s, f.name)
        if n != s:
            f.write_text(n, encoding='utf-8'); print('patched', f)
