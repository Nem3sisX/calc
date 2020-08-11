import add
import subtract
import multiply
import division

a = int(input("Enter first val"))
b = int(input("Enter second val"))
print("----------MENU----------")
print("1.Add[a+b]")
print("2.Subtract[a-b]")
print("3.Multiply[a*b]")
print("4.Divide[a/b]")
op = int(input("Enter operation [1-4]"))

if op == 1:
    res = add.add(a, b)
    print("Sum is", res)

elif op == 2:
    res = subtract.subtract(a, b)
    print("Difference is", res)

elif op == 3:
    res = multiply.multiply(a, b)
    print("Answer is", res)

elif op == 4:
    res = division.division(a, b)
    print("Answer is", res)
