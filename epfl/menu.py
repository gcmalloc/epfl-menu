#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <gcmalloc@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return gcmalloc.
# ----------------------------------------------------------------------------
#

import sys
      

import urllib
from BeautifulSoup import BeautifulSoup

URL='http://menus.epfl.ch/cgi-bin/rssMenus'

def get():
    con = urllib.urlopen(URL)

    raw_html = con.read()
    
    soup = BeautifulSoup(raw_html)
    restaurant = dict()
    for i in soup.findAll('item'):
        title = i.find('title').string.split(":")
        rest_name = title[0].strip()
        plate_name = title[1].strip()
        if not restaurant.has_key(rest_name):
            restaurant[rest_name] = dict()
        raw_menu_description = i.find('description').string
        #clean every line, and strip them
        menu_description = [line.strip() for line in raw_menu_description.split("\n")]
        #filter the description to remove empty lines
        restaurant[rest_name][plate_name] = filter(lambda a: a, menu_description)

    return restaurant
