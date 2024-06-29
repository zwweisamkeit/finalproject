import requests
import json
print("начало программы")
print()
response = requests.get("https://fakestoreapi.com/products/categories")
categories = response.json()
print("доступные категории товаров: ", categories)
print()
user_choise = str(input("выберите категорию, товары которой хотели бы увидеть: "))
print()
for i in categories:
    if user_choise == i:
        response = requests.get(f"https://fakestoreapi.com/products/category/{user_choise}")
        items = response.json()
        print(f"товары из категории {user_choise}:")
        for t in items:
            print('Артикул: ',t['id'])
            print('Название: ',t['title'])
            print('Цена: ',t['price'])
            print('Описание: ',t['description'])
            print('Категория: ',t['category'])
            print('Изображение: ',t['image'])
            print("------------------------------------------------------------------------------------------------")
        break
else:
    print("такой категории не существует") 
print()
print("конец программы")