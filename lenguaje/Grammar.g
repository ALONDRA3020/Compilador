grammar Grammar;

program:(statement NEWLINE)*EOF;

statement:assing|print|if_statement|for_statement;
/*Definimos la asignación, una asignacion es igual a una expresion*/
assing: ID '='expr;

/*Definimos la expresión*/
print:'print''('expr')';

/*Definimos el if*/
if_statement:'if''('expr')'block;

/*Definimos for*/
for_statement:'for'('assign';'expr';'assign')'block;

/*Defoinir un bloque se imprimen todas las instrucciones y operaciones que se definieron*/
block:'{'(statement NEWLINE)*'}';

/*Definimos la expresión para saber si se esta cumpliendo con la función*/
expr:expr op=('*'|'/')expr /*Operación d emultiplicació y división*/
    |expr op=('+'|'-')expr
    |expr op=('>'|'<'|'>=|'>=')expr  /*Se definen la final los operadores de comparación*/
    |expr op=('=='|'!=')expr
    |ID
    |'('expr')'
    ;

/*Definición de elementos finales*/
ID:[a-zA-Z][a-zA-Z_0-9]*;
NEWLINE:[\r\n];
WS:[\t]->skip;
SEMI:';';
