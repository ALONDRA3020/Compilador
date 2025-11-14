# Generated from Grammar.g by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,101,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,67,8,7,10,7,12,7,70,9,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,82,8,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,96,8,8,10,8,12,8,99,9,8,1,8,0,1,16,
        9,0,2,4,6,8,10,12,14,16,0,5,1,0,2,3,1,0,11,12,1,0,13,14,1,0,15,18,
        1,0,19,20,103,0,23,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,39,1,0,0,
        0,8,41,1,0,0,0,10,46,1,0,0,0,12,52,1,0,0,0,14,62,1,0,0,0,16,81,1,
        0,0,0,18,19,3,2,1,0,19,20,5,24,0,0,20,22,1,0,0,0,21,18,1,0,0,0,22,
        25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,
        0,26,27,5,0,0,1,27,1,1,0,0,0,28,33,3,4,2,0,29,33,3,8,4,0,30,33,3,
        10,5,0,31,33,3,12,6,0,32,28,1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,0,
        32,31,1,0,0,0,33,3,1,0,0,0,34,35,3,6,3,0,35,36,5,21,0,0,36,37,5,
        1,0,0,37,38,3,16,8,0,38,5,1,0,0,0,39,40,7,0,0,0,40,7,1,0,0,0,41,
        42,5,4,0,0,42,43,5,5,0,0,43,44,3,16,8,0,44,45,5,6,0,0,45,9,1,0,0,
        0,46,47,5,7,0,0,47,48,5,5,0,0,48,49,3,16,8,0,49,50,5,6,0,0,50,51,
        3,14,7,0,51,11,1,0,0,0,52,53,5,8,0,0,53,54,5,5,0,0,54,55,3,4,2,0,
        55,56,5,26,0,0,56,57,3,16,8,0,57,58,5,26,0,0,58,59,3,4,2,0,59,60,
        5,6,0,0,60,61,3,14,7,0,61,13,1,0,0,0,62,68,5,9,0,0,63,64,3,2,1,0,
        64,65,5,24,0,0,65,67,1,0,0,0,66,63,1,0,0,0,67,70,1,0,0,0,68,66,1,
        0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,72,5,10,0,0,72,
        15,1,0,0,0,73,74,6,8,-1,0,74,82,5,21,0,0,75,82,5,22,0,0,76,82,5,
        23,0,0,77,78,5,5,0,0,78,79,3,16,8,0,79,80,5,6,0,0,80,82,1,0,0,0,
        81,73,1,0,0,0,81,75,1,0,0,0,81,76,1,0,0,0,81,77,1,0,0,0,82,97,1,
        0,0,0,83,84,10,8,0,0,84,85,7,1,0,0,85,96,3,16,8,9,86,87,10,7,0,0,
        87,88,7,2,0,0,88,96,3,16,8,8,89,90,10,6,0,0,90,91,7,3,0,0,91,96,
        3,16,8,7,92,93,10,5,0,0,93,94,7,4,0,0,94,96,3,16,8,6,95,83,1,0,0,
        0,95,86,1,0,0,0,95,89,1,0,0,0,95,92,1,0,0,0,96,99,1,0,0,0,97,95,
        1,0,0,0,97,98,1,0,0,0,98,17,1,0,0,0,99,97,1,0,0,0,6,23,32,68,81,
        95,97
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'int'", "'string'", "'print'", 
                     "'('", "')'", "'if'", "'for'", "'{'", "'}'", "'*'", 
                     "'/'", "'+'", "'-'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "STRING", "NEWLINE", 
                      "WS", "SEMI" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assing = 2
    RULE_type = 3
    RULE_print = 4
    RULE_if_statement = 5
    RULE_for_statement = 6
    RULE_block = 7
    RULE_expr = 8

    ruleNames =  [ "program", "statement", "assing", "type", "print", "if_statement", 
                   "for_statement", "block", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    ID=21
    NUMBER=22
    STRING=23
    NEWLINE=24
    WS=25
    SEMI=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NEWLINE)
            else:
                return self.getToken(GrammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 412) != 0):
                self.state = 18
                self.statement()
                self.state = 19
                self.match(GrammarParser.NEWLINE)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assing(self):
            return self.getTypedRuleContext(GrammarParser.AssingContext,0)


        def print_(self):
            return self.getTypedRuleContext(GrammarParser.PrintContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(GrammarParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(GrammarParser.For_statementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.assing()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.print_()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.if_statement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.for_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_assing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssing" ):
                listener.enterAssing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssing" ):
                listener.exitAssing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssing" ):
                return visitor.visitAssing(self)
            else:
                return visitor.visitChildren(self)




    def assing(self):

        localctx = GrammarParser.AssingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.type_()
            self.state = 35
            self.match(GrammarParser.ID)
            self.state = 36
            self.match(GrammarParser.T__0)
            self.state = 37
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = GrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = GrammarParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(GrammarParser.T__3)
            self.state = 42
            self.match(GrammarParser.T__4)
            self.state = 43
            self.expr(0)
            self.state = 44
            self.match(GrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = GrammarParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(GrammarParser.T__6)
            self.state = 47
            self.match(GrammarParser.T__4)
            self.state = 48
            self.expr(0)
            self.state = 49
            self.match(GrammarParser.T__5)
            self.state = 50
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assing(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.AssingContext)
            else:
                return self.getTypedRuleContext(GrammarParser.AssingContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMI)
            else:
                return self.getToken(GrammarParser.SEMI, i)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = GrammarParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(GrammarParser.T__7)
            self.state = 53
            self.match(GrammarParser.T__4)
            self.state = 54
            self.assing()
            self.state = 55
            self.match(GrammarParser.SEMI)
            self.state = 56
            self.expr(0)
            self.state = 57
            self.match(GrammarParser.SEMI)
            self.state = 58
            self.assing()
            self.state = 59
            self.match(GrammarParser.T__5)
            self.state = 60
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NEWLINE)
            else:
                return self.getToken(GrammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = GrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(GrammarParser.T__8)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 412) != 0):
                self.state = 63
                self.statement()
                self.state = 64
                self.match(GrammarParser.NEWLINE)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(GrammarParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 74
                self.match(GrammarParser.ID)
                pass
            elif token in [22]:
                self.state = 75
                self.match(GrammarParser.NUMBER)
                pass
            elif token in [23]:
                self.state = 76
                self.match(GrammarParser.STRING)
                pass
            elif token in [5]:
                self.state = 77
                self.match(GrammarParser.T__4)
                self.state = 78
                self.expr(0)
                self.state = 79
                self.match(GrammarParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 95
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 84
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 85
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 87
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 88
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 90
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 92
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 93
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 94
                        self.expr(6)
                        pass

             
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




