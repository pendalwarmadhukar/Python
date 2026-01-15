def is_prime(n: int) -> bool:
    """
    Check whether a number is prime.

    :param n: integer number
    :return: True if prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_prime(number):
        print("Prime number")
    else:
        print("Not a prime number")
    
