"""Placement Notifier for Linux and android/ios"""

import feedparser
import notify2
import time
import os
import urllib
import base64

MOBILE_NOTIFICATION = True

if MOBILE_NOTIFICATION:
    from notify_run import Notify


def Parsefeed():

    ICON_PATH = os.getcwd() + "/64x64.png"
    url = "placements.iitb.ac.in"

    if MOBILE_NOTIFICATION:
        notify = Notify()

    #ldap ID
    auth_user = ""

    #ldap Password
    auth_passwd = ""

    #Securing your HTTP request

    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, auth_user, auth_passwd)
    authhandler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(authhandler)
    urllib.request.install_opener(opener)
    notify2.init('Placement Blog Notify')
    old =None

    while(1):
        response = urllib.request.urlopen("http://placements.iitb.ac.in/blog/?feed=rss2").read()
        f = feedparser.parse(response)

        new = f['items'][0]['title'].encode('utf-8')
        if new != old:
            n = notify2.Notification(f['items'][0]['title'].encode('utf-8'),
                                     f['items'][0]['summary'].encode('utf-8'),
                                     icon=ICON_PATH
                                     )

            n.set_urgency(notify2.URGENCY_NORMAL)
            n.show()

            if MOBILE_NOTIFICATION:
                notify.send(new)

            old = new
            n.set_timeout(15000)
        time.sleep(3000)



if __name__ == '__main__':
    try:
        Parsefeed()
    except:
        print("Error")
