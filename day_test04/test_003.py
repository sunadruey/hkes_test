class Person:
    # //类变量
    name="default"
    age=0
    gender='male'
    weight=0

    def __init__(self,name,age,gender):
        # //实例变量
        print("FUNCTION")
        self.name = name
        self.age = age
        self.gender = gender

    def set_name(self,name):
        self.name=name
        # self.name  实例的name值

    def eat(self):
        print('eationg')

    @classmethod
    def play(self):
        print("playing")

        # //类方法是不能访问的实例方法  Person.play()



zs=Person()
lisi=Person('lisi',13,'female')
print(zs.name)

