from antlr4 import *
from lenguaje.GrammarLexer import GrammarLexer
from lenguaje.GrammarParser import GrammarParser
from lenguaje.MyVisitor import MyVisitor

import io
import sys


def run_code(code:str):
    #Captura instrucciones
    input_stream=InputStream(code)
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    Parser = GrammarParser(stream)
    tree = Parser.program()

    #Captura la salida de sus instrucciones
    old_stdout = sys.stdout()
    buf = io.StringIO()
    sys.stdout = buf

    #Creamos un objeto de nuestro visitor
    visitor = MyVisitor()
    #Visitamos el arbol con nuestro bisitor
    visitor.visit(tree)
    #Capturamos la salida
    output=buf.getvalue()
    return output
