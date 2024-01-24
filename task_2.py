import random
def get_numbers_ticket(min, max, quantity):
    list = []
    if 1 <= min <= max <= 1000 and quantity - 1 <= (max-min):
        while len(list) < quantity:
            i = random.randint(min,max) 
            if i not in list:
                list.append(i)
            else:
                pass
        return sorted(list)
    else:
        return list