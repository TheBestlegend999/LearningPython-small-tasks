
# Assignment – Temperature Check Program
#
# Write a program that decides whether to go outside or stay home
# depending on the weather conditions.
#
# Instructions:
# 1) Create variables:
#    - haveUmbrella = False
#    - isRaining = True
#    - temperature = 14
# 2) Check if temperature is above or equal to 40, below or equal to 0.
#    If so, print "Stay at home."
# 3) If the above condition is not met, use elif to check if it’s raining
#    and temperature is below 10, and you have an umbrella.
#    If true, print "You can go out with an umbrella."
# 4) Add another elif to check if it’s not raining and temperature is above 10.
#    If true, print "You can go out without an umbrella."
# 5) Finally, add a default else option with the message "Stay at home!"

#1 Create variables
haveUmbrella = False
isRaining = True
temperature = 14

#2 Check extreme temperatures
if temperature >= 40 or temperature <= 0:
    print("Stay at home.")

#3 Check if it’s raining and cold, but you have an umbrella
elif isRaining and temperature < 10 and haveUmbrella:
    print("You can go out with an umbrella.")

#4 Check if it’s not raining and warm enough
elif not isRaining and temperature > 10:
    print("You can go out without an umbrella.")

#5 Default condition
else:
    print("Stay at home!")



