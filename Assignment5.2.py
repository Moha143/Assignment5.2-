largest = None
smallest = None
 
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        n=int(num)
        if largest<n:
            largest=n
 
        if smallest== None:
            smallest=n
        elif smallest>n:
            smallest=n
        continue
    except:
        print('Invalid input')
 
 
 
print('Maximum is', largest)
print('Minimum is',smallest)