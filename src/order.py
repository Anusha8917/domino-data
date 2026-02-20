def create_order(customer_id, amount):
    if not customer_id:
        raise ValueError("Customer ID is required")
    if amount <= 0:
        raise ValueError("Order amount must be positive")
    return {"customer_id": customer_id, "amount": amount, "status": "NEW"}
