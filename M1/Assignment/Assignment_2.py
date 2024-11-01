Task: Sum all the odd numbers from 0 to 100 and print it to the screen.


Code:

total_sum = 0
# Starting fom 1 and range is upto 100
for number in range(1, 101, 2):  

    #print(number)
    total_sum += number
print("The sum of odd numbers from 0 to 100 is:", total_sum)
