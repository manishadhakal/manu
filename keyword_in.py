# print(r"lineA\nlineB")
# num1,num2,num3=input("enter your three number").split( )
# print(f"this is  your average{int(num1)+int(num2)+int(num3)//3}")


def function (num1,num2):
    if num1>num2:
        return num1
    else:
        return  num2
firstnumber=input("enter your 1st number")
secondnumber=input("enter your 2nd number")
greatest=function(firstnumber,secondnumber)
print(f"this is the greatest number{greatest}")

