#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <gcmalloc@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return gcmalloc.
# ----------------------------------------------------------------------------
#
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

LUNCH_URL='http://menus.epfl.ch/cgi-bin/rssMenus'
SUPPER_URL='http://menus.epfl.ch/cgi-bin/rssMenus?midisoir=soir'

def get(supper=False):
    if supper:
        url = SUPPER_URL
    else:
        url = LUNCH_URL
    con = urllib.request.urlopen(url)

    raw_html = con.read()

    soup = BeautifulSoup(raw_html, "html.parser")
    restaurant = dict()
    for i in soup.find_all('item'):
        title = i.find('title').string.split(":")
        rest_name = title[0].strip()
        plate_name = title[1].strip()
        if rest_name not in restaurant:
            restaurant[rest_name] = dict()
        raw_menu_description = i.find('description').string
        #clean every line, and strip them
        menu_description = [line.strip() for line in raw_menu_description.split("\n")]
        #filter the description to remove empty lines
        restaurant[rest_name][plate_name] = [a for a in menu_description if a]

    return restaurant
