
raining = True
haveUmbrella = True
temperature =  1

if temperature >= 40 or temperature <= 0:
    print("Stay at home")
elif temperature > 0 and temperature < 10 and haveUmbrella and raining:
    print("You can go with Umbrella")
    
  
elif raining == False and temperature >= 10:
    print("You can go without Umbrella")
else:
    print("Stay at home")

