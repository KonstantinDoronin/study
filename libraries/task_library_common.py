import requests #импортируем библиотеку request - осуществляет запросы к серверам
r = requests.get('http://example.com')#запрос на получение содержимого интернет страницы
#print(r.text)#вывод на экран

url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value'}#
r = requests.get(url, params=par)#передача параментров в запрос (url -адрес, куда обращаемся, params - cловарь из параментров)
#print(r.url)#сформированный url-адрес с учетом параметров get-запроса

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)#отправка сформированных cookies на сервер
#print(r.text)

print(r.cookies['example_cookie_name']) #использование cookies, полученных от сервера