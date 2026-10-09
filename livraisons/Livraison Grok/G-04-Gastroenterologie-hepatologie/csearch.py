import json,sys,urllib.request,urllib.parse
UA={'User-Agent':'MEDINA-G04/1.0'}
for q in sys.argv[1:]:
  u='https://commons.wikimedia.org/w/api.php?action=query&format=json&list=search&srnamespace=6&srlimit=12&srsearch='+urllib.parse.quote(q+' filetype:bitmap')
  r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA)))
  print('##',q); [print('  ',x['title']) for x in r['query']['search']]
