import requests

def submitClockIn(name):  
  url = 'https://docs.google.com/forms/d/e/1FAIpQLSfd8HNFwyf6TYJZiyRPIrSDW75PayniyJ3avgHP4XsDbW_XCw/formResponse'
  form_data = { 'entry.1199919450': name,
                'entry.46700222'  :'Clock-In',
                'draftResponse'   :[],
                'pageHistory'     :0}
  user_agent = {  'Referer'   :'https://docs.google.com/forms/d/e/1FAIpQLSfd8HNFwyf6TYJZiyRPIrSDW75PayniyJ3avgHP4XsDbW_XCw/viewform',
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
  requests.post(url, data=form_data, headers=user_agent)


def submitClockOut(name):
  url = 'https://docs.google.com/forms/d/e/1FAIpQLSfd8HNFwyf6TYJZiyRPIrSDW75PayniyJ3avgHP4XsDbW_XCw/formResponse'
  form_data = { 'entry.1199919450': name,
                'entry.46700222'  :'Clock-Out',
                'draftResponse'   :[],
                'pageHistory'     :0}
  user_agent = {  'Referer'   :'https://docs.google.com/forms/d/e/1FAIpQLSfd8HNFwyf6TYJZiyRPIrSDW75PayniyJ3avgHP4XsDbW_XCw/viewform',
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
  requests.post(url, data=form_data, headers=user_agent)

