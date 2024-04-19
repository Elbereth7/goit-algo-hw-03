import re

def normalize_phone(phone_number):
# Normalizing phone number to '+38\d{10}$' format
    try:
        normalized_phone = re.sub(r'\D', '', phone_number) # Remove all the elements that are not numbers (spaces, special signes, letters)
        if re.search(r'^38\d{10}$', normalized_phone):
            normalized_phone = f'+{normalized_phone}' # If phone number starts with '38' and has 12 numbers in total then add '+' prefix
        elif re.search(r'^0\d{9}$', normalized_phone):
            normalized_phone = f'+38{normalized_phone}' # If phone number starts with '0' and has 10 numbers in total then add '+38' prefix
        elif not normalized_phone.startswith('38') and not normalized_phone.startswith('0'): 
            # Raise a ValueError in case if phone number is not Ukrainian
            raise ValueError(f'Phone number {phone_number} is not valid. Please enter your Ukrainian phone number')
        if (len(normalized_phone) != 12 and normalized_phone.startswith('38')) or (len(normalized_phone) != 10 and normalized_phone.startswith('0')):
            # Raise a ValueError in case if phone number is too short / too long
            raise ValueError(f'Phone number {phone_number} is not valid. Please check the length of the phone number')
    except ValueError as ve: # In case phone number doesn't pass the value content validation
        normalized_phone = None
        print(ve)
    except TypeError as te: # In case phone number type is incorrect (eg. entered int or float instead of string)
        normalized_phone = None
        print(f'Phone number value {phone_number}: {te}')
    return normalized_phone

if __name__ == '__main__':
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
        "48783002635",
        "508374858",
        "+380 44 123 4567 34",
        "(050)88899001",
        12.3,
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
