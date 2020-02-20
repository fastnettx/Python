import requests
try:
    param = {'key1': 'value1'}
    getRequest = requests.get('https://reqres.in/api/users',  params=param)
    object=getRequest.json()
    list = object['data']
    for key in list:
        print (key['email'])
except Exception as e:
    print(e)


