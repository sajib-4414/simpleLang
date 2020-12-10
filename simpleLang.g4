grammar simpleLang;

program
    : main_function
    ;
   
main_function
    : BEGINMAIN statements ENDMAIN
    | BEGINMAIN ENDMAIN
    ;
   
statements
    : statement*
    ;

statement
    : var_decl_stmt
    | var_assign_stmt
    | print_stmt
    | condition_stmt
    | while_stmt
    ;
 
print_stmt
    : print_var_stmt
    | print_sconst_stmt
    ;

print_sconst_stmt
    : PRINT STRING_LITERAL
    ;
    
print_var_stmt
    : PRINT IDENTIFIER
    ;

var_decl_stmt 
    : DECLAREINT IDENTIFIER SETINITIALVALUE expression 
    ;

condition_stmt
    : IF expression statements ELSE statements ENDIF #ifelseendif
    | IF expression statements ENDIF                 #ifendid
    ;
    
while_stmt
    : WHILE expression statements ENDWHILE
    ;
    
expression
    : IDENTIFIER #varexpr
    | NUMBER     #numberexpr
    | AT TRUE    #trueexpr
    | AT FALSE   #falseexpr
    ;

var_assign_stmt
    : ASSIGNVARIABLE IDENTIFIER SETVALUE expression operations ENDASSIGNVARIABLE
    ;
    
operations
    : operation | operations operation
    ;
    
operation
    : PLUSOPERATOR expression           #add operator operation
    | MINUSOPERATOR expression          #substract operator operation
    | MULTIPLICATIONOPERATOR expression #multiply operator operation
    | DIVISIONOPERATOR expression       #division operator operation
    | EQUALTO expression                #equal to condition
    | GREATERTHAN expression            #greater than condition
    | OR expression                     #or operation
    | AND expression                    #and operation
    ;


BEGINMAIN
    : 'start_program'
    ;
    
ENDMAIN
    : 'end_program'
    ;

AT
    : '@'
    ;
    
TRUE
    : 'bool_true'
    ;

FALSE
    : 'bool_false'
    ;
    
PLUSOPERATOR
    : 'add_val'
    ;
    
MINUSOPERATOR
    : 'subtract_val'
    ;
    
MULTIPLICATIONOPERATOR
    : 'mult_val'
    ;
    
DIVISIONOPERATOR
    : 'divide_val'
    ;
    
EQUALTO
    : 'equal_to'
    ;
    
GREATERTHAN
    : 'gt_than'
    ;

OR
    : 'or_condition'
    ;
    
AND
    : 'and_condition'
    ;

PRINT
    : 'print_val'
    ;

DECLAREINT
    : 'declare_intvar'
    ;
    
SETINITIALVALUE
    : 'initialize_var'
    ;
    
ASSIGNVARIABLE
    : 'assign_var'
    ;

SETVALUE
    : 'set_var_val'
    ;
    
ENDASSIGNVARIABLE
    : 'end_assignment'
    ;
    
IF
    : 'if_condition'
    ;
    
ELSE
    : 'else_condition'
    ;
    
ENDIF
    : 'end_if_condition'
    ;
    
WHILE
    : 'while_condition'
    ;
    
ENDWHILE
    : 'end_while_condition'
    ;
    
IDENTIFIER
    : [a-zA-Z]+
    ;

NUMBER
    : DIGIT+
    ;

    
STRING_LITERAL
 : ( SHORT_STRING | LONG_STRING )
 ;
   
WS 
    : [ \r\n\t]+ -> channel(HIDDEN)
    ;

/*
 * fragments
 */

fragment DIGIT
    : ('0'..'9')
    ;
 
fragment SHORT_STRING
 : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n'] )* '\''
 | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n"] )* '"'
 ;

fragment LONG_STRING
 : '\'\'\'' LONG_STRING_ITEM*? '\'\'\''
 | '"""' LONG_STRING_ITEM*? '"""'
 ;

fragment LONG_STRING_ITEM
 : LONG_STRING_CHAR
 | STRING_ESCAPE_SEQ
 ;

fragment LONG_STRING_CHAR
 : ~'\\'
 ;
 
fragment STRING_ESCAPE_SEQ
 : '\\' .
 ;