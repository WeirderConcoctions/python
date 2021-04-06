conversion = input("Choose one of the Following\n1.Celcius to Fahrenheit\n2.Farenheit to Celcius\n3. Kelvin to Celsius\n4. Kelvin to Farenheit\n5. Celsius to Kelvin\n6. Fahrenheit to Kelvin\n7. Get Formulas for both ConversionsEnter choice here (1/2/3/4/5/6/7): ")
if conversion == '1':
          celsiusinput = float(input("Enter Celcius Value to be converted here: "))
          fahrenheit = (celsiusinput * 1.8) + 32
          print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsiusinput,fahrenheit))
elif conversion == '2':
          fahrenheitinput = float(input("Enter Fahrenheit Value to be converted here: "))
          celsius = (fahrenheitinput - 32) / 1.8
          print('%0.1f degree Fahrenheit is equal to %0.1f degree Celsius' %(fahrenheitinput,celsius))
elif conversion == '3':  
          kelvininput = float(input("Enter Kelvin Value to be converted here: "))
          celsius = kelvininput - 273.15
          print('%0.1f degree Kelvin is equal to %0.1f degree Celsius' %(kelvininput,celsius))
elif conversion == '4':
          kelvininput = float(input("Enter Kelvin Value to be converted here: "))
          fahrenheit = ((kelvininput - 273.15)*1.8) + 32
          print('%0.1f degree Kelvin is equal to %0.1f degree Fahrenheit' %(kelvininput,fahrenheit))
elif conversion == '5':
          celsiusinput = float(input("Enter Celsius Value to be converted here: "))
          kelvin = (celsiusinput + 273.15)
          print('%0.1f degree Kelvin is equal to %0.1f degree Fahrenheit' %(celsiusinput,kelvin))
elif conversion == '6':
          celsiusinput = float(input("Enter Fahrenheit Value to be converted here: "))
          kelvin = ((fahrenheitinput - 32) / 1.8) + 273.15
          print('%0.1f degree Kelvin is equal to %0.1f degree Fahrenheit' %(fahrenheitinput,kelvin))
elif conversion == '7':
          print("Celsius to Fahrenheit: (0°C × 9/5) + 32 = 32°F\nFahrenheit to Celsius: (32°F − 32) × 5/9 = 0°C\nKelvin to Celsius: 0K − 273.15 = -273.1°C\nKelvin to Fahrenheit: (0K − 273.15) × 9/5 + 32 = -459.7°F\nCelsius to Kelvin: 0°C + 273.15 = 273.15K\nCelsius to Fahrenheit: 0°C + 273.15 = 273.15K\n")