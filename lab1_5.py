def check_multiple(number: int) -> bool:
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

def check_password(input_string: str) -> str:
    return "access granted" if input_string == "CSC101Password" else "access denied"

def calculate_federal_tax(salary: int) -> int:
    taxTypes = [
        {"maxamt": 11000, "tax": 1000},
        {"maxamt": 44725, "tax": 1200},
        {"maxamt": 95375, "tax": 11000},
        {"maxamt": float("inf"), "tax": 24000}  # For salaries above 95375
    ]  # Tax Info Dictionary

    if salary <= taxTypes[0]["maxamt"]:
        return taxTypes[0]["tax"]
    elif salary <= taxTypes[1]["maxamt"]:
        return taxTypes[1]["tax"]
    elif salary <= taxTypes[2]["maxamt"]:
        return taxTypes[2]["tax"]
    else:
        return taxTypes[3]["tax"]  # Highest tax bracket
