from method import *
optinals = '''
    1. Add student
    2. Remove student
    3. Update student
    4. View all student
    5. View all student after sort by point
    6. Exit
'''

actionOptional = dict()
actionOptional["1"] = addStudent
actionOptional["2"] = removeStudent
actionOptional["3"] = updateStudent
actionOptional["4"] = viewStudent
actionOptional["5"] = viewAfterSort

print("       Welcome to manager student program")
while True:
    print(optinals)
    print("Please enter your option: ", end="")
    optinal = input()
    if optinal == "6":
        print("Thanks for using program - GOODBYE")
        break
    if optinal not in actionOptional:
        print("No match with any action, please choose again")
    else:
        actionOptional[optinal]()
