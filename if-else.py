#if-else statement

score = float(input("Enter Students Score"))
grade = ""

if score >=80:
    grade = "A+"
    remark = "Outstanding!"
elif score >=70:
    grade = "A"
    remark = "Excellent!"
elif score >=60:
    grade = "A-"
    remark = "Very Good!"
elif score >=50:
    grade = "B"
    remark = "Keep working on yourself!"
elif score >=40:
    grade = "B"
    remark = "Passed! Need to improve."
else:
    grade = 'F'
    remark = "Failed! Please retake the course."
print(f"Grade :{grade}. {remark}")