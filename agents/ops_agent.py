
from tools.reservation_tools import (
    check_table_availability,
    book_table,
    get_today_special
)

def handle_ops(query):
    query = query.lower()

    if "availability" in query:
        return check_table_availability("tomorrow", "8 PM", "Maadi")

    elif "book" in query:
        return book_table("User", "tomorrow", "8 PM", "Maadi")

    elif "special" in query:
        return get_today_special("Maadi")

    return "Operation not recognized."
