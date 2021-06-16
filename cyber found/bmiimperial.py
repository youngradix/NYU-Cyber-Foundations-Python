weight = float(input("Please enter weight in pounds: "))
height = float(input("Please enter height in inches: "))
weight = weight * 0.453592
height = height * 0.0254

bmiCalculator = (weight)/(height**2)

if bmiCalculator < 18.5:
    status = "Underweight"
elif bmiCalculator > 18.5 and < 24.9:
    status = "Normal"
elif bmiCalculator > 25.0 and < 29.9:
    status = "Overweight"
else:
    status = "Obese"


bmi = print(f'bmi is: {bmiCalculator}, Status is ' + status)