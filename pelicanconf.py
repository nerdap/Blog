#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Apoorv Upreti'
SITENAME = u"Apoorv's Blog"
SITEURL = ''

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

THEME = r'./pelican-svbtle'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()#(('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/nerdap/'),
          ('github', 'http://github.com/nerdap/'),
	  ('linkedin', 'http://in.linkedin.com/in/apoorvupreti/'),
)

DEFAULT_PAGINATION = 4

FILES_TO_COPY = (('extra/CNAME', 'CNAME'), )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
