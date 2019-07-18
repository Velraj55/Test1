is_male = True
is_tall = True

if is_male and is_tall:
    print("It is Male tall guy")

elif not(is_male) and is_tall :
    print("It is not a tall male guy")

elif is_male and not(is_tall):
    print("It is a small male guy")

elif is_male or is_tall:
    print("It is either Male or tall guy")

else:
    print("It is female")
