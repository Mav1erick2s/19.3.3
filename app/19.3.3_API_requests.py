import requests

# GET
url = "https://petstore.swagger.io/v2/pet/findByStatus"
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
params = {'status': 'available'}

res = requests.get(url, headers=headers, params=params)

print("Получаем статус код", res.status_code)
print(res.json())


# POST
url = "https://petstore.swagger.io/v2/pet"
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data_pet = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "Polly"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "Jey"
        }
    ],
    "status": "available"
}

res_pet = requests.post(url, headers=headers, json=data_pet)

print("Добавление нового питомца, статус код", res_pet.status_code)
print(res_pet.json())


# POST
url = "https://petstore.swagger.io/v2/user"
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data_user = {
    "id": 0,
    "username": "Tom",
    "firstName": "Dave",
    "lastName": "Moriarty",
    "email": "tommory@gmail.com",
    "password": "tomcrut32%7",
    "phone": "89607839876",
    "userStatus": 0
}

res_user = requests.post(url, headers=headers, json=data_user)

print("Добавление нового пользователя, статус код", res_user.status_code)
print(res_user.json())


# PUT
url = "https://petstore.swagger.io/v2/user/Tom"
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data_change = {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}

res_change = requests.put(url, headers=headers, json=data_change)

print('Изменяем данные пользователя, статус код', res_change.status_code)
print(res_change.json())


# DELETE
url = 'https://petstore.swagger.io/v2/user/Tom'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

res_user = requests.delete(url, headers=headers)

print("Удаляем пользователя, статус код", res_user.status_code)
print(res_user.json())
