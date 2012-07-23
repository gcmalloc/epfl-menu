from setuptools import setup
setup(name='epfl-menu',
      version = '0.1',
      description = 'File checksumming utility',
      author = 'gcmalloc',
      url = 'http://github.com/gcmalloc/epfl-menu',
      py_modules = ['epfl.menu'],
      install_requires=['BeautifulSoup'],
      scripts = ['bin/menu'])                                                                                             
