#Credit http://stockrt.github.io/p/emulating-a-browser-in-python-with-mechanize/
import mechanize
import cookielib
import getpass

# Browser
br = mechanize.Browser()

#Uncomment if using local proxy 
#br.set_proxies({"https": "localhost:3128"})

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent 
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
r = br.open('https://sso.bris.ac.uk/sso/login')
html = r.read()
br.select_form(nr=0)

#Enter Credentials
user_input = raw_input("Username: ")
br['username'] = user_input
user_input = getpass.getpass("Password: ")
br['password'] = user_input
br.submit()

#Attempt to access a secure page
r = br.open('https://wwwa.fen.bris.ac.uk/COMS20600/')
html = r.read()
print html