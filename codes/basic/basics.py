# Write your code here :-)

age = 12
name = "Ajeeb"

# print(name, age)

# if 'b' in name:
#     print('Boy')

print(">" * 10)

# for i in range(0, 20, 3):
#     print(i)


def print_mults(start, end, mult):
    for i in range(start, end, mult):
        print(i)


def print_pyramid(rows,twoside=False):
    print('>'*13)
    print('Print Pyramid')
    print('>'*13)
    for r in range(rows):
        if r==0:
            count = 1
        else:
            count = r+1
        if twoside:
            print(' '*(int(rows-count-1)),"*" * (2*count))
        else:
            print("*" * count)
    print('>'*13)


print_mults(0, 13, 4)

print_pyramid(10)
print_pyramid(10,twoside=True)


# class StudentMark:
#     mark_list = [("phy", 43), ("che", 32), ("bio", 29), ("math", 22)]

#     def __init__(self, marks=None, student="student_name"):
#         if marks:
#             self.mark_list = marks
#         self.student = student

#     def print_all(self):
#         for subj, mark in self.mark_list:
#             print("Student: ", self.student)
#             print(f"{subj}: {mark}")

#     def print_40_plus(self):
#         for subj, mark in self.mark_list:
#             if mark > 40:
#                 print("Student: ", self.student)
#                 print(f"{subj}: {mark}")


# student0 = StudentMark(student="New Student")
# student1 = StudentMark([("phy", 11), ("che", 24), ("bio", 29), ("math", 20)], "Sanju")
# student2 = StudentMark(
#     [("phy", 11), ("che", 24), ("bio", 29), ("math", 20)], "Sreeshanth"
# )

# print(" Print All Marks")
# print(">" * 10)
# student1.print_all()
# student2.print_all()

# print("40+ marks")
# print(">" * 10)
# student1.print_40_plus()
# student2.print_40_plus()

# print("Print mark with loop")
# print(">" * 10)
# all_students = [
#     student0,
#     student2,
#     student1,
# ]
# for st in all_students:
#     st.print_40_plus()


# start, end, step = input('Enter 3 numbers with space \n').split()
# print_mults(int(start), int(end), int(step))