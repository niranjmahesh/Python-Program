number_value = int(input("Please enter an integer :"))
flag = False

if (number_value) == 0 or (number_value) == 1 :
    print("The number {0} is prime ".format(number_value))

elif (number_value) > 1 :
    for prime_number  in range (2 , number_value):
        if (number_value % prime_number == 0) :
            print("The number {0} is NOT prime ".format(number_value))
            break
        elif (number_value == prime_number+1):
            print("The number {0} is prime ".format(number_value))

        

    
       
        