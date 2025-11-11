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
        4,1,23,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,5,6,62,8,6,10,6,12,6,65,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,
        1,7,3,7,75,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,
        7,89,8,7,10,7,12,7,92,9,7,1,7,0,1,14,8,0,2,4,6,8,10,12,14,0,4,1,
        0,10,11,1,0,12,13,1,0,14,17,1,0,18,19,95,0,21,1,0,0,0,2,30,1,0,0,
        0,4,32,1,0,0,0,6,36,1,0,0,0,8,41,1,0,0,0,10,47,1,0,0,0,12,57,1,0,
        0,0,14,74,1,0,0,0,16,17,3,2,1,0,17,18,5,21,0,0,18,20,1,0,0,0,19,
        16,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,
        0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,31,3,4,2,0,27,31,3,
        6,3,0,28,31,3,8,4,0,29,31,3,10,5,0,30,26,1,0,0,0,30,27,1,0,0,0,30,
        28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,5,20,0,0,33,34,5,1,0,
        0,34,35,3,14,7,0,35,5,1,0,0,0,36,37,5,2,0,0,37,38,5,3,0,0,38,39,
        3,14,7,0,39,40,5,4,0,0,40,7,1,0,0,0,41,42,5,5,0,0,42,43,5,3,0,0,
        43,44,3,14,7,0,44,45,5,4,0,0,45,46,3,12,6,0,46,9,1,0,0,0,47,48,5,
        6,0,0,48,49,5,3,0,0,49,50,3,4,2,0,50,51,5,7,0,0,51,52,3,14,7,0,52,
        53,5,7,0,0,53,54,3,4,2,0,54,55,5,4,0,0,55,56,3,12,6,0,56,11,1,0,
        0,0,57,63,5,8,0,0,58,59,3,2,1,0,59,60,5,21,0,0,60,62,1,0,0,0,61,
        58,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,
        0,65,63,1,0,0,0,66,67,5,9,0,0,67,13,1,0,0,0,68,69,6,7,-1,0,69,75,
        5,20,0,0,70,71,5,3,0,0,71,72,3,14,7,0,72,73,5,4,0,0,73,75,1,0,0,
        0,74,68,1,0,0,0,74,70,1,0,0,0,75,90,1,0,0,0,76,77,10,6,0,0,77,78,
        7,0,0,0,78,89,3,14,7,7,79,80,10,5,0,0,80,81,7,1,0,0,81,89,3,14,7,
        6,82,83,10,4,0,0,83,84,7,2,0,0,84,89,3,14,7,5,85,86,10,3,0,0,86,
        87,7,3,0,0,87,89,3,14,7,4,88,76,1,0,0,0,88,79,1,0,0,0,88,82,1,0,
        0,0,88,85,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,15,
        1,0,0,0,92,90,1,0,0,0,6,21,30,63,74,88,90
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'print'", "'('", "')'", "'if'", 
                     "'for'", "':'", "'{'", "'}'", "'*'", "'/'", "'+'", 
                     "'-'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NEWLINE", "WS", "SEMI" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assign = 2
    RULE_print = 3
    RULE_if_statement = 4
    RULE_for_statement = 5
    RULE_block = 6
    RULE_expr = 7

    ruleNames =  [ "program", "statement", "assign", "print", "if_statement", 
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
    ID=20
    NEWLINE=21
    WS=22
    SEMI=23

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048676) != 0):
                self.state = 16
                self.statement()
                self.state = 17
                self.match(GrammarParser.NEWLINE)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
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

        def assign(self):
            return self.getTypedRuleContext(GrammarParser.AssignContext,0)


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
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.assign()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.print_()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.if_statement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
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


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = GrammarParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(GrammarParser.ID)
            self.state = 33
            self.match(GrammarParser.T__0)
            self.state = 34
            self.expr(0)
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
        self.enterRule(localctx, 6, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(GrammarParser.T__1)
            self.state = 37
            self.match(GrammarParser.T__2)
            self.state = 38
            self.expr(0)
            self.state = 39
            self.match(GrammarParser.T__3)
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
        self.enterRule(localctx, 8, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(GrammarParser.T__4)
            self.state = 42
            self.match(GrammarParser.T__2)
            self.state = 43
            self.expr(0)
            self.state = 44
            self.match(GrammarParser.T__3)
            self.state = 45
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

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.AssignContext)
            else:
                return self.getTypedRuleContext(GrammarParser.AssignContext,i)


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
        self.enterRule(localctx, 10, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(GrammarParser.T__5)
            self.state = 48
            self.match(GrammarParser.T__2)
            self.state = 49
            self.assign()
            self.state = 50
            self.match(GrammarParser.T__6)
            self.state = 51
            self.expr(0)
            self.state = 52
            self.match(GrammarParser.T__6)
            self.state = 53
            self.assign()
            self.state = 54
            self.match(GrammarParser.T__3)
            self.state = 55
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
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(GrammarParser.T__7)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048676) != 0):
                self.state = 58
                self.statement()
                self.state = 59
                self.match(GrammarParser.NEWLINE)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(GrammarParser.T__8)
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 69
                self.match(GrammarParser.ID)
                pass
            elif token in [3]:
                self.state = 70
                self.match(GrammarParser.T__2)
                self.state = 71
                self.expr(0)
                self.state = 72
                self.match(GrammarParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 88
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 76
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 77
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 78
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 79
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 80
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 81
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 82
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 83
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 84
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 86
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.expr(4)
                        pass

             
                self.state = 92
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
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




