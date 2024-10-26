Credit Card Validation

This project contains a Python script to validate credit card numbers based on specific rules provided by a fictional ABCD Bank. The validation criteria are strict and ensure that the credit card number meets all the requirements, including proper formatting and avoiding repeated sequences of digits.

Problem Statement

A valid credit card number must meet the following conditions:

It must start with a 4, 5, or 6.
It must contain exactly 16 digits.
It may consist of digits grouped in 4, separated by one hyphen ("-"), but no other separators are allowed.
It must NOT have any other separators like spaces or underscores.
It must NOT have four or more consecutive repeated digits.
Valid Credit Card Numbers:
4253625879615786
4424424424442444
5122-2368-7954-3214
Invalid Credit Card Numbers:
42536258796157867 (Too many digits)
4424444424442444 (Four consecutive repeated digits)
5122-2368-7954 - 3214 (Extra spaces or separators)
Input

The program expects the following input format:

An integer N representing the number of credit card numbers to validate.
The next N lines each contain a credit card number.
Sample Input
yaml
Copy code
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
Output

For each credit card number, the program prints either Valid or Invalid based on the validation rules.

Sample Output
Copy code
Valid
Valid
Invalid
Valid
Invalid
Invalid
Usage

To run the program, follow these steps:

Clone the repository or download the script.
Run the script in your preferred Python environment.
bash
Copy code
python credit_card_validator.py
Input the number of credit card numbers and the credit card numbers themselves when prompted.
The program will print Valid or Invalid for each credit card number.
Explanation of the Code

The main validation logic is implemented using regular expressions. The script checks for:

Correct starting digit (4, 5, or 6).
Proper length of the credit card number (16 digits or groups of 4 digits with hyphens).
The absence of more than three consecutive repeated digits.
The exclusion of invalid characters or separators.
Example

Input:
yaml
Copy code
4
4253625879615786
4424424424442444
5122-2368-7954-3214
4253-6258-7961-57867
Output:
Copy code
Valid
Invalid
Valid
Invalid
