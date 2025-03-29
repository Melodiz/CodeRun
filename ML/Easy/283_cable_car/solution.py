import numpy as np

def read_input():
    n = int(input())  # Read the number of points
    x_coords, y_coords = [], []
    for _ in range(n):
        x, y = map(int, input().split())  # Read each point's coordinates
        x_coords.append(x)
        y_coords.append(y)
    return x_coords, y_coords

def fast(x_coords, y_coords):
    x_prev, y_prev = 0, 0  # Initialize previous coordinates
    total_distance = 0
    stack = [(x_coords[0], y_coords[0], 0)]  # Initialize stack with the first point

    for i in range(len(x_coords)):
        current_point = (x_coords[i], y_coords[i], i)  # Current point with index
        
        # Process the stack to add additional distances
        while stack:
            last_point = stack.pop()
            if last_point[1] <= current_point[1]:  # Check if the last point is lower or equal in height
                distance = np.hypot(last_point[0] - current_point[0], last_point[1] - current_point[1])
                total_distance += distance
                if current_point[2] - last_point[2] == 1:  # Check if points are consecutive
                    total_distance -= distance  # Avoid double counting
                if not stack:
                    break
            else:
                stack.append(last_point)  # Push the last point back if it's higher
                break
        
        stack.append(current_point)  # Push the current point to the stack
        
        # Add the distance between consecutive points
        total_distance += np.hypot(x_coords[i] - x_prev, y_coords[i] - y_prev)
        x_prev, y_prev = x_coords[i], y_coords[i]  # Update previous coordinates

    return total_distance

def main():
    x_coords, y_coords = read_input()  # Read input coordinates
    result = fast(x_coords, y_coords)  # Calculate the total distance
    print(result)  # Print the result

if __name__ == "__main__":
    main()