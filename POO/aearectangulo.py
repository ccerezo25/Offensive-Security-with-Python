class Rectangulo():
    def __init__(self,base,altura):
        self.__base = base 
        self.__altura = altura 
    
    @property
    def modificar(self):
        return f"su resultado es:{self.__base*self.__altura}"
    
    @property
    def base(self):
        pass

    @base.setter
    def base (self,base):
        self.__base = base

    @property
    def altura(self):
        pass
    
    @altura.setter
    def altura(self,altura):
        self.__altura = altura

Rc=Rectangulo(5,10)
Rc.base = 8
Rc.altura = 6
print(Rc.modificar)
        

    
   
    