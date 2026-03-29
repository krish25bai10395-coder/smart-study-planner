

from data_handler import add_study_session, add_score
from analytics import study_analysis, score_analysis, weak_subject
from predictor import predict_score

while True:
    print("\nSmart Study Planner")
    print("1. Add Study Session")
    print("2. Add Test Score")
    print("3. Study Analysis")
    print("4. Score Analysis")
    print("5. Weak Subject")
    print("6. Predict Next Score")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        subject = input("Subject: ")
        hours = float(input("Hours studied: "))
        add_study_session(subject, hours)

    elif choice == "2":
        subject = input("Subject: ")
        score = float(input("Score obtained: "))
        total = float(input("Total marks: "))
        add_score(subject, score, total)

    elif choice == "3":
        study_analysis()

    elif choice == "4":
        score_analysis()

    elif choice == "5":
        weak_subject()

    elif choice == "6":
        subject = input("Enter subject: ")
        predict_score(subject)

    elif choice == "7":
        break

    else:
        print("Invalid choice")