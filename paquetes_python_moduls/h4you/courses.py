class Course: 
    def __init__(self,name,duration,link):
        self.name= name
        self.duration = duration
        self.link = link
    def __repr__(self):
        return f"{self.name} [{self.duration} horas] ({self.link})"

courses = [
    Course("Introducion a linux",15,"https://hack4u.io/cursos/introduccion-a-linux/"),
    Course("Personalizacion a linux",3,"https://hack4u.io/cursos/perzonalizacion-de-entorno-linux/"),
    Course("Introducion al hacking",53,"https://hack4u.io/cursos/introduccion-al-hacking/")
]

#print(Courses)

def list_course():
    for course in courses:
        print(course)