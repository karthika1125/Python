# try:                          # try -The try block lets you test a block of code for errors.
#     numerator=10
#     denominator=0
#     result=numerator/denominator
#     print(result)
# except:                         # except -The except block lets you handle the error.
#     print("error : Denominator cannont be zero")    


# try:
#     even_number=[2,4,6,8]
#     print(even_number[5])
# except IndexError:
#     print("index out of bound")    


# try:
#     num=int(input("Enter a number: "))
#     assert num%2==0
# except:
#     print("not an even number ")
# else:                          # else - The else block lets you execute code when there is no error.
#     reciprocal=1/num
#     print(reciprocal)        



# try:
#     numerator=int(input("Enter a value: "))     #user input
#     denominator=0
#     result=numerator/denominator
#     print(result)
# except:
#     print("Error: Denominator cannot be 0 ")

# finally:                        # finally - The finally block lets you execute code, regardless of the result of the try- and except blocks.
#     print("This is done")        