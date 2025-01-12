#Nested if --> condition inside the other condition
#greater in 3 numbers
a=int(input("Enter the value for A \n")) #100
b=int(input("Enter the value for B \n")) #2015
c=int(input("Enter the Value for C \n")) #215

if a>b:
    if a>c:
        print(a," is greater")
    else:
        print(c," is greater")
else:
    if b>c:
        print(b," is greater")
    else:
        print(c," is greater")