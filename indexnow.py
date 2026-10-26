#!/usr/bin/env python3
"""Tell Bing / Yandex / other IndexNow search engines that pages changed (Google does not use IndexNow).
Upload a0d08729b4409901217f419b649a3faa.txt to the site root first, then run on your own computer:  python3 indexnow.py"""
import json, re, urllib.request
KEY = "a0d08729b4409901217f419b649a3faa"; HOST = "www.cosmoclinic.com"
urls = re.findall(r"<loc>(.*?)</loc>", open("sitemap.xml", encoding="utf-8").read())
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": "https://%s/%s.txt" % (HOST, KEY), "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", body, {"Content-Type": "application/json; charset=utf-8"})
print(len(urls), "URLs submitted, HTTP", urllib.request.urlopen(req).status)
