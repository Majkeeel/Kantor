import requests
import json

gold = requests.get('http://api.nbp.pl/api/cenyzlota')
gold_price = gold.json()[0]['cena']
gold_data = gold.json()[0]['data']
currency = requests.get("http://api.nbp.pl/api/exchangerates/tables/a/?format=json")
# currency_price = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{f}/?format=json")

user_choice = -1

while user_choice != 4:
    if user_choice == 1:
        print("-"*55)
        print("Aktualna cena złota z dnia " + gold_data + " wynosi: " + str(gold_price) + "zł" )
        print("-"*55)
    if user_choice == 2:
        print("Aktualna cena walut z dnia " + currency.json()[0]['effectiveDate'])
        print()
        for i in range(0, 34):
            print("-"*42)
            print(currency.json()[0]['rates'][i]['code'] + " - " + currency.json()[0]['rates'][i]['currency'])
    if user_choice == 3:
        currency_name = input("Podaj skrót waluty która chcesz wyminić: ")
        currency_price_info = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency_name}/?format=json")
        currency_price = currency_price_info.json()['rates'][0]['mid']
        currency_quantity = int(input("Podaj ilość waluty która chcesz wyminić: "))
        result = currency_quantity * float(currency_price)
        print(f"Po wymianie waluty otrzymasz: {result}" + "zł")

    print("Pythonowy Kantor 🐍") 
    print(" ")   
    print("1. Pokaz aktualną cene złota")
    print("2. Pokaż dostępne waluty do sprawdzenia")
    print("3. Wymiana walut")
    print("4. Wyjdź")
    print(" ")   
    user_choice = int(input("Wybierz liczbe: "))
    print()
