print('Welcome to the Avenger's Personality Quiz. This quiz will tell you what Avenger you are from the Marvel Cinematic Universe.')
print('Please answer the following five questions to get your result using A, B, C, D, or E as your answer choices.')

questions = ("Others would describe you as ______?: ",
             "How do you work best?: ",
             "What matters most to you?: ",
             "What is your favorite movie/book genre?: ",
             "What superpower would you want to have?: ")

options = (("A. ", "B. ", "C. ", "D. ", "E. "),
           ("A. ", "B. ", "C. ", "D. ", "E. "),
           ("A. ", "B. ", "C. ", "D. ", "E. "),
           ("A. ", "B. ", "C. ", "D. ", "E. "),
           ("A. ", "B. ", "C. ", "D. ", "E. "))

score = 0
A = 0
B = 0
C = 0
D = 0
E = 0
answers = []
totalscore = A + B + C + D + E
qnumber = 0


for question in questions:
  print("-----------------------------")
  print(questions)
  for option in options[qnumber]:
    print(option)

answer = input("Enter (A, B, C, D, E): ").upper()
answers.append(answer)
if guess == "A":
  A += 1
elif guess == "B":
  B += 2
elif guess == "C":
  C += 3
elif guess == "D":
  D += 4
elif guess == "E":
  E += 5
else:
  print("Invalid input.")

qnumber += 1

print("-----------------------------")
print("-----------RESULTS-----------")
print("-----------------------------")

if score >= 25:
  print("You are
elif score >= 20:
  print("You are
elif score >= 15:
  print("You are
elif score >= 10:
  print("You are
elif score >= 5:
  print("You are
