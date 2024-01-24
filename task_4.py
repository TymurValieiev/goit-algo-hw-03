# users = [
#     {"name": "John Doe", "birthday": "1985.01.25"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"},
#     {"name": "Den Brown", "birthday": "1987.05.11"},
#     {"name": "Andrea Cardini", "birthday": "1994.01.15"},
#     {"name": "Julia Roberts", "birthday": "1986.11.01"}
# ]

import re
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    current_day = datetime.now().date()

    current_year = current_day.strftime("%Y") #2024
    
    for user in users: # Змінюємо дати народження в словниках на поточний рік
        user["birthday"] = re.sub(r"\d{4}", current_year, user["birthday"]) 
        
    upcoming_birthdays = []

    for user in users: 
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        days_to_birthday = (birthday - current_day).days

        if 0 <= days_to_birthday <= 7: # Перевіряємо чи випадає день народження на поточний тиждень
            
            if birthday.weekday() >= 5: # Переносимо вихідний день на наступний понеділок
                days_to_birthday += (7 - birthday.weekday())

            congratulation_date = current_day + timedelta(days_to_birthday)

            upcoming_birthdays.append({'name': user['name'],'congratulation_date': congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)