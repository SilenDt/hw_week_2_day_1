class Student:
    def __init__(self, name_of_student,name_of_cohort):
        self.cohort = name_of_cohort
        self.name = name_of_student 

    def talk(self):
        return "I can talk!"
    def say_favourite_language(self,language):
        return f"I love {language}"
