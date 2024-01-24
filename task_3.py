import re
def normalize_phone(phone_number):
    pattern = r"[^0-9]" 
    replacement = ""
    clean_phone_number = re.sub(pattern, replacement, phone_number) #Прибирає з номеру все крім цифр
    pattern = r"\d*(\d{10})"
    replacement = r"+38\1"
    formatted_phone = re.sub(pattern, replacement, clean_phone_number) #Залишає лише останні 10 цифр номеру та додає "+38" на початок
    return formatted_phone if len(formatted_phone)==13 else f"Номер телефону має містити щонайменше 10 цифр"