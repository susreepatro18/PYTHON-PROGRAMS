def fractional_knapsack(items, capacity):
    # Calculate value to weight ratio for each item
    items = sorted(items, key=lambda item: item[0] / item[1], reverse=True)

    total_value = 0.0  # Total value accumulated
    for value, weight in items:
        if capacity >= weight:
            # If the entire item can be taken, take it
            capacity -= weight
            total_value += value
        else:
            # Take the fraction of the item that fits
            total_value += value * (capacity / weight)
            break  # Bag is full

    return total_value


# Example usage:
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
print(fractional_knapsack(items, capacity))  # Output: 240.0
