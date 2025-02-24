class Cyber_cesar: 
    def __init__(self,pc,copiadora_ricoh,copiadora_epson,cortadora):
        self.pc = pc 
        self.copiadora_ricoh= copiadora_ricoh
        self.copiadora_epson=copiadora_epson
        self.cortadora=cortadora

    def enumerar(self):
        raise NotImplementedError("Hay que añadir este metodo")

class pc_gamer(Cyber_cesar):

    def enumerar(self):
        return f"esta es la pc: {self.pc}, aveces uso la cortadora{self.cortadora}"
        
class coiadora1(Cyber_cesar):

    def enumerar(self):
        return f"esta es la copiadora {self.copiadora_ricoh}"

class coiadora2(Cyber_cesar):

    def enumerar(self):
        return f"esta es la segunda copiador {self.copiadora_epson}"

class ncortadora(Cyber_cesar):

    def enumerar(self):
        return f"esta es la cortadora {self.cortadora}"
    
def llamada(i):
    print(i.enumerar())



#n1 = Cyber_cesar("asus","ricoh200","epson300","cortadora_artesco")
#pc_gamer.enumerar(n1)
n1=pc_gamer("pc1","ricoh","epson100","c .artesco")
n2=coiadora1("pc1","ricoh","epson100","c .artesco")
n3=coiadora2("pc1","ricoh","epson100","c .artesco")
n4=ncortadora("pc1","ricoh","epson100","c .artesco")
llamada(n1)
llamada(n2)
llamada(n3)
llamada(n4)


#ahra si quiero hacer metamorfismo para instaciar clases lo que debo de hacer es 
#primro instanciar clases 



