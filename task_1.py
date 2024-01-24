from datetime import datetime
def get_days_from_today(date): 
    try:
        return datetime.today().toordinal() - datetime.strptime(date, "%Y-%m-%d").toordinal()
    except ValueError: 
        return f"Введена дата: '{date}' не відповідає формату 'РРРР-ММ-ДД'"