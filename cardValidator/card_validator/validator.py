def get_issuer(number: str) -> str:
    number = "".join(number.split())

    if number.startswith('4') and len(number) == 16:
        return 'Visa'

    starts_with_amex = number.startswith('34') or number.startswith('37')
    if starts_with_amex and len(number) == 15:
        return 'American Express'

    starts_with_master = number.startswith('51') or number.startswith('52') or number.startswith(
        '53') or number.startswith('54') or number.startswith('55')
    if starts_with_master and len(number) == 16:
        return 'MasterCard'

    raise ValueError('Invalid Card Number')
