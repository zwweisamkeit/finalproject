import requests
import json
print("начало программы")
print("===============================================")
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
        print("товары из выбранной вами категории:")
        for t in items:
            print(t)
            print()
        break
else:
    print("такой категории не существует")
print("===============================================")
print("конец программы")