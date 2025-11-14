grammar Grammar;

program: (statement NEWLINE)* EOF;

statement: assing | print | if_statement | for_statement;



/* Definimos la asignacion con tipo*/
assing: type ID '=' expr;

/* Definimos los tipos */
type: 'int' | 'string';

/* Definimos print */
print:'print' '('expr')';

/* Definimos if */
if_statement: 'if' '('expr')' block;

/* Definimos for */
for_statement: 'for' '('assing';'expr';'assing')' block;

/* Definimos block */
block:'{'(statement NEWLINE)*'}';

/* Definimos expr */
expr: expr op=('*'|'/') expr
        | expr op=('+'|'-') expr
        | expr op=('>'|'<'|'>='|'<=') expr
        | expr op=('=='|'!=') expr
        | ID 
        /* Definicion de valores numericos  */
        | NUMBER
        /* Agregamos string a la expresion */
        | STRING
        | '('expr')'
        ;

/*Definicion de elementos finales*/
ID:[a-zA-Z][a-zA-Z_0-9]*;

/*Agregamos reglas para los numeros */
NUMBER: [0-9]+;

/*Agregamos reglas para el string */
STRING: '"'(~[ "\r\n])*?'"';

NEWLINE: [\r\n];
WS: [\t] -> skip;
SEMI: ';' ;