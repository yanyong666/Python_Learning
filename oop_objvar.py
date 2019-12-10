#codding = UTF-8

class Robot:
    """表示有一个带有名字的机器人"""
    population = 0
    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))

    # 当有人被创建时，机器人数量人口增加
        Robot.population +=1
    def __del__(self):
        """机器人挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are the still {:d} robots working.".format(Robot.population))

    def die(self):
        """机器人挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -=1

        if Robot.population ==0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are the still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候"""
        print("Greetings,my masters call me {}.".format(self.name))

    # @classmethod
    # def how_manny(cls):
    #     """打印当前的机器人数量"""
    #     print("we have {:d} robots.".format(cls.population))
    @staticmethod
    def how_manny():
        print("we have {:d} robots.".format(Robot.population))

droid1 = Robot("R1-D1")
droid1.say_hi()
Robot.how_manny()

droid2 = Robot("R2-D2")
droid2.say_hi()
Robot.how_manny()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")

droid1.die()
# 等价于
# del droid1
droid2.die()
# 等价于
# del droid2
Robot.how_manny()
