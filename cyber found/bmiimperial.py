
weight = float(input("Please enter weight in pounds: "))
height = float(input("Please enter height in inches: "))
weight = weight * 0.453592
height = height * 0.0254

bmiCalculator = (weight)/(height**2)

bmi = print(f'bmi is: {bmiCalculator}')