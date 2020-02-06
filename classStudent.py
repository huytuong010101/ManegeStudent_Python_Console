class classStudent:
    def __init__(self, fullName=None, sex=None, className=None, point=None):
        self._fullName = fullName
        self._sex = sex
        self._className = className
        self._point = point

    def __str__(self):
        return self.fullName + ";" + self.sex + ";" + self.className + ";" + str(self.point)

    def showInfo(self):
        print("| {} | {} | {} | {} |".format(self.fullName.center(20), self.sex.center(6), self.className.center(10), str(self.point).center(4)))

    @property
    def fullName(self):
        return self._fullName

    @fullName.setter
    def fullName(self, fullName):
        self._fullName = fullName

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, sex):
        self._sex = sex

    @property
    def className(self):
        return self._className

    @className.setter
    def className(self, className):
        self._className = className

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point):
        self._point = point

    @property
    def title(self):
        return "Good" if self.point > 5 else "Bad"
