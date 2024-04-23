print("Welcome to the Avenger's Personality Quiz. This quiz will tell you what Avenger you are from the Marvel Cinematic Universe.")
print("Please answer the following five questions to get your result using A, B, C, D, or E as your answer choices.")

questions = ("Others would describe you as ______?: ",
             "How do you work best?: ",
             "What matters most to you?: ",
             "What is your favorite movie/book genre?: ",
             "What superpower would you want to have?: ")

options = (("A. Mysterious", "B. Funny", "C. Carefree", "D. Arrogant", "E. Loyal"),
           ("A. Alone or with others", "B. By following others", "C. As the leader of a group", "D. Alone", "E. With a group"),
           ("A. Family", "B. Peace", "C. Order", "D. Love", "E. Justice"),
           ("A. Thriller", "B. Comedy", "C. Action", "D. Fantasy", "E. Drama"),
           ("A. Invisibility", "B. Super Speed", "C. Flight", "D. Telekinesis", "E. Strength"))

score = 0

q1 = input("Others would describe you as ______?:\n(A) Mysterious\n(B) Funny\n(C) Carefree\n(D) Arrogant\n(E) Loyal\n")
if q1 == "A":
    score += 1
elif q1 == "B":
    score += 2
elif q1 == "C":
    score += 3
elif q1 == "D":
    score += 4
elif q1 == "E":
    score += 5
else:
    print("Invalid answer.")

q2 = input("How do you work best?:\n(A) Alone or with others\n(B) By following others\n(C) As the leader of the group\n(D) Alone\n(E) With a group\n")
if q2 == "A":
    score += 1
elif q2 == "B":
    score += 2
elif q2 == "C":
    score += 3
elif q2 == "D":
    score += 4
elif q2 == "E":
    score += 5
else:
    print("Invalid answer.")


q3 = input("What matters most to you?:\n(A) Family\n(B) Peace\n(C) Order\n(D) Love\n(E) Justice\n")
if q3 == "A":
    score += 1
elif q3 == "B":
    score += 2
elif q3 == "C":
    score += 3
elif q3 == "D":
    score += 4
elif q3 == "E":
    score += 5
else:
    print("Invalid answer.")


q4 = input("What is your favorite movie/book genre?:\n(A) Thriller\n(B) Comedy\n(C) Action\n(D) Fantasy\n(E) Drama\n")
if q4 == "A":
    score += 1
elif q4 == "B":
    score += 2
elif q4 == "C":
    score += 3
elif q4 == "D":
    score += 4
elif q4 == "E":
    score += 5
else:
    print("Invalid answer.")


q5 = input("What superpower would you want to have?:\n(A) Invisibility\n(B) Super Speed\n(C) Flight\n(D) Telekinesis\n(E) Strength\n")
if q5 == "A":
    score += 1
elif q5 == "B":
    score += 2
elif q5 == "C":
    score += 3
elif q5 == "D":
    score += 4
elif q5 == "E":
    score += 5
else:
    print("Invalid answer.")    

if score >= 25:
  print("You are Captain America!")
elif score >= 20:
  print("You are Thor!")
elif score >= 15:
  print("You are Iron Man!")
elif score >= 10:
  print("You are Spider-Man!")
elif score >= 5:
  print("You are Black Widow!")


print("Thank you for playing!")
