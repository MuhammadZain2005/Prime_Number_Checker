# Prime Number Checker

This Python program checks if a given number is prime and includes several enhancements for improved functionality and efficiency.

## Features

- **Input Validation**: Ensures the input is a valid integer.
- **Efficient Prime Checking**: 
  - Uses basic primality test for numbers less than \(10^7\).
  - Utilizes the Miller-Rabin primality test for large numbers.
- **Performance Metrics**: Measures and displays the time taken to check if a number is prime.
- **Prime Number Generation**: Generates and displays a list of prime numbers up to a specified limit.

## How to Use

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/prime-number-checker.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd prime-number-checker
    ```

3. **Run the program:**

    Execute the script using Python.

    ```bash
    python prime_number_checker.py
    ```

4. **Follow the prompts** to input the number you want to check and optionally generate a list of prime numbers.

## Example

```bash
Insert a number to see if it's prime > 29
The number 29 is a prime number.
Time taken to check: 0.000002 seconds

Do you want to generate a list of prime numbers up to a limit? (yes/no) > yes
Enter the limit > 50
Prime numbers up to 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Time taken to generate primes: 0.000036 seconds
```

## Comments
This program is designed to help you understand prime number checking, efficient algorithms for large numbers, and performance measurement in Python.

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to contribute by submitting a pull request or opening an issue if you find a bug or have a feature request.

```bash
You can save this content into a `README.md` file for your GitHub repository.
```
