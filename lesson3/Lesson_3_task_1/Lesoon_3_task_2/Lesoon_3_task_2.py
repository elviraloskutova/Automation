from smartpfone import Smartpfone

catalog = []

phone1 = Smartpfone("Samsung", "Galaxy S21", "+79884526314")
phone2 = Smartpfone("Apple", "iPhone 13", "+79774960990")
phone3 = Smartpfone("Xiaome", "Mi 12", "+79091371749")
phone4 = Smartpfone("Nokia", "Nseries", "+79654562531")
phone5 = Smartpfone("Motorola", "Moto G32", "+79854265369")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")