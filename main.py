from ipdata import ipdata
from pprint import pprint

ipdata = ipdata.IPData('6459aaacc7de0f4c43c17291be71c1d593c49dc017c5fa4f1db58e0e') #Create Account Free In IPDATA Site.
response = ipdata.lookup('151.250.250.17') #ip Target
pprint(response)