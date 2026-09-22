

def calculate_premium(sum_insured):

    rate = 0.05

    premium = sum_insured * rate

    return premium


def calculate_tax(premium):

    tax_rate = 0.18

    tax = premium * tax_rate

    return tax


def calculate_total(premium, tax):

    return premium + tax