#TempConvert.py
#Name: Emma Zechmann
#Date: 2/8/2026
#Assignment: Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  given_temp=int(input("give me a temperature in degrees fahrenheit: "))
  Given_cel= round((given_temp - 32) * 5/9,1)
  print(f"{given_temp} degrees fahrenheit is, {Given_cel} degrees celcius!")
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  

 

  
if __name__ == '__main__':
  main()
