# Assignment – Investment and Inflation Calculation
#
# 1) Calculate the return on investment after one year, save the following variables:
#    - capital = 5000
#    - rateOfInterest = 0.08 meaning 8%
#    - inflationRate = 0.15 meaning 15%
#
# 2) Calculate the return on investment and how much the capital value decreased due to inflation,
#    show these amounts in the console.
#
# 3) Add the return on investment to the capital and subtract the lost capital due to inflation,
#    show the final value in the console.


# 1) Variables
capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

# 2) Calculate profit and loss
return_on_investment = capital * rateOfInterest
inflation_loss = capital * inflationRate

print("Return on investment:", return_on_investment)
print("Capital lost due to inflation:", inflation_loss)

# 3) Calculate final value
final_value = capital + return_on_investment - inflation_loss
print("Final capital value after one year:", final_value)


