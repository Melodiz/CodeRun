from numpy import linspace

def F(x, y):
    if x + y == 0:
        return float('-inf')  # Avoid division by zero
    return 2 * x * y / (x + y)

max_value = float('-inf')
max_x = 0

size = 10_000
left = 0
right = 1

for epoch in range(10):
    x_values = linspace(left, right, size)

    for x in x_values:
        y = -12 * x / 5 + 12 / 5
        current_value = F(x, y)
        if current_value > max_value:
            max_value = current_value
            max_x = x

    # Update the search range centered around max_x
    range_width = (right - left) / 3
    left = max(0, max_x - range_width)
    right = min(1, max_x + range_width)
    # print(f"Epoch {epoch+1}: left = {left}, max_x = {max_x}, right = {right}, max_value = {max_value}")

print(f"Maximum value of F = {max_value} at x = {max_x}")
print("Rounded:", round(max_value, 6))