#!/usr/bin/env python
# coding=utf8

import re
import subprocess
import urllib2


matches = []

feed_url = 'https://www.archlinux.org/feeds/release/'

feed = urllib2.urlopen("https://www.archlinux.org/feeds/releases/").read()

pattern = r"(20\d{2}\.[01-12]{2}\.[01-]{2})"

regex = re.compile(pattern, re.IGNORECASE)

for match in regex.finditer(feed):
        matches.append(match.group(1))

current_version = (matches[0])
last_version = (matches[5])

with open('template.json', 'r+') as f:
    content = f.read()
    f.seek(0)
    f.truncate()
    f.write(content.replace(last_version, current_version))

subprocess.Popen(["git", "add", "template.json"])
subprocess.Popen(["git", "commit", "-m", "\"update .iso URL\""])
subprocess.Popen(["git", "push"])
