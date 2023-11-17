while True:
  grade = float(input("Enter your total grade (0-100): "))
  if 0 <= grade <= 100:
    break
  else:
    print("Please enter a valid grade within the range 0 to 100.")
if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")