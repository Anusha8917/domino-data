def create_order(customer_id, amount):
    if not customer_id:
        raise ValueError("Customer ID is required")
    return {"customer_id": customer_id, "amount": amount}
