from classStudent import *

def isExist(fullName):
    file = open("dataBase.txt", "r", encoding="utf-8")
    for row in file:
        if row.split(";")[0] == fullName:
            file.close()
            return True
    file.close()
    return False

def addStudent():
    try:
        fullName = input("Enter the full name: ")
        while True:
            sex = input("Enter the sex (Male/Female): ")
            if sex in ["Male", "Female"]:
                break
            else:
                print("We only accept Male or Female")
        className = input("Enter the class name: ")
        point = int(input("Enter the point: "))
        file = open("dataBase.txt", "a", encoding="utf-8")
        data = classStudent(fullName, sex, className, point)
        file.writelines(data.__str__() + "\n")
        file.close()
        print("Saved your data!")
    except:
        print("Sorry. There are some error!")


def removeStudent():
    fullName = input("Enter full name of student want to remove: ")
    if not isExist(fullName):
        print(fullName + " is not exist")
        return
    data = []
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        data = map(lambda item: item.split(";"), file)
        #file.close()
    except:
        print("Error when read file")
        return
    newData = list(filter(lambda item: item[0] != fullName, data))
    file = open("dataBase.txt", "w", encoding="utf-8")
    for row in newData:
        file.writelines(";".join(row))
    file.close()
    print("Deleted student whose name is " + fullName)


def updateStudent():
    fullName = input("Enter full name of student want to update: ")
    if not isExist(fullName):
        print(fullName + " is not exist")
        return
    print("Please enter information to update (Enter '.' to skip)")
    while True:
        sex = input("Sex (Male/Female): ")
        if sex in ["Male", "Female", "."]:
            break
        else:
            print("We only accept Male or Female or .")
    className = input("Class name: ")
    point = input("Point: ")
    data = []
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        data = list(map(lambda item: item.split(";"), file))
        # file.close()
    except:
        print("Error when read file")
        return
    for i in range(len(data)):
        if data[i][0] == fullName:
            data[i][1] = sex if sex != "." else data[i][1]
            data[i][2] = className if className != "." else data[i][2]
            data[i][3] = point + "\n" if point != "." else data[i][3]
    file = open("dataBase.txt", "w", encoding="utf-8")
    for row in data:
        file.writelines(";".join(row))
    file.close()
    print("Update student whose name is " + fullName)


def viewStudent():
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        print("| {} | {} | {} | {} |".format("Full name".center(20), "Sex".center(6), "Class name".center(10),
                                             "Point".center(4)))
        print("".center(53, "-"))
        for row in file:
            data = row.split(";")
            data[3] = int(data[3])
            sv = classStudent(*data)
            sv.showInfo()
        file.close()
    except:
        print("Error when read data")


def viewAfterSort():
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        print("| {} | {} | {} | {} |".format("Full name".center(20), "Sex".center(6), "Class name".center(10),
                                             "Point".center(4)))
        print("".center(53, "-"))
        listData = list(file)
        listData.sort(key=lambda item: int(item.split(";")[3]))
        for row in listData:
            data = row.split(";")
            data[3] = int(data[3])
            sv = classStudent(*data)
            sv.showInfo()
        file.close()
    except:
        print("Error when read data")

