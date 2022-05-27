from unicodedata import name
class Student:
    
    # Class attributes
    name = ""
    age = 0
    tracks = []
    score = 0.0
    
    # Student class constructor
    def __init__(self, name, age, tracks, score):
        self.name = name 
        self.age = age
        self.tracks = tracks
        self.score = score
    
    # methods
    def change_name(self, n):
        self.name = n    # assign new value(function argument) to class attribute
        return print(self.name)
        
    def change_age(self, a):
        self.age = a # assign new value(function argument) to class attribute
        return print(int(self.age))    
    
    def add_track(self, t):
        self.tracks.append(t)   #add new value/element to track
        return print(self.tracks)
        
    def get_score(self):
        return print(self.score)  #return and print score
    


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Function calls with argument
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
