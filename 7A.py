from html.parser import HTMLParser
import urllib.request
from ipaddress import ip_address, IPv4Address

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0

    def handle_starttag(self, tag, attrs):
        if tag!='body':
            return
        if self.recording:
            self.reording += 1
            return
        self.recording = 1

    def handle_endtag (self, tag):
        if tag == 'body' and self.recording:
            self.recording -= 1


    def handle_data (self, data):
        if not self.recording:
            return
        data_list = data.split()
        for d in data_list:
            ip_type = "Invalid"
            try:
                ip_type = "IPv4" if type(ip_address(d)) is IPv4Address else "IPv6"
            except ValueError:
                ip_type = "Invalid"
            if ip_type == "IPv4":
                print(d)

myparser = MyHTMLParser()
with urllib.request.urlopen ('http://checkip.dyndns.org/') as response:
    html = str(response.read())
myparser.feed(html)
