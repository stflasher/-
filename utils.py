import re

def validate_date(date_string):
    pattern = r'\d{4}-\d{2}-\d{2}'
    return re.match(pattern, date_string)

def validate_amount(amount_string):
    return amount_string.replace('.', '', 1).isdigit()
