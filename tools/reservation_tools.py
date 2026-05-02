
def check_table_availability(date, time, branch):
    return f"Table is available at {branch} on {date} at {time}"

def book_table(name, date, time, branch):
    return f"Table booked for {name} at {branch} on {date} at {time}"

def get_today_special(branch):
    specials = {
        "Nasr City": "Grilled Salmon",
        "Maadi": "Steak with Mushroom Sauce"
    }
    return specials.get(branch, "Chef's Special")
