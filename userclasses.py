class User:
    """A sample user superclass"""

    def __init__(self,first,last,username,password,dob,email,typeOfUser,pic):
        self.first = first
        self.last = last
        self.username = username
        self.password = password
        self.dob = dob
        self.email = email
        self.type = typeOfUser
        self.pic = pic


    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @property
    def dobyear(self):
        return self.dob[6:]
    
    @property
    def dobmonth(self):
        return self.dob[3:5]
    
    @property
    def dobday(self):
        return self.dob[:2]
            
class Student(User):
    """A students basic attributes"""
       
    def __init__(self,first,last,username,password,dob,email,typeOfUser,yeargroup,pic,achievementpoints,behaviourpoints):
        super(Student,self).__init__(first,last,username,password,dob,email,typeOfUser,pic)
        self.yeargroup = yeargroup
        self.achievementpoints = achievementpoints
        self.behaviourpoints = behaviourpoints

class Class:
    """A sample class"""

    def __init__(self,yearGroup,teacher,subject,id,lesson1,lesson2,lesson3,lesson4):
        self.yearGroup = yearGroup
        self.teacher = teacher
        self.subject = subject
        self.id = id
        self.lesson1 = lesson1
        self.lesson2 = lesson2
        self.lesson3 = lesson3
        self.lesson4 = lesson4


class Subject:
    """A sample subject"""
    def __init__(self,fullname,shortname,head):
        self.fullname = fullname
        self.shortname = shortname
        self.head = head


class Behaviourpoint:
    """A sample behaviour point"""
    def __init__(self,teacher,student,points,reason):
        self.teacher = teacher
        self.student = student
        self.points = int(points)
        self.reason = reason

class Achievementpoint(Behaviourpoint):
    """A sample achievement point"""
    pass

class StudentClass:
    """A class that links students and their classes"""
    def __init__(self,student,currentClass):
        self.student = student
        self.currentClass = currentClass
        self.predicted = none

class Homework:
    def __init__(self,homeworkId,classId,due,title,desc):
        self.homeworkId = homeworkId
        self.classId = classId
        self.due = str(due)
        self.title = title
        self.desc = desc

    @property
    def dueday(self):
        return self.due[8:]
    
    @property
    def duemonth(self):
        return self.due[5:7]
    
    @property
    def dueyear(self):
        return self.due[:4]
        
        

