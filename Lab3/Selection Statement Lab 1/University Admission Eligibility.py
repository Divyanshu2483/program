# University Admission Eligibility

percentage = float(input("Enter 12th percentage: "))
maths = input("Did you study Mathematics? (yes/no): ")
exam_score = float(input("Enter entrance exam score: "))

if percentage < 75:
    print("Not Eligible: Less than 75% in 12th")
elif maths != "yes":
    print("Not Eligible: Mathematics not studied")
elif exam_score < 80:
    print("Not Eligible: Entrance exam score less than 80")
else:
    print("Congratulations! You are Eligible for Admission")
