# function to calculate wind chill
def wind_chill(t, v):
    return 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)

t = input("Enter the temperature in Farenheit:-")
v = input("Enter the speed of wind in miles per hour:-")
windchill = wind_chill(t,v)
print(f"Wind chill = {windchill}")
