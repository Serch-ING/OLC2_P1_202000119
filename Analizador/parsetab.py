
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMAYORIGUALMAYORMENORIGUALMENORleftSUMARESTAleftMULTIDIVIleftMODULOrightPOWFPOWABS AND AS BARRA BREAK CADENA CAPACITY CARACTER CD CI CLONE COMA CONTAINS CONTINUE DESIGUALDAD DIRSTRING DIVI DP ELSE ENTERO ERR FALSE FLOAT FOR FUNCION GBAJO ID IF IGUAL IGUALDAD IN INSERT LD LEN LET LI LOOP MAIN MATCH MAYOR MAYORIGUAL MENOR MENORIGUAL MOD MODULO MULTI MUT NEW NOT OR PD PI POW POWF PRINT PRINTLN PUBLICO PUNTO PUSH PYC REFER REMOVE RESTA RETURN SQRT STRUCT SUMA TIPOBOOL TIPOCHAR TIPOFLOAT TIPOINT TIPOSTRING TOOWNED TOSTRING TRUE VECT VECTOR WCAPACITY WHILEinit            : instruccionesinstrucciones    : instrucciones instruccion\n                        | instruccioninstruccion      : impresionesimpresiones     : PRINTLN PI CADENA PD PYC\n                       | PRINT PI CADENA PD PYC\n                       | PRINTLN PI CADENA COMA impresion_valores PD PYC\n                       | PRINT PI CADENA COMA  impresion_valores PD PYCimpresion_valores     :  impresion_valores COMA expresiones\n                         | expresiones expresiones  :\n                    | expresiones SUMA expresiones\n                    | expresiones RESTA expresiones\n                    | expresiones MULTI expresiones\n                    | expresiones DIVI expresiones\n                    | expresiones MODULO expresiones\n                    | POWF PI expresiones COMA expresiones PD\n                    | POW PI expresiones COMA expresiones PD\n                    | expresiones MAYORIGUAL expresiones\n                    | expresiones MAYOR expresiones\n                    | expresiones MENORIGUAL expresiones\n                    | expresiones MENOR expresiones\n                    | ID\n                    | ENTERO\n                    | FLOAT\n                    | CADENA'
    
_lr_action_items = {'PRINTLN':([0,2,3,4,7,16,25,42,54,],[5,5,-3,-4,-2,-5,-6,-7,-8,]),'PRINT':([0,2,3,4,7,16,25,42,54,],[6,6,-3,-4,-2,-5,-6,-7,-8,]),'$end':([1,2,3,4,7,16,25,42,54,],[0,-1,-3,-4,-2,-5,-6,-7,-8,]),'PI':([5,6,20,21,],[8,9,38,39,]),'CADENA':([8,9,13,15,27,29,30,31,32,33,34,35,36,37,38,39,55,56,],[10,11,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'PD':([10,11,13,15,17,18,19,22,23,24,26,27,29,30,31,32,33,34,35,36,37,41,43,44,45,46,47,48,49,50,51,55,56,57,58,59,60,],[12,14,-11,-11,-26,28,-10,-23,-24,-25,40,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-9,-12,-13,-14,-15,-16,-19,-20,-21,-22,-11,-11,59,60,-17,-18,]),'COMA':([10,11,13,15,17,18,19,22,23,24,26,27,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,59,60,],[13,15,-11,-11,-26,27,-10,-23,-24,-25,27,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-9,-12,-13,-14,-15,-16,-19,-20,-21,-22,55,56,-17,-18,]),'PYC':([12,14,28,40,],[16,25,42,54,]),'SUMA':([13,15,17,19,22,23,24,27,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,],[-11,-11,-26,29,-23,-24,-25,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,29,-12,-13,-14,-15,-16,29,29,29,29,29,29,-11,-11,29,29,-17,-18,]),'RESTA':([13,15,17,19,22,23,24,27,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,],[-11,-11,-26,30,-23,-24,-25,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,30,-12,-13,-14,-15,-16,30,30,30,30,30,30,-11,-11,30,30,-17,-18,]),'MULTI':([13,15,17,19,22,23,24,27,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,],[-11,-11,-26,31,-23,-24,-25,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,31,31,31,-14,-15,-16,31,31,31,31,31,31,-11,-11,31,31,-17,-18,]),'DIVI':([13,15,17,19,22,23,24,27,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,],[-11,-11,-26,32,-23,-24,-25,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,32,32,32,-14,-15,-16,32,32,32,32,32,32,-11,-11,32,32,-17,-18,]),'MODULO':([13,15,17,19,22,23,24,27,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,],[-11,-11,-26,33,-23,-24,-25,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,33,33,33,33,33,-16,33,33,33,33,33,33,-11,-11,33,33,-17,-18,]),'MAYORIGUAL':([13,15,17,19,22,23,24,27,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,],[-11,-11,-26,34,-23,-24,-25,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,34,-12,-13,-14,-15,-16,-19,-20,-21,-22,34,34,-11,-11,34,34,-17,-18,]),'MAYOR':([13,15,17,19,22,23,24,27,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,],[-11,-11,-26,35,-23,-24,-25,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,35,-12,-13,-14,-15,-16,-19,-20,-21,-22,35,35,-11,-11,35,35,-17,-18,]),'MENORIGUAL':([13,15,17,19,22,23,24,27,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,],[-11,-11,-26,36,-23,-24,-25,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,36,-12,-13,-14,-15,-16,-19,-20,-21,-22,36,36,-11,-11,36,36,-17,-18,]),'MENOR':([13,15,17,19,22,23,24,27,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,],[-11,-11,-26,37,-23,-24,-25,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,37,-12,-13,-14,-15,-16,-19,-20,-21,-22,37,37,-11,-11,37,37,-17,-18,]),'POWF':([13,15,27,29,30,31,32,33,34,35,36,37,38,39,55,56,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'POW':([13,15,27,29,30,31,32,33,34,35,36,37,38,39,55,56,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'ID':([13,15,27,29,30,31,32,33,34,35,36,37,38,39,55,56,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'ENTERO':([13,15,27,29,30,31,32,33,34,35,36,37,38,39,55,56,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'FLOAT':([13,15,27,29,30,31,32,33,34,35,36,37,38,39,55,56,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,7,]),'impresiones':([0,2,],[4,4,]),'impresion_valores':([13,15,],[18,26,]),'expresiones':([13,15,27,29,30,31,32,33,34,35,36,37,38,39,55,56,],[19,19,41,43,44,45,46,47,48,49,50,51,52,53,57,58,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','Gramatica.py',248),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','Gramatica.py',253),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','Gramatica.py',254),
  ('instruccion -> impresiones','instruccion',1,'p_instruccion','Gramatica.py',266),
  ('impresiones -> PRINTLN PI CADENA PD PYC','impresiones',5,'p_instruccion_imprimir','Gramatica.py',275),
  ('impresiones -> PRINT PI CADENA PD PYC','impresiones',5,'p_instruccion_imprimir','Gramatica.py',276),
  ('impresiones -> PRINTLN PI CADENA COMA impresion_valores PD PYC','impresiones',7,'p_instruccion_imprimir','Gramatica.py',277),
  ('impresiones -> PRINT PI CADENA COMA impresion_valores PD PYC','impresiones',7,'p_instruccion_imprimir','Gramatica.py',278),
  ('impresion_valores -> impresion_valores COMA expresiones','impresion_valores',3,'p_imprimir_lista_valores','Gramatica.py',308),
  ('impresion_valores -> expresiones','impresion_valores',1,'p_imprimir_lista_valores','Gramatica.py',309),
  ('expresiones -> <empty>','expresiones',0,'p_expresiones','Gramatica.py',321),
  ('expresiones -> expresiones SUMA expresiones','expresiones',3,'p_expresiones','Gramatica.py',322),
  ('expresiones -> expresiones RESTA expresiones','expresiones',3,'p_expresiones','Gramatica.py',323),
  ('expresiones -> expresiones MULTI expresiones','expresiones',3,'p_expresiones','Gramatica.py',324),
  ('expresiones -> expresiones DIVI expresiones','expresiones',3,'p_expresiones','Gramatica.py',325),
  ('expresiones -> expresiones MODULO expresiones','expresiones',3,'p_expresiones','Gramatica.py',326),
  ('expresiones -> POWF PI expresiones COMA expresiones PD','expresiones',6,'p_expresiones','Gramatica.py',327),
  ('expresiones -> POW PI expresiones COMA expresiones PD','expresiones',6,'p_expresiones','Gramatica.py',328),
  ('expresiones -> expresiones MAYORIGUAL expresiones','expresiones',3,'p_expresiones','Gramatica.py',329),
  ('expresiones -> expresiones MAYOR expresiones','expresiones',3,'p_expresiones','Gramatica.py',330),
  ('expresiones -> expresiones MENORIGUAL expresiones','expresiones',3,'p_expresiones','Gramatica.py',331),
  ('expresiones -> expresiones MENOR expresiones','expresiones',3,'p_expresiones','Gramatica.py',332),
  ('expresiones -> ID','expresiones',1,'p_expresiones','Gramatica.py',333),
  ('expresiones -> ENTERO','expresiones',1,'p_expresiones','Gramatica.py',334),
  ('expresiones -> FLOAT','expresiones',1,'p_expresiones','Gramatica.py',335),
  ('expresiones -> CADENA','expresiones',1,'p_expresiones','Gramatica.py',336),
]
