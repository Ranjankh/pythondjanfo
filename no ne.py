import asyncio
#WAP to convert celsius to fahrenheit

# c=60

# fahrenheit = (c* (9.0/5.0) + 32)
# print(fahrenheit)

# def  outerfunction(x):
#     def innerfunction(y):
#         return x+y
#     return innerfunction

# closure_instance= outerfunction(4)
# result=closure_instance(5)
# print(result)


    

# def eFunction(a,b,c):
#     try:
#         result=(a/b)+c
#         return result
#     except ZeroDivisionError:
#         print("Error:Division by zero is not allowd")
#         return None
#     except Exception as e:
#         print("This is an error:(e)")

# a=int(input("Enter the value of a"))
# b=int(input("Enter the value of b"))
# c=int(input("enter the value of c"))
# result=eFunction(a,b,c)
# print(result)




# def efunctionfromCtoF(C,F):
#     F = (C* (9.0/5.0) + 32)
#     return F
# def efunctionfromFtoC(C,F):
#     C=(F-32)*5/9
#     return C

# C= float(input("Enter the value of F"))
# F=float(input("Enter the value of C"))

# Choice=input("Enter F to convert to F\nEnter C to convert to C")
# if(Choice=="f"):
#    print ( efunctionfromCtoF(C,F))
# elif(Choice =="c"):
#     print(efunctionfromFtoC(C,F))   


    
async def getData():
    print("I am Here ")
    await asyncio.sleep(2)
    print("I am Here after 2 seconds")

asyncio.run(getData())

