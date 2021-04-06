conversion = input("Choose one of the Following\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n\nNote that this calculator gives answers only upto the first decimal point\nEnter the number representing the operation needed to be performed (1/2/3/4/): ")
if conversion == '1':
          firstnumber = float(input("Enter the first Value to be operated on here: "))
          secondnumber = float(input("Enter the second Value to be operated on here: "))
          print('%0.1f added to %0.1f is equal to %0.1f ' %(firstnumber,secondnumber, firstnumber+secondnumber))
elif conversion == '2':
          firstnumber = float(input("Enter the first Value to be operated on here: "))
          secondnumber = float(input("Enter the second Value to be operated on here: "))
          print('%0.1f subtracted from %0.1f is equal to %0.1f ' %(secondnumber,firstnumber, firstnumber-secondnumber))
elif conversion == '3':  
          firstnumber = float(input("Enter the first Value to be operated on here: "))
          secondnumber = float(input("Enter the second Value to be operated on here: "))
          print('%0.1f multiplied by %0.1f is equal to %0.1f ' %(firstnumber,secondnumber, firstnumber*secondnumber))
elif conversion == '4':
          firstnumber = float(input("Enter the first Value to be operated on here: "))
          secondnumber = float(input("Enter the second Value to be operated on here: "))
          print('%0.1f divided by %0.1f is equal to %0.1f ' %(firstnumber,secondnumber, firstnumber/secondnumber))
else: 
     print("Invalid Input")