def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item.append(item[0] / item[1])

    # Sort the items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        if capacity == 0:
            break

        if item[1] <= capacity:
            total_value += item[0]
            knapsack.append(item)
            capacity -= item[1]
        else:
            fraction = capacity / item[1]
            total_value += item[0] * fraction
            knapsack.append([item[0] * fraction, item[1] * fraction, item[2]])
            capacity = 0

    return total_value, knapsack

if __name__ == "__main__":
    # Example usage
    items = [
        [60, 10],  # [value, weight]
        [100, 20],
        [120, 30],
    ]
    capacity = 50

    max_value, selected_items = fractional_knapsack(items, capacity)

    print("Maximum value in the knapsack:", max_value)
    print("Selected items:")
    for item in selected_items:
        print(f"Value: {item[0]}, Weight: {item[1]}")

