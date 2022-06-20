import urllib.request
import threading
import time
import requests



def url_checker(url):
    try:
        return urllib.request.urlopen(url).getcode()
    except urllib.error.URLError as e:
        return "No fue posible establecer conexion con el host " + str(e.reason)

