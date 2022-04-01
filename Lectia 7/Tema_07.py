#ABSTRACTION
#Clasa abstracta FormaGeometrica
#Contine un field PI=3.14
#Contine o metoda abstracta aria
#Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’


from abc import ABC , abstractmethod

class FormaGeometrica(ABC):
    pi = 3.14

    def descriere(self):
        print('Cel mai probabil am colturi!')

    @abstractmethod
    def aria(self):
        pass


class Patrat(FormaGeometrica):

    def descriere(self):
        print('Cel mai probabil am colturi!')

    def aria(self):
        print(f'Aria Patrat = {self.__latura * self.__latura}')

    def __init__(self,latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este {self.__latura}')

    @latura.setter
    def latura(self,latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Deleter : Am sters latura')
        self.__latura = None


class Cerc(FormaGeometrica):
    def descriere(self):
        print('Cel mai probabil nu am colturi!')

    def aria(self):
        print(f'Aria cercului = {self.pi * self.__raza ** 2}')

    def __init__(self,raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter:raza este {self.__raza}')

    @raza.setter
    def raza(self,raza):
        print(f'Setter: Noua raza este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Deleter : Am sters raza')
        self.__raza = None



forma = Patrat(3)
forma.aria()
forma.latura = 5
forma.latura
forma.aria()
del forma.latura
forma.latura

raza = Cerc(2)
raza.descriere()
raza.aria()
raza.raza = 10
raza.raza