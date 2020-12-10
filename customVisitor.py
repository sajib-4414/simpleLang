# Generated from simpleLang.g4 by ANTLR 4.9.2
from antlr4 import *
from simpleLangVisitor import simpleLangVisitor
import logging

# This class defines a complete visitor class also called as a walker
#for a parse tree produced by simpleLangParser.


memory = {}

class customVisitor(simpleLangVisitor):

    # Visit a the main programs parse tree
    def visitProgram(self, ctx):
        logging.debug("program")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by main_function.
    def visitMain_function(self, ctx):
        logging.debug("main_function")
        return self.visitChildren(ctx)


    # walker method for visiting statements parse tree
    def visitStatements(self, ctx):
        logging.debug("statements")
        return self.visitChildren(ctx)


    # visitor method for each statement
    def visitStatement(self, ctx):
        logging.debug("statement")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#print_stmt.
    def visitPrint_stmt(self, ctx):
        logging.debug("print_stmt")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#print_sconst_stmt.
    def visitPrint_sconst_stmt(self, ctx):
        logging.debug("print_sconst_stmt")
        print(ctx.children[1].symbol.text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#print_var_stmt.
    def visitPrint_var_stmt(self, ctx):
        logging.debug("print_var_stmt")
        print(memory[ctx.children[1].symbol.text])
        return self.visitChildren(ctx)
    
    
    # Visit a parse tree produced by simpleLangParser#var_decl_stmt.
    def visitVar_decl_stmt(self, ctx):
        logging.debug("var_decl_stmt")
        var = self.visit(ctx.children[3])
        memory[ctx.children[1].symbol.text] = var
        return self.visitChildren(ctx)
        

    # Visit a parse tree produced by simpleLangParser#var_assign_stmt.
    def visitVar_assign_stmt(self, ctx): 
        key = ctx.children[1].symbol.text
        value = self.visit(ctx.children[3])
        func = self.visit(ctx.children[4])
        memory[key] = func(value)       
        logging.debug("var_assign_stmt -> " + str(key) + " = " + str(func(value)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#ifelseendif.
    def visitIfelseendif(self, ctx):
        logging.debug("ifElseEndif")
        if self.visit(ctx.children[1]) == 1:
            return self.visit(ctx.children[2])
        else:
            return self.visit(ctx.children[4])


    # Visit a parse tree produced by simpleLangParser#ifendid.
    def visitIfendid(self, ctx):
        logging.debug("ifEndif")
        if self.visit(ctx.children[1]) == 1:
            return self.visit(ctx.children[2])
            
    # Visit a parse tree produced by simpleLangParser#while_stmt.
    def visitWhile_stmt(self, ctx):   
        logging.debug("while_stmt")
        while self.visit(ctx.children[1]) == 1:
            self.visit(ctx.children[2])

    ##################################
    # Parsing expressions
    ##################################


    # Visit a parse tree produced by simpleLangParser#varexpr.
    def visitVarexpr(self, ctx):
        return memory[ctx.children[0].symbol.text]


    # Visit a parse tree produced by simpleLangParser#numberexpr.
    def visitNumberexpr(self, ctx):
        return int(ctx.children[0].symbol.text)


    # Visit a parse tree produced by simpleLangParser#trueexpr.
    def visitTrueexpr(self, ctx):
        return 1


    # Visit a parse tree produced by simpleLangParser#falseexpr.
    def visitFalseexpr(self, ctx):
        return 0
    
    ##################################
    # Operations
    ##################################
        
    # Visit a parse tree produced by simpleLangParser#operations.
    def visitOperations(self, ctx):
        if len(ctx.children) > 1:
            func = self.visit(ctx.children[0])
            op = self.visit(ctx.children[1])
            return lambda x:op(func(x))
        else:
            op = self.visit(ctx.children[0])
            return op


    # Visit a parse tree produced by simpleLangParser#plusop.
    def visitPlusop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:x+var


    # Visit a parse tree produced by simpleLangParser#minusop.
    def visitMinusop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:x-var


    # Visit a parse tree produced by simpleLangParser#multiplicationop.
    def visitMultiplicationop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:x*var


    # Visit a parse tree produced by simpleLangParser#divisionop.
    def visitDivisionop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:x/var

    # Visit a parse tree produced by simpleLangParser#equalop.
    def visitEqualop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:1 if x==var else 0

    # Visit a parse tree produced by simpleLangParser#greaterop.
    def visitGreaterop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:1 if x>var else 0


    # Visit a parse tree produced by simpleLangParser#orop.
    def visitOrop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:0 if x==var and x == 0 else 1


    # Visit a parse tree produced by simpleLangParser#andop.
    def visitAndop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:1 if x != 0 and var!= 0 else 0
