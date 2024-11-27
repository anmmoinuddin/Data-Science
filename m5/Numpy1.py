# NumPy Essentials Practice Exercises Overview:
Time to test the knowledge on NumPy. Lets start with simple task and move on to more challenging ones!<br>
**Good Luck**<br>

&#9758; *Please note, there are several ways to get the required output, so your code could be different then what is provided in this notebook. <br>As long as you are getting the tasks done, it is fine at this stage. *
**1. What is the major difference between "`Vector`" and "`Matrix`"?**
# Please consult the lectures
Vectors are 1-dimensional array , in the contrary, matrixs are 2-dimensional,although it can have only one row or one column
**2. How to import `NumPy` library?** 
# To avoid overwriting the output, please code here 

import numpy as np
**3. Convert the given Python list into NumPy array and check its data type**
list_1 = [1,2,3,4,5]
# To avoid overwriting the output, please code here 
list_1 = [1,2,3,4,5]
my_array=np.array(list_1)
my_array,type(my_array)

**4. Generate `array [0,1,2,3,4,5]` using NumPy built-in function, `arange()`**
# To avoid overwriting the output, please code here 
num = np.arange(6)
num

**5. Generate an `array of "5" zeros` **
# To avoid overwriting the output, please code here 
np.zeros(5)

**6. Generate the following `matrix`.**
# To avoid overwriting the output, please code here 
np.zeros((3,4))

**7. Generate** `[1.,1.,1.,1.,1.]` **using NumPy built-in function?**
# To avoid overwriting the output, please code here 
x=np.ones(5)
print(x)


**8. Generate an array of "5" tens.**
# To avoid overwriting the output, please code here 
np.full(5,10,dtype=float)

**9. Use `arange()` to generate an array of even numbers between 50 and 100.**<br>
*50 and 100 are not included*
# To avoid overwriting the output, please code here 
np.arange(52,100,2)

**10. Generate an array of 10 linearly spaced points between 0 and 1.**<br>
**Output step size as well?**
# To avoid overwriting the output, please code here 
np.linspace(0, 1, 10)

**11. Perform the following tasks:**
* Generate a **`vector array of 25`** numbers using **`arange()`**
* write a code to convert the vector array into **`2-D matrix using reshape`**
* can we use **`shape`** instead of reshape as well?
# To avoid overwriting the output, please code here 

# Generating vector array
x=np.arange(25)
x
# To avoid overwriting the output, please code here 

# reshape to convert into 2-d
x.reshape(5,5)
# To avoid overwriting the output, please code here 
x.shape=(5,5)
x
# Using shape

**12. Please generate the following matrix.**
# To avoid overwriting the output, please code here 
t=np.arange(0.1,2.6,0.1)
t.reshape(5,5)


**13. Write a code to generate the output below, use "`linspace()`" and "`print()`"**
# To avoid overwriting the output, please code here 
 
linear_array = np.linspace(0, 24, 25, dtype=int)

matrx = linear_array.reshape(5, 5)
matrx

**14. What is the main difference between `linspace()` and `arange()`?**
# Please consult the lectures. 
# arange() takes 3rd argument as step size.
# linspace() take 3rd argument as no of point we want.
numpy.arange(start,stop,step) which takes start, stop and step as parameters,the start value is inclusive whereas stop value is exclusive.
the step value determines increment between elements.

numpy.linspace(start,stop,num) takes start,stop and num as parameters. both start and stop values are included in the resulting array.
the num parameter determines how many values to generate between the start and stop.
**15. How to generate a single random integer number using NumPy built-in function?**
# To avoid overwriting the output, please code here 
s=np.random.rand(4)
s

**16. Write a code to generate a 7x5 matrix of 35 random numbers? use rand here** <br>
*Notice, there are no ( ) in the output matrix!*
# To avoid overwriting the output, please code here
u=np.random.rand(7,5)
u 

**17. Generate the following matrix using NumPy's built-in method for identity matrix.**
# To avoid overwriting the output, please code here 
identity_matrix = np.eye(5)*5
identity_matrix

### You must be feeling comfortable using NumPy now!
# Great Job and Good Luck 
