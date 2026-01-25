def validate_customer(customer):
    if not customer.get("name"):
        raise ValueError("Customer name is required")
    return True
