# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:25:26 2016

@author: rayka95
"""

import requests
import sys

if len(sys.argv)>1:
    number = sys.argv[1]
else:
    number = "09033400110"
r = requests.post('https://api.zarinpal.com/rest/v3/oauth/checkUsername.json',json={"username": number})
name = r.json()['data']['full_name']
name.replace(" ","\\u0020")
print(name)
