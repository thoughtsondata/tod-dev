AUTHOR = 'Ivey'
SITENAME = 'Thoughts on Data'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Index", "/index.html"),
            ("About", "/about.html"),
        ('Mailing List', 'https://docs.google.com/forms/d/e/1FAIpQLSdpjM_LVVvRCKhuFiYqemRuycfRChsM-Pr3nIho5mDO7c9qOw/viewform?usp=sf_link'),)

DISPLAY_PAGES_ON_MENU = True

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/thoughtsondata'),
          ('Email', 'mailto:hello@thoughtsondata.dev'),)

DEFAULT_PAGINATION = 8
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
# OUTPUT_RETENTION = [".git"]

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = 50

ARCHIVES_URL = "archives.html"
ARCHIVES_SAVE_AS = 'archives.html'
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
TAGS_URL = 'tag/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True