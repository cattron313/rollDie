# rollDie
This is a challenge for a class that I am interested in attending.

## Problem
Roll a number 1-10 from a six-sided die.

## Solution 1
Divide the numbers 1-10 in half. Roll the die. If 1, 2, or 3 is rolled, it represents the numbers 1-5. If 4, 5, or 6 is rolled, it represents the numbers 6-10. Roll the die again until you get a number that isn't 6. If the first roll was less than or equal to 3 then return the number (which will be 1, 2, 3, 4, or 5), if the first roll was greater than 3, then return the number plus 5 (1+5=6, 2+5=7, 3+5=8, 4+5=9, or 5+5=10)

## Solution 2
Roll the die N times where N is greater than 5. I think at least 5 because the least common multiple of 6 and 10 is 30. Sum the results of each roll and modulo the sum by 10. Add one to the remainder and return the result.
