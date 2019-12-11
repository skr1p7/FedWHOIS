from bs4 import BeautifulSoup
import urlparse4 as urlparse 
import mechanize 

class colors:
    GREEN = '\033[92m'
    STOP = '\033[0m'

query = raw_input(colors.GREEN + "Enter your search query> " + colors.STOP)
url = "https://viewdns.info/reversewhois/?q="+query

mech =  mechanize.Browser()
mech.set_handle_equiv(False) 
mech.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
r = mech.open(url)



reader = BeautifulSoup(r.read(), "lxml")
reader = reader.find("table", attrs={'id':'null'})
reader = reader.find('table')

print("Domains owned by "+query+" are> ")
for text in reader.findAll('tr'):
    print(text.find('td').text)