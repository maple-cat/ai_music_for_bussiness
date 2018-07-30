import requests,json



url = 'http://stcazr-c56:8080/submit'


headers = {}


a= requests.post(url,params = {'wish':'你好'}).text
results = json.loads(a)
print(results)

for i in results:


    print(i['Ranking'])
