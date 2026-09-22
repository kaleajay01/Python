from premium.calculator import (calculate_premium as calculate_base_premium, calculate_tax, calculate_total)

from premium.repository import save_premium


def calculate_premium(sum_insured):

    premium = calculate_base_premium(sum_insured)

    tax = calculate_tax(premium)

    total = calculate_total(
        premium,
        tax
    )

    record = {
        "sum_insured": sum_insured,
        "premium": premium,
        "tax": tax,
        "total": total
    }

    save_premium(record)

    return record