import requests

url = 'https://defectdojo.hack.cloudnative.nttdatauk.cloud/api/v2/users/'
headers = {'content-type': 'application/json',
           'Authorization': 'Token 72c6287153f4595fd28fbf6cbcb01af08e70dad3'}
r = requests.get(url, headers=headers, verify=True) # set verify to False if ssl cert is self-signed

for key, value in r.__dict__.iteritems():
  print key
  print value
  print '------------------'
