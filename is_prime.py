def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """
    


    # Function implementation here ...
    output = True #setting the default to true as i assume the number input is a prime

    # Handle edge cases
    if num <= 1:
        output = False
    elif num <= 3:
        output = True
    else:
        # Check divisibility by 2 or 3
        if num % 2 == 0 or num % 3 == 0:
            output = False
        else:
            # Loop through numbers up to the square root of num
            for i in range(5, int(num**0.5) + 1, 6):
                if num % i == 0 or num % (i + 2) == 0:
                    output = False
                    break  # remove from the loop as soon as a divisor is found


    return output


# # # Run code example
boolean = is_prime(5)   # returns True
print(boolean)
  