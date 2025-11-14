from antlr4 import *
from lenguage.GrammarLexer import GrammarLexer
from lenguage.GrammarParser import GrammarParser
#import lenguage.GrammarLexer as GrammarLexer
#import lenguage.GrammarParser as GrammarParser
import traceback

import  io
import sys
#import lenguage.MyVisitor as MyVisitor
from lenguage.MyVisitor import MyVisitor

def run_code(code:str):
    input_stream=InputStream(code)
    lexer=GrammarLexer(input_stream)
    stream=CommonTokenStream(lexer)
    parser=GrammarParser(stream)
    tree=parser.program()

    # Capturan la salida 
    old_stdout=sys.stdout
    buf = io.StringIO()
    sys.stdout = buf
    
    try:
        #Creamos un objeto de nuestro visitor
        visitor = MyVisitor()
        #Visitamos el arbol con nuestro visitor
        visitor.visit(tree)
        # Capturamos la salida
        output = buf.getvalue()
        #Retornamos la salida de la operacion
        return output
    #Capturamos excepciones
    except Exception:
        tb = traceback.format_exc()
        return tb
    finally:
        sys.stdout = old_stdout

