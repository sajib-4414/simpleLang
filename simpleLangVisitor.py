# Generated from simpleLang.g4 by ANTLR 4.9
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by simpleLangParser.

class simpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by simpleLangParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#main_function.
    def visitMain_function(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#statements.
    def visitStatements(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#print_stmt.
    def visitPrint_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#print_sconst_stmt.
    def visitPrint_sconst_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#print_var_stmt.
    def visitPrint_var_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#var_decl_stmt.
    def visitVar_decl_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#ifelseendif.
    def visitIfelseendif(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#ifendid.
    def visitIfendid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#while_stmt.
    def visitWhile_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#varexpr.
    def visitVarexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#numberexpr.
    def visitNumberexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#trueexpr.
    def visitTrueexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#falseexpr.
    def visitFalseexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#var_assign_stmt.
    def visitVar_assign_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#operations.
    def visitOperations(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#plusop.
    def visitPlusop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#minusop.
    def visitMinusop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#multiplicationop.
    def visitMultiplicationop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#divisionop.
    def visitDivisionop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#equalop.
    def visitEqualop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#greaterop.
    def visitGreaterop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#orop.
    def visitOrop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simpleLangParser#andop.
    def visitAndop(self, ctx):
        return self.visitChildren(ctx)


