def validate_customer(customer):
    if not customer.get("name"):
        raise ValueError("Customer name is required")
    if not customer.get("email"):
        raise ValueError("Customer email is required")
    return True
