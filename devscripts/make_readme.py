#!/usr/bin/env python3

# yt-dlp --help | make_readme.py
# This must be run in a console of correct width
import re
import sys

README_FILE = 'README.md'
helptext = sys.stdin.read()

if isinstance(helptext, bytes):
    helptext = helptext.decode('utf-8')

with open(README_FILE, encoding='utf-8') as f:
    oldreadme = f.read()

header = oldreadme[:oldreadme.index('## General Options:')]
footer = oldreadme[oldreadme.index('# CONFIGURATION'):]

options = helptext[helptext.index('  General Options:'):]
options = re.sub(r'(?m)^  (\w.+)$', r'## \1', options)
options = options + '\n'

with open(README_FILE, 'w', encoding='utf-8') as f:
    f.write(header)
    f.write(options)
    f.write(footer)
