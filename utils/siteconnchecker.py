#import urllib to check connectivity checker for a website

import urllib.request as urllib

def main(url):
    response = urllib.urlopen(url)
    print(response.getcode())
    print("connected to ", url, " successfully !")

urltocheck = input("input the url of the site")
main(urltocheck)
