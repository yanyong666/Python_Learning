# coding= UTF-8

class SchoolMember:
    """代表学校里面任何成员"""
    def __init__(self, name , age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        """告诉我有关我自己的细节"""
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=" ")

class Teacher(SchoolMember):
    """代表每一位老师"""
    def __init__(self, name, age, salary):
        # 在这里你需要注意，当我们使用 SchoolMember 类的 tell 方法时，
        # 我们可以将 Teacher 或 Student 的实例看作 SchoolMember 的实例。
        #同时，你会发现被调用的是子类型的 tell 方法，而不是 SchoolMember 的 tell 方法。
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    # 重载父类方法
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生。'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    # 重载父类方法
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# 打印一行空白行
print()
members = [t,s]
for member in members:
    # 对全体师生工作
    member.tell()