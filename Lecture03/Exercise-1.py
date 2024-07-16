score1 = float(input("Enter your first score: "))
score2 = float(input("Enter your second score: "))
score3 = float(input("Enter your third score: "))

average_score = (score1 + score2 + score3) / 3

if average_score >= 95:
    print("Your average score is ", format(average_score, ".2f"))
    print("Congratulations!!")
elif average_score >= 70:
    print("Your average score is ", format(average_score, ".2f"))
    print("you did good")
else:
    print("Your average score is ", format(average_score, ".2f"))
    print("Nah. ")