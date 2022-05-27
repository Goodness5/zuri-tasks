class Student():
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    def say_hi(self):
        print(" my name is ", + self.name )
std1 = Student("bob", 26, "Frontend", 25.55)
print(std1.__dict__)


std1.name = "peter"
std1.age = 34
std1.tracks = "UI/UX"

print(std1.name)
print(std1.age)
print(std1.tracks)


#h = Student('bob', 26, "FE", 25.55)
#h.say_hi

    #def change(self, name):


#print(Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
