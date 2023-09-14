from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Функція повинна коректно працювати з порожнім списком користувачів.
    if not users:
        return {}

    today = date.today()
    week = today + timedelta(days=6)
    happy_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    happy_users = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    }

    for x in users:
        new_b_day = datetime(today.year, x["birthday"].month, x["birthday"].day).date()
        if x["birthday"].year < today.year:
            b_day = datetime(today.year, x["birthday"].month, x["birthday"].day).date()
            if b_day < today:
                b_day = datetime(
                    today.year + 1, x["birthday"].month, x["birthday"].day
                ).date()
        else:
            b_day = x["birthday"]
        if today <= b_day <= week:
            weekday = 0 if b_day.weekday() in [0, 5, 6] else b_day.weekday()
            happy_users.setdefault(happy_days[weekday], []).append(x["name"])

    users = {}
    for k in happy_users.keys():
        if happy_users[k]:
            users[k] = happy_users[k]

    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2022, 9, 14).date()},
        {"name": "John Lembur", "birthday": datetime(2023, 9, 19).date()},
        {
            "name": "Alice",
            "birthday": datetime(2021, 1, 1).date(),
        },
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
