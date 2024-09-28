# Prime Number Checker and Generator

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate all prime numbers up to a certain limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    while True:
        print("\nOptions:")
        print("1. Check if a number is prime")
        print("2. Generate a list of prime numbers up to a limit")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            num = int(input("Enter a number to check if it's prime: "))
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        
        elif choice == '2':
            limit = int(input("Generate prime numbers up to: "))
            primes = generate_primes(limit)
            print(f"Prime numbers up to {limit}: {primes}")
        
        elif choice == '3':
            print("Exiting the Prime Number Checker.")
            break
        
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
