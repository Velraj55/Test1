MonthConversions ={
    "jan":"January",
    "feb":"February",
    "Mar":"March"
    }

print (MonthConversions["feb"])
print (MonthConversions.get("Mar"))

fromUsr = input("Enter Mont abbr: ")
#print (MonthConversions[fromUsr])
print (MonthConversions.get(fromUsr))

#print (MonthConversions["luv"])
print (MonthConversions.get(fromUsr,"Not valid one"))


