from antlr4 import *
from simpleLangLexer import simpleLangLexer
from simpleLangParser import simpleLangParser
from customVisitor import customVisitor
import logging
import sys

def main():
    #tests/test_fail/test_syntax.simpleLang
    input = FileStream("tests/test_pass/test_syntax.simpleLang")
    lexer = simpleLangLexer(input)
    stream = CommonTokenStream(lexer)
    parser = simpleLangParser(stream)
    tree = parser.program()
    visitor = customVisitor()
    visitor.visit(tree)

 
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    main()