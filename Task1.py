x=int(input("Enter a number: "))

if x==0:
    print(x,"is neither even nor odd number.")
elif(x%2==0):
    print(x,"is an even number.")
else:
    print(x,"is an odd number.")