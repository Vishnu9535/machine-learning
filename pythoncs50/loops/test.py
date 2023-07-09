# for _ in range(3):
#     print("meow "*3)
# students = {
#     "Hermoine": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# for student in students:
#     print(student,students[student],sep=" ,")
# students = [
#     {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]

# for student in students:
#     for i in student:
#         print(i,student[i], sep=", ",end="")
# #     print("\n")
# def main():
#     print_square(3)


# def print_square(size):

#     # For each row in square
#     for i in range(size):

#         # For each brick in row
#         for j in range(size):

#             #  Print brick
#             print("#", end="")

#         # Print blank line
#         print()


# main()
# def main():
#     print_square(3)


# def print_square(size):
#     for i in range(size):
#         print_row(size)


# def print_row(width):
#     print("#" * width)


# main()

# st="1234vishnu"
# print(st[0:3].isdecimal())
# z=dict()
# z={x: x**3 for x in [2,5,7]}
# print(z)
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))
for i in range(1,29,4):
    print(i)