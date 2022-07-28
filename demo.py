from calc import addition,multiplication
import calc as c

# from calc import multiplication
num1 = int(input("Enter Number 1 "))
num2 = int(input("Enter Number 2 "))
result_add = addition(num1,num2)
print(result_add)
result_mul = multiplication(num1,num2)
print(f'Multiplication is {result_mul}')