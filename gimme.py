import socket
import os
import mechanicalsoup

# Returns IPV4 address of site you type.
get = input("Website > ")
recv = socket.gethostbyname(get)
# Prints result
print ("[*] IP == " + recv)

# Create the browser object
browser = mechanicalsoup.StatefulBrowser()
visit = input("What sites Source code are we returning? EX: (https://www.URI.tld/anypath/) > ")
page = browser.open(visit)
page_code = browser.get_current_page()

# Print stuff
print (page_code)
print (browser)
print (page)



