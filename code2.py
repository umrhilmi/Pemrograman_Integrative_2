def calculate_sum():
    total = 0
    while True:
        num = float(input("Enter a number (-1 to stop): "))
        if num == -1:
            break
        total += num
    print(f"Total sum: {total:.2f}")

# Example usage
calculate_sum()
