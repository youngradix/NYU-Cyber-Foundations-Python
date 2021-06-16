weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))


bmiCalculator = (weight)/(height**2)

if bmiCalculator < 18.5:
    status = "underweight"
elif bmiCalculator > 18.5 and bmiCalculator < 24.9:
    status = "normal"
elif bmiCalculator > 25.0 and bmiCalculator < 29.9:
    status = "overweight"
else:
    status = "obese"

bmiCalculator = round(bmiCalculator, 2)

bmi = print(f'bmi is: {bmiCalculator}, status is ' + status)