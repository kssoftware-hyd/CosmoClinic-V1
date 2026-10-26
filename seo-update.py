#!/usr/bin/env python3
"""Cosmo International Clinic - Advanced SEO (v2). Run from the site root:  python3 seo-update.py
Rebuilds on every page: title, meta description + keywords, OG/Twitter, canonical, hreflang, preconnect,
JSON-LD (clinic, website, breadcrumbs, FAQ, blog, service), alt-text clean-up, blog internal links,
plus sitemap.xml, robots.txt. Safe to re-run."""
import re, json, pathlib, html
D = 'https://www.cosmoclinic.com'
TODAY = '2026-10-26'
SUF = ' | Cosmo International Clinic'
# page: (title <=60 chars, description <=155 chars, keywords, schema name)
P = {
 'index.html': ('Hair Transplant in Hyderabad | Cosmo International Clinic',
  'Hair transplant, beard transplant and skin treatments in Banjara Hills, Hyderabad. Free consultation at Cosmo International Clinic. Call +91 9246119111.',
  'hair transplant in Hyderabad, hair transplant clinic Hyderabad, direct hair transplant Hyderabad, hair transplant Banjara Hills, beard transplant Hyderabad, women hair transplant Hyderabad, skin clinic Hyderabad','Home'),
 'about.html': ('About Cosmo International Clinic | Hyderabad',
  'Cosmo International Clinic is a hair transplant and skin treatment centre in Banjara Hills, Hyderabad. Learn about our consultation-first approach to care.',
  'about Cosmo International Clinic, hair clinic Banjara Hills, skin clinic Hyderabad, Cosmo Netherlands','About Us'),
 'treatments.html': ('Hair & Skin Treatments in Hyderabad | Cosmo Clinic',
  'Hair transplant, hair loss, skin rejuvenation, fat loss, face lifting, acne and scar treatments in Hyderabad. Book a consultation at Cosmo Clinic.',
  'hair and skin treatments Hyderabad, hair transplant Hyderabad, skin rejuvenation Hyderabad, fat loss treatment Hyderabad, acne treatment Hyderabad','Treatments'),
 'patient-results.html': ('Hair Transplant Results Hyderabad | Cosmo Clinic',
  'See patient hair transplant results from Cosmo International Clinic, Hyderabad. Results vary between individuals and are not guaranteed.',
  'hair transplant results Hyderabad, hair transplant before and after, DHT results India','Patient Results'),
 'gallery.html': ('Clinic Gallery | Cosmo International Clinic Hyderabad',
  'Photos of Cosmo International Clinic in Banjara Hills, Hyderabad, plus simple illustrations explaining how a hair transplant works.',
  'Cosmo clinic gallery, hair transplant clinic photos Hyderabad, hair clinic Banjara Hills','Gallery'),
 'testimonials.html': ('Patient Testimonials | Cosmo Clinic Hyderabad',
  'Watch patient video testimonials from Cosmo International Clinic, a hair transplant and skin clinic in Hyderabad.',
  'hair transplant reviews Hyderabad, Cosmo clinic reviews, patient testimonials hair transplant','Testimonials'),
 'contact.html': ('Contact & Book Consultation | Cosmo Clinic Hyderabad',
  'Call +91 9246119111, WhatsApp or send an enquiry. Maheshwari Towers, Road No. 1, Banjara Hills, Hyderabad 500034. Open daily 11 AM to 7 PM.',
  'Cosmo clinic contact, hair transplant consultation Hyderabad, book hair transplant consultation, hair clinic Banjara Hills address','Contact Us'),
 'blogs.html': ('Hair Transplant & Hair Loss Blog | Cosmo Clinic',
  'Plain-language articles on hair transplant, hair loss treatments and skin care from Cosmo International Clinic, Hyderabad.',
  'hair transplant blog, hair loss treatment guide, when to get a hair transplant, hair transplant recovery timeline','Blogs'),
 'treatments/direct-hair-transplant.html': ('Direct Hair Transplant in Hyderabad | Cosmo Clinic',
  'Direct hair transplant (DHT) in Hyderabad: follicles are implanted one by one for a natural-looking hairline. Book a consultation at Cosmo International Clinic.',
  'direct hair transplant Hyderabad, DHT hair transplant, DHI hair transplant Hyderabad, hair transplant cost Hyderabad, hair transplant Banjara Hills','Direct Hair Transplant'),
 'treatments/hair-loss-treatment.html': ('Hair Loss Treatment in Hyderabad | Cosmo Clinic',
  'Hair loss treatment in Hyderabad: medicines, laser therapy, PRP and transplant options explained after a personal consultation at Cosmo International Clinic.',
  'hair loss treatment Hyderabad, PRP hair treatment Hyderabad, hair fall treatment Hyderabad, hair thinning treatment','Hair Loss Treatments'),
 'treatments/skin-rejuvenation.html': ('Skin Rejuvenation in Hyderabad | Cosmo Clinic',
  'Skin rejuvenation treatments in Hyderabad to improve skin texture, tone and appearance, planned after assessment at Cosmo International Clinic.',
  'skin rejuvenation Hyderabad, skin clinic Banjara Hills, skin treatment Hyderabad, glowing skin treatment','Skin Rejuvenation'),
 'treatments/fat-loss.html': ('Fat Loss Treatment in Hyderabad | Cosmo Clinic',
  'Clinic-guided fat loss treatment options in Hyderabad for stubborn areas, discussed after assessment at Cosmo International Clinic.',
  'fat loss treatment Hyderabad, body contouring Hyderabad, fat reduction treatment, stubborn fat treatment','Fat Loss Treatments'),
 'treatments/face-lifting.html': ('Non-Surgical Face Lifting in Hyderabad | Cosmo Clinic',
  'Non-surgical face lifting in Hyderabad: RF, HIFU, fillers, Botox and thread lift options, planned individually at Cosmo International Clinic.',
  'face lifting Hyderabad, non surgical face lift Hyderabad, HIFU Hyderabad, anti ageing treatment Hyderabad, thread lift Hyderabad','Face Lifting'),
 'treatments/hair-removal-scar.html': ('Hair Removal & Scar Treatment in Hyderabad | Cosmo',
  'Laser hair reduction and scar repair options in Hyderabad, planned after skin assessment at Cosmo International Clinic, Banjara Hills.',
  'laser hair removal Hyderabad, scar treatment Hyderabad, scar removal Hyderabad, micro-needling Hyderabad, acne scar treatment','Hair Removal and Scar'),
 'treatments/acne-treatment.html': ('Acne Treatment in Hyderabad | Cosmo International Clinic',
  'Acne treatment in Hyderabad: skin assessment and a personal plan to manage acne and marks at Cosmo International Clinic, Banjara Hills.',
  'acne treatment Hyderabad, pimple treatment Hyderabad, acne scar treatment Hyderabad, skin clinic Banjara Hills','Acne Treatment'),
 'treatments/color-improvement.html': ('Skin Color Improvement in Hyderabad | Cosmo Clinic',
  'Skin color improvement in Hyderabad: carbon facial, peels, Glutathione and microdermabrasion for pigmentation and tan at Cosmo Clinic.',
  'skin pigmentation treatment Hyderabad, skin color improvement Hyderabad, carbon facial Hyderabad, dark spots treatment, glutathione Hyderabad','Color Improvement'),
}
CLINIC = {"@context":"https://schema.org","@type":["MedicalClinic","LocalBusiness"],"@id":D+"/#clinic","name":"Cosmo International Clinic",
 "alternateName":"Cosmo Clinic Hyderabad","url":D+"/","logo":D+"/images/logo.png","image":D+"/images/logo.png","telephone":"+919246119111","email":"cosmodr55@gmail.com",
 "description":"Hair transplant and skin treatment clinic in Banjara Hills, Hyderabad.",
 "address":{"@type":"PostalAddress","streetAddress":"201 A, 2nd Floor, Maheshwari Towers, 3rd Lane from Karachi Bakery, near Care Hospital, Road No. 1, Banjara Hills","addressLocality":"Hyderabad","addressRegion":"Telangana","postalCode":"500034","addressCountry":"IN"},
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"11:00","closes":"19:00"}],
 "areaServed":[{"@type":"City","name":"Hyderabad"},{"@type":"AdministrativeArea","name":"Telangana"}],
 "availableService":[{"@type":"MedicalProcedure","name":n} for n in ["Direct Hair Transplant","Beard Transplant","Women Hair Transplant","Hair Loss Treatment","Skin Rejuvenation","Fat Loss Treatment","Face Lifting","Hair Removal and Scar Treatment","Acne Treatment","Skin Color Improvement"]],
 "sameAs":["https://www.instagram.com/cosmoclinicin","https://www.youtube.com/@cosmoclinicin","https://www.facebook.com/people/Cosmoclinicin/61570549773908/"]}
REL = {  # blog id -> (text, link)
 'when-to-get-a-hair-transplant':('Learn about','treatments/direct-hair-transplant.html','direct hair transplant in Hyderabad'),
 'how-direct-hair-transplant-works':('Read more about','treatments/direct-hair-transplant.html','direct hair transplant in Hyderabad'),
 'what-to-expect-after-a-hair-transplant':('See real','patient-results.html','hair transplant patient results'),
 'choosing-a-hair-transplant-clinic-in-hyderabad':('Visit','contact.html','Cosmo International Clinic in Banjara Hills to book a consultation'),
 'hair-loss-treatments-beyond-surgery':('Learn about','treatments/hair-loss-treatment.html','hair loss treatment in Hyderabad')}
def ld(o): return '<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False,separators=(',',':'))+'</script>'
def txt(s): return html.unescape(re.sub(r'<[^>]+>',' ',s)).replace('\u2019',"'").strip()
def esc(s): return html.escape(s,quote=True)
def seo(t, rel):
    page = rel.split('/')[-1]; url = D + '/' + rel; deep = '/' in rel; pre = '../' if deep else ''
    t = re.sub(r'https://(?:www\.)?cosmoclinic\.com', D, t)
    meta = P.get(rel)
    if meta:
        ti, de, kw, nm = meta
        t = re.sub(r'<title>.*?</title>', '<title>%s</title>' % html.escape(ti,quote=False), t, 1, re.S)
        for pat, val in (('name="description"', de), ('property="og:title"', ti), ('property="og:description"', de)):
            t = re.sub(r'(<meta %s content=").*?(">)' % pat, lambda m: m.group(1)+esc(val)+m.group(2), t, 1)
        t = re.sub(r'<meta name="keywords" content="[^"]*">', '', t)
        t = t.replace('<meta name="description"', '<meta name="keywords" content="%s"><meta name="description"' % esc(kw), 1)
        t = re.sub(r'<meta name="twitter:title" content="[^"]*">', '', t)
        t = re.sub(r'<meta name="twitter:description" content="[^"]*">', '', t)
        t = t.replace('<meta name="twitter:card" content="summary">', '<meta name="twitter:card" content="summary"><meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s">' % (esc(ti), esc(de)), 1)
    t = re.sub(r'(<link rel="canonical" href=")[^"]*(">)', lambda m: m.group(1)+url+m.group(2), t, 1)
    t = re.sub(r'(<meta property="og:url" content=")[^"]*(">)', lambda m: m.group(1)+url+m.group(2), t, 1)
    t = t.replace('max-image-preview:large">', 'max-image-preview:large,max-snippet:-1,max-video-preview:-1">')
    if 'twitter:card' not in t:
        extra = ('<meta name="robots" content="%s"><meta property="og:site_name" content="Cosmo International Clinic"><meta property="og:locale" content="en_IN">'
                 '<meta property="og:image" content="%s/images/logo.png"><meta name="twitter:card" content="summary"><meta name="geo.region" content="IN-TG"><meta name="geo.placename" content="Hyderabad">') % (
                 'noindex,follow' if page=='404.html' else 'index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1', D)
        if page != '404.html': extra += '<link rel="alternate" hreflang="en-IN" href="%s"><link rel="alternate" hreflang="x-default" href="%s">' % (url,url)
        t = t.replace('<meta name="theme-color"', extra + '<meta name="theme-color"', 1)
    if 'rel="preconnect"' not in t:
        t = t.replace('<link href="https://fonts.googleapis.com/css2', '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2', 1)
    # ---- JSON-LD rebuilt each run
    t = re.sub(r'<script type="application/ld\+json">.*?</script>', '', t, flags=re.S)
    if page != '404.html':
        blocks = []
        if rel in ('index.html','about.html','contact.html'): blocks.append(CLINIC)
        if rel == 'index.html': blocks.append({"@context":"https://schema.org","@type":"WebSite","@id":D+"/#website","url":D+"/","name":"Cosmo International Clinic","inLanguage":"en-IN","publisher":{"@id":D+"/#clinic"}})
        if rel != 'index.html':
            nm = meta[3] if meta else (txt(re.search(r'<h1>(.*?)</h1>', t, re.S).group(1)) if re.search(r'<h1>(.*?)</h1>', t, re.S) else page)
            items = [{"@type":"ListItem","position":1,"name":"Home","item":D+"/index.html"}]
            if deep: items += [{"@type":"ListItem","position":2,"name":"Treatments","item":D+"/treatments.html"},{"@type":"ListItem","position":3,"name":nm,"item":url}]
            else: items.append({"@type":"ListItem","position":2,"name":nm,"item":url})
            blocks.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items})
        if deep and meta:
            blocks.append({"@context":"https://schema.org","@type":"Service","serviceType":meta[3],"name":meta[3]+" in Hyderabad","url":url,"description":meta[1],
                           "areaServed":{"@type":"City","name":"Hyderabad"},"provider":{"@type":["MedicalClinic","LocalBusiness"],"name":"Cosmo International Clinic","url":D+"/","telephone":"+919246119111","image":D+"/images/logo.png","address":CLINIC["address"]}})
        if rel == 'index.html':
            faq = [(txt(q),txt(a)) for q,a in re.findall(r'<details><summary>(.*?)</summary>(.*?)</details>', t, re.S)]
            if faq: blocks.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
        if rel == 'blogs.html':
            arts = re.findall(r'<section class="sec(?: alt)? blog-post" id="([^"]+)"><div class="wrap"><p class="blog-meta">.*?</p><h2>(.*?)</h2>', t)
            blocks.append({"@context":"https://schema.org","@type":"Blog","name":"Cosmo International Clinic Blog","url":url,"inLanguage":"en-IN","blogPost":[
              {"@type":"BlogPosting","headline":txt(h),"url":url+"#"+i,"datePublished":TODAY,"dateModified":TODAY,"image":D+"/images/logo.png","inLanguage":"en-IN","author":{"@type":"Organization","name":"Cosmo International Clinic"},"publisher":{"@type":"Organization","name":"Cosmo International Clinic","logo":{"@type":"ImageObject","url":D+"/images/logo.png"}},"mainEntityOfPage":url+"#"+i} for i,h in arts]})
        t = t.replace('</head>', ''.join(ld(b) for b in blocks)+'</head>', 1)
    # ---- alt text clean-up
    t = t.replace('alt="Sample clinic or doctor image"', 'alt="Before and after hair transplant at Cosmo International Clinic, Hyderabad"')
    t = t.replace('alt="Hair transplant before"', 'alt="Hair transplant patient before treatment, Cosmo International Clinic Hyderabad"').replace('alt="Hair transplant after"', 'alt="Hair transplant patient after treatment, Cosmo International Clinic Hyderabad"')
    t = re.sub(r'alt="([^"]*?) \(sample image\)"', r'alt="\1 at Cosmo International Clinic, Hyderabad"', t)
    t = re.sub(r'alt="([^"]*?) sample image"', r'alt="\1 in Hyderabad"', t)
    # ---- blog internal links
    if rel == 'blogs.html' and 'class="rel-link"' not in t:
        for bid,(lead,href,label) in REL.items():
            t = re.sub(r'(id="%s">.*?)(<p><a class="link" href="#main">Back to top</a></p>)' % re.escape(bid),
                       lambda m: m.group(1)+'<p class="rel-link">%s <a class="link" href="%s">%s</a>.</p>' % (lead, href, label)+m.group(2), t, 1, re.S)
    return t
root = pathlib.Path('.')
files = list(root.glob('*.html')) + list(root.glob('treatments/*.html'))
for f in files:
    s = f.read_text(encoding='utf-8'); n = seo(s, f.as_posix())
    if n != s: f.write_text(n, encoding='utf-8'); print('seo', f)
rels = ['index.html','treatments.html','patient-results.html','about.html','gallery.html','testimonials.html','blogs.html','contact.html']
tr = sorted(f.as_posix() for f in root.glob('treatments/*.html')) or []
for k in P:
    if k.startswith('treatments/') and k not in tr: tr.append(k)
pr = {'index.html':'1.0','treatments.html':'0.9','contact.html':'0.9','blogs.html':'0.7'}
rels += sorted(set(tr))
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
   '<url><loc>%s/%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>\n' % (D,u,TODAY,'weekly' if u in ('index.html','blogs.html') else 'monthly',pr.get(u,'0.8' if u.startswith('treatments/') else '0.6')) for u in rels) + '</urlset>\n'
pathlib.Path('sitemap.xml').write_text(sm)
pathlib.Path('robots.txt').write_text('User-agent: *\nAllow: /\nDisallow: /404.html\nSitemap: %s/sitemap.xml\n' % D)
