def raiseToPower(base_num,pow_num):
    result = 1
    #final = 1
    for  letter in range(pow_num):
        result = base_num * result


    print(result)

base_num = int(input("Enter base num:"))
pow_num = int(input("Enter pow num:"))

raiseToPower(base_num,pow_num)