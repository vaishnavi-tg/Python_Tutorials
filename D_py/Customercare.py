city=input("Enter the city name\n")
list=["Hyderabad","Mumbai","Banglore","Mysuru","Delhi"]
if city.strip().title() in list:
    print(city," City has the customer care center availabel")
else:
    print(city,"City dosent have a customer care center")    