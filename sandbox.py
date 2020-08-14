#!/usr/bin/env python

# Copyright 2019-2020 iexcloud. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from decouple import config
import sys, os, base64, datetime, hashlib, hmac
import requests # pip install requests
from dotenv import load_dotenv
load_dotenv()

# ************* REQUEST VALUES *************
method = 'GET'
host = 'sandbox.iexapis.com'
host_0 = 'cloud.iexapis.com'


# API_USERNAME = config('USER')
a = os.getenv('IEX_PUBLIC_SANDBOX_KEY')
print(a)

access_key = os.environ.get('IEX_PUBLIC_SANDBOX_KEY')
print(access_key)
secret_key = os.environ.get('IEX_SECRET_SANDBOX_KEY')

canonical_querystring = 'token=' + access_key
canonical_uri = '/v1/stock/tsla/company'
endpoint = "https://" + host + canonical_uri


# ************* SEND THE REQUEST *************
request_url = endpoint + '?' + canonical_querystring

print('\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++')
print('Request URL = ' + request_url)
r = requests.get(request_url)

print('\nRESPONSE++++++++++++++++++++++++++++++++++++')
print('Response code: %d\n' % r.status_code)
print(r.text) 



def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).hexdigest()

def getSignatureKey(key, dateStamp):
    kDate = sign(key, dateStamp)
    return sign(kDate, 'iex_request')

if access_key is None or secret_key is None:
    print('No access key is available.')
    sys.exit()


"""
t = datetime.datetime.utcnow()
iexdate = t.strftime('%Y%m%dT%H%M%SZ')
datestamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope
canonical_headers = 'host:' + host + '\n' + 'x-iex-date:' + iexdate + '\n'
signed_headers = 'host;x-iex-date'
payload_hash = hashlib.sha256(('').encode('utf-8')).hexdigest()
canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash
algorithm = 'IEX-HMAC-SHA256'
credential_scope = datestamp + '/' + 'iex_request'
string_to_sign = algorithm + '\n' +  iexdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()
signing_key = getSignatureKey(secret_key, datestamp)
signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

headers = {'x-iex-date':iexdate, 'Authorization':authorization_header}
"""