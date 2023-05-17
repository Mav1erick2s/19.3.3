import requests

# res = requests.get("https://petfriends.skillfactory.ru/apidocs/#/default/get_api_pets", headers=headers, params=params)
# print (res.text)

status = 'available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
                   headers={'accept': 'application/json'})

print(res.text)
print ("test")