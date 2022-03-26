student_name = 'artuh'

marks = {
    'james': 90,
    'jules': 85,
    'artuh': 45
}

for student in marks:
    if student == student_name:
        print(marks[student])
        break

else:
    print('no entry with that name found')