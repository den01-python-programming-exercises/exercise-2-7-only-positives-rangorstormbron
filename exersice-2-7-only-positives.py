while True:
    number=int(input("please give a positive interger"))

    if (number ==0):
        print("output =" ,str(number**2))
        break
    elif (number <= 0):
        print("invalid number try again")
        continue
    elif (number >=0):
        print("output =" ,str(number**2))
        break 
    
