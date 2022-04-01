# Creati o clasa Student cu 2 atribute, un nume si o nota.
# Instantiati cele 2 fielduri prin intermediul constructorului.
# a) Scrieti 2 functii pentru nota: get_grade care sa returneze nota studentului si set_grade care sa ii modifice nota.
# Asigurativa ca e si logic, nu doar ca functioneaza:)!
# b) Scrieti o functie care sa descrie elevul: "The student`s name is .... and has the grade ..."
# c) Creati o lista de studenti primita ca input de la tastatura; dupa ce ati construit-o, afisati descrierea fiecarui student
# d) Filtrati lista de studenti (sau construiti una noua) astfel incat sa ramana doar acei studenti care au o nota de trecere:
# de preferat determinati daca studentul are nota de trecere sau nu folosindu`va de o alta functie a clasei Student

class Student:
    def __init__(self,nume,nota):
       self.nume = nume
       self.nota = nota

    def get_grade(self):
        return self.nota

    def set_grade(self,nota_noua):
        verificare = True
        while verificare:
            try:
                nota_noua = int(nota_noua)
                assert nota_noua >= 0 and nota_noua <= 10

            except:
                print('Invalid option')
                nota_noua = input('Introduceti noua nota : ')

            else:
                verificare = False
                self.nota = nota_noua

    def student_profile(self):
        print(f'The student`s name is {self.nume} and has the grade {self.nota}!')

list_of_student = []
while True:

    student_name = input('Student name :')
    if student_name == 'Stop':
        break

    student_nota = int(input('Nota Studentulu :'))
    student1=Student(student_name,student_nota)
    list_of_student.append(student1)



for elem in list_of_student:
    elem.student_profile()


pass_student = []
print('Elevi Admisi!')
for elem in list_of_student:
    if elem.get_grade() >= 5:
        pass_student.append(elem)
for elem in pass_student:
    elem.student_profile()




from  prettytable import PrettyTable

myTable = PrettyTable(['Student Name','Class','Section'])
myTable.add_row(['Bogdan','12','A'])
myTable.add_row(['Ancuta','12','A'])
myTable.add_row(['Cira','12','A'])
myTable.add_row(['Florina','12','A'])
myTable.add_row(['Mihai','12','A'])
myTable.add_autoindex('sr.No')
myTable.del_column('Class')


print(myTable)


