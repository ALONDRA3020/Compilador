from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self_memory = {}
    
    #Definimos la asignación 
    def VisitAssign(self,ctx):
        #Se obtiene el id o nombre de la variable
        name=ctx.ID().getText()
        #Se obtiene el valor, ya sea un valor númerico o una expresión
        value=self.visit(ctx.expr())
        #Se almacena en memoria a parti del nombre y el valor
        self.memory[name]=value

    #Definimos la impresión
    def VisitPrint(self,ctx):
        #Definimos la expresión qe sea mostrar
        value=self.visit(ctx.expr())
        #Imprime el valor
        print(value)