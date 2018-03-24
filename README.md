# rollDie
This is a challenge for a class that I am interested in attending.

## Problem
Roll a number 1-10 from a 6-sided die.

## Solution 1
Divide the numbers 1-10 in half. Roll the die. If 1, 2, or 3 is rolled, it represents the numbers 1-5. If 4, 5, or 6 is rolled, it represents the numbers 6-10. Roll the die again until you get a number that isn't 6. If the first roll was less than or equal to 3 then return the number (which will be 1, 2, 3, 4, or 5), if the first roll was greater than 3, then return the number plus 5 (1+5=6, 2+5=7, 3+5=8, 4+5=9, or 5+5=10). This on average takes a little over 2 rolls.

## Solution 2
Roll the die 5 times. Rolling the 6-sided die 5 times because the least common multiple of 6 and 10 is 30 (6x5=3x10). Sum the results of each roll and modulo the sum by 10. Add one to the remainder and return the result. The modulo values are evenly distributed as well as the 6 sides of the dice (because of the LCM characteristic), so the results should be equally probable.
