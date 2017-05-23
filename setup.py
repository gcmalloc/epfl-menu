from setuptools import setup
setup(name='epfl-menu',
      version = '0.2',
      description = 'Retrieve EPFL menus of the day',
      author = 'gcmalloc',
      url = 'http://github.com/gcmalloc/epfl-menu',
      py_modules = ['epfl.menu'],
      install_requires=['bs4'],
      scripts = ['bin/menu'])
