numbers = ["4","5","6","7"]
friends = ["Velraj", "Arichandran", "Sharanya" , "Vihaan","VIHAAN"]

friends.extend(numbers)

friends.insert(2,"vipin")
friends.remove("Velraj")

#friends.sort()
friends.reverse()

friends2=friends.copy()
print(friends)
print (friends2)
