weight = 85
height = 1.85
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi:.2f}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your bmi is {bmi:.2f}, you are normal weight.")
else:
    print(f"Your bmi is {bmi:.2f}, you are overweight.")
