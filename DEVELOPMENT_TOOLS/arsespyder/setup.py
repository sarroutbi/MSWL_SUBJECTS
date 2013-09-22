from setuptools import setup, find_packages
setup (name     = 'arsespyder',
       version  = '0.0.1',
       packages = find_packages(),
       scripts  = [''],
       install_requires = ['bs4', 'urllib2'],
       package_data = {},
       author   = "Sergio Arroutbi",
       author_email = "sarroutbi@yahoo.es",
       description = "Web Spider to retrieve links",
       license = "ISC (Internet Systems Consortium)",
       keywords = "Web, crawler, links",
       url = "https://github.com/sarroutbi/MSWL_SUBJECTS/tree/master/DEVELOPMENT_TOOLS/arsespyder",
       long_description = "",
       download_url = "http://sarroutbi.dyndns.org/DEVELOPMENT_TOOLS/arsespyder-0.0.1.tar.gz", )