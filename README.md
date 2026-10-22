# 1.  Pythagorean Theorem
This program takes three integers as input and checks whether they satisfy the Pythagorean theorem.

It calculates the square of each number and checks whether the square of one number equals the sum of the squares of the other two numbers. If the condition is true, it prints Yes; otherwise, it prints No.

Example: If the inputs are 3, 4, and 5, the output will be Yes, because 3² + 4² = 5².
  
# 2. Power of Two
This program takes an integer as input and checks the powers of 2, starting from 2⁰ and moving upward.

At each step, the program compares the input number with the current power of 2. When it finds a power of 2 that is greater than the input number, it prints that value and stops the loop using the break statement.

Example: If the input is 10, the program checks the powers of 2:

1, 2, 4, 8, 16

Since 16 is the first power of 2 greater than 10, the output will be 16.
# 3. Reverse Number Comparison
This program takes two strings as input and reverses each one before comparing them.

It uses [::-1] to reverse the characters of each input. Then, it compares the reversed strings and displays the result using comparison operators such as < or =.

Example: If the inputs are 123 and 321, their reversed forms will be 321 and 123, respectively. The program then compares these reversed strings.

Note: The comparison is performed between strings, not numeric values, so the result is based on character order.
# 4. Number Statistics
This program takes four integers as input and performs five mathematical operations:
- Sum: Calculates the sum of the four numbers.
- Average: Calculates the average by dividing their sum by 4.
- Product: Calculates the product of the four numbers.
- Maximum: Finds the largest number.
- Minimum: Finds the smallest number.
Finally, the program displays all the results using print(). The :.6f format specifier displays numerical results with six decimal places.

Example: If the inputs are 2, 4, 6, and 8, the results will be:
- Sum: 20
- Average: 5
- Product: 384
- Maximum: 8
- Minimum: 2
# 5. Number Difference Calculator
This program takes six integers as input and compares them with the expected values 1, 1, 2, 2, 2, 8.

For each input, the program subtracts the entered value from the corresponding expected value and displays the six results.

Example: If the inputs are 1 1 2 2 2 8, the output will be:

0 0 0 0 0 0

If all the results are zero, it means that all the input numbers match the expected values.

Note: This program does not actually find missing numbers. Instead, it calculates the difference between each input and its expected value.

# 6.