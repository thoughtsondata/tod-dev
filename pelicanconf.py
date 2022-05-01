AUTHOR = 'Ivey'
SITENAME = 'Thoughts on Data'
SITEURL = 'tod.dev'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = "%b %d, %Y"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Index", "/index.html"),
            ("About", "https://www.tod.dev/pages/about.html"),
        ('Mailing List', 'https://form.tod.dev/'),)

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