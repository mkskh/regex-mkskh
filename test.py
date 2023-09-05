import re

print('')

name = input('Write a name for verification (The first letter must be capitalized): ')
check_name = re.compile("^[A-Z]{1}[a-z]+$")
print(check_name.search(name))

print('')

surname = input('Write a surname for verification (The first letter must be capitalized): ')
check_surname = re.compile("^[A-Z]{1}[a-z]+$")
print(check_surname.search(surname))

print('')

phone_number = input('Write a phone number for verification (in format +11 111 1111 1111 (without spaces)): ')
check_phone = re.compile("^\+{1}[0-9]{13}$")
print(check_phone.search(phone_number))

print('')

birth_date = input('Write a date of birth for verification (in format dd.mm.yyyy): ')
check_birth = re.compile("^[0-9]{2}\.[0-9]{2}\.[0-9]{4}$")
print(check_birth.search(birth_date))

print('')

email = input('Write an e-mail for verification: ')
check_email = re.compile("^[a-zA-Z0-9\.\-\_]+@{1}[a-zA-Z]+\.[a-zA-Z]{2,3}$")
print(check_email.search(email))

print('')


