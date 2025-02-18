class A:
    
    species = "Human"
    
    def __init__(self, first_name):
        self.first_name = first_name
    
    def __str__(self):
        return(f"Hi {self.first_name}, how are you doing today")
        
    def lang(self, language):
        self.language = language
        return(f'Hi my name is {self.first_name} and I speak in {self.language}')

obj1 = A("Mubassir")
print(obj1.first_name)
print(obj1)
print(obj1.__class__.species)
print(obj1.lang('English'))