def is_prime(n):  # Function to check if a number is prime
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Checking divisibility
        if n % i == 0:
            return False
    return True

def sum_of_primes(start, end):  # Function to calculate sum of primes in range
    return sum(n for n in range(start, end + 1) if is_prime(n))

def length_converter(value, unit):  # Function to convert length units
    if unit.upper() == 'M':
        return round(value * 3.28084, 2)  # Meters to feet
    elif unit.upper() == 'F':
        return round(value / 3.28084, 2)  # Feet to meters
    else:
        return "Invalid unit"

def consonant_counter(text):  # Function to count consonants in a string
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)  # Counting consonants

def min_max_finder():  # Function to find min and max in user input
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    return f"Smallest: {min(numbers)}, Largest: {max(numbers)}"  # Min and max

def is_palindrome(text):  # Function to check for palindrome
    cleaned_text = ''.join(text.lower().split())  # Removing spaces, case insensitive
    return cleaned_text == cleaned_text[::-1]  # Checking if reversed string matches


def word_counter(filename):
    """Counts the occurrences of specific words in a text file."""
    words_to_count = ["the", "was", "and"]
    word_count = {word: 0 for word in words_to_count}
    
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()  # Read file and convert to lowercase
            for word in words_to_count:
                word_count[word] = text.split().count(word)  # Count occurrences of each word
    except FileNotFoundError:
        return "File not found"
    
    return word_count



def main():  # Main function to run the program
    while True:
        print("""
        Select a function (1-6):
        1. Calculate sum of prime numbers
        2. Convert length units
        3. Count consonants in string
        4. Find min and max numbers
        5. Check for palindrome
        6. Word Counter
        0. Exit program
        """)
        choice = input("Enter your choice: ")
        if choice == '1':
            start, end = map(int, input("Enter start and end range: ").split())
            print("Sum of primes:", sum_of_primes(start, end))
        elif choice == '2':
            value = float(input("Enter length value: "))
            unit = input("Enter conversion type (M/F): ")
            print("Converted value:", length_converter(value, unit))
        elif choice == '3':
            text = input("Enter a string: ")
            print("Number of consonants:", consonant_counter(text))
        elif choice == '4':
            print(min_max_finder())
        elif choice == '5':
            text = input("Enter a string: ")
            print("Palindrome:", is_palindrome(text))
        elif choice == '6':
            filename = input("Enter filename: ")
            print("Word count:", word_counter(filename))
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
        if input("Would you like to try another function? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()  # Running the main function













