def generate_fibonacci():
    fibonacci_list = []  # Create an empty list to store the Fibonacci numbers

    # Generate the Fibonacci sequence
    a, b = 0, 1
    for _ in range(7):
        fibonacci_list.append(a)  # Insert the current Fibonacci number into the list
        a, b = b, a + b  # Calculate the next Fibonacci number

    return fibonacci_list


# Call the function to generate and retrieve the Fibonacci numbers
fibonacci_sequence = generate_fibonacci()
print(fibonacci_sequence)