"""Placement Notifier for android/ios"""
"""
pip install notify-run
notify-run register
notify-run configure https://notify.run/[channel name]

check out https://notify.run/

"""


import feedparser
import time
import os
import urllib
from notify_run import Notify


def Parsefeed():

    url = "placements.iitb.ac.in"

    notify = Notify()

    # ldap ID
    auth_user = ""

    # ldap Password
    auth_passwd = ""

    # Securing your HTTP request

    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, auth_user, auth_passwd)
    authhandler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(authhandler)
    urllib.request.install_opener(opener)
    old = None

    while(1):
        response = urllib.request.urlopen("http://placements.iitb.ac.in/blog/?feed=rss2").read()
        f = feedparser.parse(response)

        new = f['items'][0]['title'].encode('utf-8')
        if new != old:
            notify.send(new)
            old = new
        time.sleep(3000)


if __name__ == '__main__':
    try:
        Parsefeed()
    except:
        print("Error")
