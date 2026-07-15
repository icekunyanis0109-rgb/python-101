score_1 = int(input("What is your first score? : "))
score_2 = int(input("What is your second score? : "))
score_3 = int(input("What is your third score? : "))
average_score = (score_1 + score_2 + score_3) / 3
if average_score >= 95:
    print("The average score is:", f"{average_score:.2f}")
    print("Congratulation!\nThat is a great average!")
else:
    print("The average score is:", f"{average_score:.2f}")
