def manage_inventory(inventory, item_name, target_category):
    try:
        if item_name not in inventory:
            raise ValueError(f"Item '{item_name}' not found in inventory.")
    except ValueError as e:
        return str(e), ()

    total_value = 0.0
    categories = set()

    for item, details in inventory.items():
        price, quantity, category = details
        categories.add(category)

        if category == target_category:
            item_value = price * quantity

            if quantity > 50:
                item_value *= 0.9   # 10% discount

            total_value += item_value

    return total_value, tuple(categories)


# ----- GIVEN INVENTORY -----
inventory = {
    "Laptop": [999.99, 30, "Electronics"],
    "Shirt": [19.99, 60, "Clothing"],
    "Phone": [499.99, 45, "Electronics"]
}

print(manage_inventory(inventory, "Shirt", "Electronics"))
