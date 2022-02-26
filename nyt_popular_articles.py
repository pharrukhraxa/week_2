import requests

url = "https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json"

querystring = {"api-key":"u5kUkSfDiGthjZWXORISByZSGLlrHpB5"}

headers = {
    'authorization': "Basic cGhhcnJ1a2hyYXhhOmdocF94dnlrQkdUeXQ0c3ZUdmE2WVYzaWo1YkJQQWVvd2YyczJ3ekY=",
    'cache-control': "no-cache",
    'postman-token': "b2857875-ad97-544b-b685-8c702638bfe3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)