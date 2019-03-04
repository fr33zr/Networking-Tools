import socket
import os
import mechanicalsoup


get = input("Website > ")
recv = socket.gethostbyname(get)
print ("[*] IP == " + recv)

# Create the browser object
browser = mechanicalsoup.StatefulBrowser()
visit = input("What sites Source code are we returning?(https://www.URI.tld/path/")
page = browser.open(visit)
page_code = browser.get_current_page()

# Print stuff
print (page_code)
print (browser)
print (page)



