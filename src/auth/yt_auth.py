from ytmusicapi import YTMusic

def authenticate():
    ytm = YTMusic('src/auth/browser.json')
    return ytm

