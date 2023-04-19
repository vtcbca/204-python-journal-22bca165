import numpy as np


marks = np.array([
    [75, 80, 85, 90, 95],
    [60, 70, 80, 90, 100],
    [70, 75, 80, 85, 90],
    [80, 85, 90, 95, 100],
    [65, 70, 75, 80, 85]
])


def print_min_marks():
    min_marks = np.min(marks, axis=0)
    print("Minimum marks in each subject:", min_marks)


def print_max_marks():
    max_marks = np.max(marks, axis=0)
    print("Maximum marks in each subject:", max_marks)


def print_avg_marks():
    avg_marks = np.mean(marks, axis=0)
    print("Average marks in each subject:", avg_marks)


def print_mode_marks():
    mode_marks = []
    for i in range(marks.shape[1]):
        unique_marks, counts = np.unique(marks[:,i], return_counts=True)
        mode = unique_marks[np.argmax(counts)]
        mode_marks.append(mode)
    print("Mode marks in each subject:", mode_marks)


def print_variance():
    variance = np.var(marks, axis=0)
    print("Variance of marks in each subject:", variance)


def print_student_total():
    student_total = np.sum(marks, axis=1)
    print("Total marks of each student:", student_total)


while True:
    print("""
    Menu:
    1. Print the minimum marks of each subject.
    2. Print the maximum marks of each subject.
    3. Print the average marks of each subject.
    4. Print the marks which are most student get or repeated in subject. 
    5. Find the variance value for each subject marks.
    6. Print the total of each student.
    7. Quit.
    """)

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        print_min_marks()
    elif choice == '2':
        print_max_marks()
    elif choice == '3':
        print_avg_marks()
    elif choice == '4':
        print_mode_marks()
    elif choice == '5':
        print_variance()
    elif choice == '6':
        print_student_total()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")
