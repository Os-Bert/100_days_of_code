student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

highest_score = 0

for score in student_heights:
    if score > highest_score:
        highest_score = score

print(f" The highest score in the class is: {highest_score}")
