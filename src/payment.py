def validate_payment(amount):
    if amount <= 0:
        raise ValueError("Payment amount must be positive")
    if amount > 100000:
        raise ValueError("Payment exceeds limit")
    return True
