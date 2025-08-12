''' Accept the average score of the student and print the result as follows:
0 to 59 Fail
60 t0 84 second class
85 tp 95 first class
96 to 100 Excellent
Also check for invalid score. No negative marking '''

average_score = int(input("Enter your average score to print the result: "))
if average_score >= 0 and average_score <= 59:
    print(" Result is Fail")
elif average_score <= 84:
    print("Result is second class")
elif average_score <= 95:
    print("Result is First class")
elif average_score <= 100:
    print("Result is Excellent")
else:
    print("Invalid Score")
