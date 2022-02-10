def final_grade(homework, assessment, exam):
    percentage_score = ((int(homework_score) + int(assessment_score) + int(exam_score)) / 1.75)
    return percentage_score

user_name = input("Pease enter your full name: ")
homework_score = input("Pease enter your homework score (out of 25): ")
assessment_score = input("Pease enter your assessment score (out of 50): ")
exam_score = input("Please enter your final exam score (out of 100): ")

print(user_name + " your final score is: " + str(final_grade(homework_score, assessment_score, exam_score)))


