def validate_payment(amount):
    if amount <= 0:
        raise ValueError("Payment amount must be positive")
    return True
