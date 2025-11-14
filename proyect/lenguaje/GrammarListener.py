# Generated from Grammar.g by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#assing.
    def enterAssing(self, ctx:GrammarParser.AssingContext):
        pass

    # Exit a parse tree produced by GrammarParser#assing.
    def exitAssing(self, ctx:GrammarParser.AssingContext):
        pass


    # Enter a parse tree produced by GrammarParser#type.
    def enterType(self, ctx:GrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#type.
    def exitType(self, ctx:GrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#print.
    def enterPrint(self, ctx:GrammarParser.PrintContext):
        pass

    # Exit a parse tree produced by GrammarParser#print.
    def exitPrint(self, ctx:GrammarParser.PrintContext):
        pass


    # Enter a parse tree produced by GrammarParser#if_statement.
    def enterIf_statement(self, ctx:GrammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#if_statement.
    def exitIf_statement(self, ctx:GrammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by GrammarParser#for_statement.
    def enterFor_statement(self, ctx:GrammarParser.For_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#for_statement.
    def exitFor_statement(self, ctx:GrammarParser.For_statementContext):
        pass


    # Enter a parse tree produced by GrammarParser#block.
    def enterBlock(self, ctx:GrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by GrammarParser#block.
    def exitBlock(self, ctx:GrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by GrammarParser#expr.
    def enterExpr(self, ctx:GrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#expr.
    def exitExpr(self, ctx:GrammarParser.ExprContext):
        pass



del GrammarParser