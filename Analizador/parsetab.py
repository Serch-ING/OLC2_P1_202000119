
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMAYORIGUALMAYORMENORIGUALMENORIGUALDADDESIGUALDADleftSUMARESTAleftMULTIDIVIleftMODULOrightPOWFPOWrightNOTUMENOSABS AND AS BARRA BREAK CADENA CAPACITY CARACTER CD CI CLONE COMA CONTAINS CONTINUE DESIGUALDAD DIRSTRING DIVI DP ELSE ENTERO ERR FALSE FLOAT FOR FUNCION GBAJO ID IF IGUAL IGUALDAD IN INSERT LD LEN LET LI LOOP MAIN MATCH MAYOR MAYORIGUAL MENOR MENORIGUAL MOD MODULO MULTI MUT NEW NOT OR PD PI POW POWF PRINT PRINTLN PUBLICO PUNTO PUSH PYC REFER REMOVE RESTA RETURN SQRT STRUCT SUMA TIPOBOOL TIPOCHAR TIPOFLOAT TIPOINT TIPOSTRING TOOWNED TOSTRING TRUE VECT VECTOR WCAPACITY WHILEinit            : instruccionesinstrucciones    : instrucciones instruccion\n                        | instruccioninstruccion      : impresiones\n                        | declaracion\n                        | asignacion\n                        | funcion funcion  : FUNCION MAIN PI PD LI instrucciones LD\n                |  FUNCION ID PI PD tipo_funcion LI instrucciones LD\n                |  FUNCION ID parametros PD tipo_funcion LI instrucciones LDparametros : acceso   : PUBLICO\n                |tipo_funcion : RESTA MAYOR tipo_datos\n                    | RESTA MAYOR VECTOR MENOR tipo_datos MAYOR\n                    |declaracion  : LET mutable ID tipado PYC\n                        | LET mutable ID tipado IGUAL expresiones PYCasignacion      : ID IGUAL expresiones PYC mutable      : MUT\n                        | tipado      : DP tipo_datos\n                        | tipo_datos     : TIPOINT\n                      | TIPOFLOAT\n                      | TIPOCHAR\n                      | TIPOSTRING\n                      | DIRSTRING\n                      | TIPOBOOL impresiones     : PRINTLN PI CADENA PD PYC\n                       | PRINT PI CADENA PD PYC\n                       | PRINTLN PI CADENA COMA impresion_valores PD PYC\n                       | PRINT PI CADENA COMA  impresion_valores PD PYCimpresion_valores     :  impresion_valores COMA expresiones\n                         | expresiones expresiones  : RESTA expresiones %prec UMENOS\n                    | expresiones SUMA expresiones\n                    | expresiones RESTA expresiones\n                    | expresiones MULTI expresiones\n                    | expresiones DIVI expresiones\n                    | expresiones MODULO expresiones\n                    | POWF PI expresiones COMA expresiones PD\n                    | POW PI expresiones COMA expresiones PD\n                    | expresiones MAYORIGUAL expresiones\n                    | expresiones MAYOR expresiones\n                    | expresiones MENORIGUAL expresiones\n                    | expresiones MENOR expresiones\n                    | expresiones IGUALDAD expresiones\n                    | expresiones DESIGUALDAD expresiones\n                    | PI expresiones PD\n                    | ID\n                    | ENTERO\n                    | ENTERO tipo_string\n                    | FLOAT\n                    | CADENA\n                    | TRUE\n                    | FALSEtipo_string      :  TOOWNED\n                        | TOSTRING'
    
_lr_action_items = {'PRINTLN':([0,2,3,4,5,6,7,13,44,66,69,71,94,104,105,107,109,110,111,114,115,118,121,123,],[8,8,-3,-4,-5,-6,-7,-2,-19,-30,-31,-17,8,8,8,8,-32,-33,-18,-8,8,8,-9,-10,]),'PRINT':([0,2,3,4,5,6,7,13,44,66,69,71,94,104,105,107,109,110,111,114,115,118,121,123,],[9,9,-3,-4,-5,-6,-7,-2,-19,-30,-31,-17,9,9,9,9,-32,-33,-18,-8,9,9,-9,-10,]),'LET':([0,2,3,4,5,6,7,13,44,66,69,71,94,104,105,107,109,110,111,114,115,118,121,123,],[10,10,-3,-4,-5,-6,-7,-2,-19,-30,-31,-17,10,10,10,10,-32,-33,-18,-8,10,10,-9,-10,]),'ID':([0,2,3,4,5,6,7,10,12,13,16,17,18,26,28,39,41,44,45,46,47,48,49,50,51,52,53,54,55,57,59,66,69,71,72,94,98,102,103,104,105,107,109,110,111,114,115,118,121,123,],[11,11,-3,-4,-5,-6,-7,-21,20,-2,23,-20,24,24,24,24,24,-19,24,24,24,24,24,24,24,24,24,24,24,24,24,-30,-31,-17,24,11,24,24,24,11,11,11,-32,-33,-18,-8,11,11,-9,-10,]),'FUNCION':([0,2,3,4,5,6,7,13,44,66,69,71,94,104,105,107,109,110,111,114,115,118,121,123,],[12,12,-3,-4,-5,-6,-7,-2,-19,-30,-31,-17,12,12,12,12,-32,-33,-18,-8,12,12,-9,-10,]),'$end':([1,2,3,4,5,6,7,13,44,66,69,71,109,110,111,114,121,123,],[0,-1,-3,-4,-5,-6,-7,-2,-19,-30,-31,-17,-32,-33,-18,-8,-9,-10,]),'LD':([3,4,5,6,7,13,44,66,69,71,104,109,110,111,114,115,118,121,123,],[-3,-4,-5,-6,-7,-2,-19,-30,-31,-17,114,-32,-33,-18,-8,121,123,-9,-10,]),'PI':([8,9,18,19,20,26,27,28,29,39,41,45,46,47,48,49,50,51,52,53,54,55,57,59,72,98,102,103,],[14,15,28,35,36,28,57,28,59,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'MUT':([10,],[17,]),'IGUAL':([11,23,42,73,74,75,76,77,78,79,],[18,-23,72,-22,-24,-25,-26,-27,-28,-29,]),'MAIN':([12,],[19,]),'CADENA':([14,15,18,26,28,39,41,45,46,47,48,49,50,51,52,53,54,55,57,59,72,98,102,103,],[21,22,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'RESTA':([18,24,25,26,28,30,31,32,33,34,39,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,65,68,72,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,101,102,103,108,112,113,119,120,],[26,-51,46,26,26,-52,-54,-55,-56,-57,26,26,26,26,26,26,26,26,26,26,26,26,26,-36,26,46,26,-53,-58,-59,96,96,46,26,-37,-38,-39,-40,-41,46,46,46,46,46,46,46,-50,46,26,46,26,26,46,46,46,-42,-43,]),'POWF':([18,26,28,39,41,45,46,47,48,49,50,51,52,53,54,55,57,59,72,98,102,103,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'POW':([18,26,28,39,41,45,46,47,48,49,50,51,52,53,54,55,57,59,72,98,102,103,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'ENTERO':([18,26,28,39,41,45,46,47,48,49,50,51,52,53,54,55,57,59,72,98,102,103,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'FLOAT':([18,26,28,39,41,45,46,47,48,49,50,51,52,53,54,55,57,59,72,98,102,103,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'TRUE':([18,26,28,39,41,45,46,47,48,49,50,51,52,53,54,55,57,59,72,98,102,103,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'FALSE':([18,26,28,39,41,45,46,47,48,49,50,51,52,53,54,55,57,59,72,98,102,103,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'PD':([20,21,22,24,30,31,32,33,34,35,36,37,56,58,60,61,62,67,68,70,80,81,82,83,84,85,86,87,88,89,90,92,108,112,113,119,120,],[-11,38,40,-51,-52,-54,-55,-56,-57,63,64,65,-36,92,-53,-58,-59,99,-35,100,-37,-38,-39,-40,-41,-44,-45,-46,-47,-48,-49,-50,-34,119,120,-42,-43,]),'COMA':([21,22,24,30,31,32,33,34,56,60,61,62,67,68,70,80,81,82,83,84,85,86,87,88,89,90,91,92,93,108,119,120,],[39,41,-51,-52,-54,-55,-56,-57,-36,-53,-58,-59,98,-35,98,-37,-38,-39,-40,-41,-44,-45,-46,-47,-48,-49,102,-50,103,-34,-42,-43,]),'DP':([23,],[43,]),'PYC':([23,24,25,30,31,32,33,34,38,40,42,56,60,61,62,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,99,100,101,119,120,],[-23,-51,44,-52,-54,-55,-56,-57,66,69,71,-36,-53,-58,-59,-22,-24,-25,-26,-27,-28,-29,-37,-38,-39,-40,-41,-44,-45,-46,-47,-48,-49,-50,109,110,111,-42,-43,]),'SUMA':([24,25,30,31,32,33,34,56,58,60,61,62,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,101,108,112,113,119,120,],[-51,45,-52,-54,-55,-56,-57,-36,45,-53,-58,-59,45,-37,-38,-39,-40,-41,45,45,45,45,45,45,45,-50,45,45,45,45,45,-42,-43,]),'MULTI':([24,25,30,31,32,33,34,56,58,60,61,62,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,101,108,112,113,119,120,],[-51,47,-52,-54,-55,-56,-57,-36,47,-53,-58,-59,47,47,47,-39,-40,-41,47,47,47,47,47,47,47,-50,47,47,47,47,47,-42,-43,]),'DIVI':([24,25,30,31,32,33,34,56,58,60,61,62,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,101,108,112,113,119,120,],[-51,48,-52,-54,-55,-56,-57,-36,48,-53,-58,-59,48,48,48,-39,-40,-41,48,48,48,48,48,48,48,-50,48,48,48,48,48,-42,-43,]),'MODULO':([24,25,30,31,32,33,34,56,58,60,61,62,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,101,108,112,113,119,120,],[-51,49,-52,-54,-55,-56,-57,-36,49,-53,-58,-59,49,49,49,49,49,-41,49,49,49,49,49,49,49,-50,49,49,49,49,49,-42,-43,]),'MAYORIGUAL':([24,25,30,31,32,33,34,56,58,60,61,62,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,101,108,112,113,119,120,],[-51,50,-52,-54,-55,-56,-57,-36,50,-53,-58,-59,50,-37,-38,-39,-40,-41,-44,-45,-46,-47,-48,-49,50,-50,50,50,50,50,50,-42,-43,]),'MAYOR':([24,25,30,31,32,33,34,56,58,60,61,62,68,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,101,108,112,113,119,120,124,],[-51,51,-52,-54,-55,-56,-57,-36,51,-53,-58,-59,51,-24,-25,-26,-27,-28,-29,-37,-38,-39,-40,-41,-44,-45,-46,-47,-48,-49,51,-50,51,106,51,51,51,51,-42,-43,125,]),'MENORIGUAL':([24,25,30,31,32,33,34,56,58,60,61,62,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,101,108,112,113,119,120,],[-51,52,-52,-54,-55,-56,-57,-36,52,-53,-58,-59,52,-37,-38,-39,-40,-41,-44,-45,-46,-47,-48,-49,52,-50,52,52,52,52,52,-42,-43,]),'MENOR':([24,25,30,31,32,33,34,56,58,60,61,62,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,101,108,112,113,117,119,120,],[-51,53,-52,-54,-55,-56,-57,-36,53,-53,-58,-59,53,-37,-38,-39,-40,-41,-44,-45,-46,-47,-48,-49,53,-50,53,53,53,53,53,122,-42,-43,]),'IGUALDAD':([24,25,30,31,32,33,34,56,58,60,61,62,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,101,108,112,113,119,120,],[-51,54,-52,-54,-55,-56,-57,-36,54,-53,-58,-59,54,-37,-38,-39,-40,-41,-44,-45,-46,-47,-48,-49,54,-50,54,54,54,54,54,-42,-43,]),'DESIGUALDAD':([24,25,30,31,32,33,34,56,58,60,61,62,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,101,108,112,113,119,120,],[-51,55,-52,-54,-55,-56,-57,-36,55,-53,-58,-59,55,-37,-38,-39,-40,-41,-44,-45,-46,-47,-48,-49,55,-50,55,55,55,55,55,-42,-43,]),'TOOWNED':([30,],[61,]),'TOSTRING':([30,],[62,]),'TIPOINT':([43,106,122,],[74,74,74,]),'TIPOFLOAT':([43,106,122,],[75,75,75,]),'TIPOCHAR':([43,106,122,],[76,76,76,]),'TIPOSTRING':([43,106,122,],[77,77,77,]),'DIRSTRING':([43,106,122,],[78,78,78,]),'TIPOBOOL':([43,106,122,],[79,79,79,]),'LI':([63,64,65,74,75,76,77,78,79,95,97,116,125,],[94,-16,-16,-24,-25,-26,-27,-28,-29,105,107,-14,-15,]),'VECTOR':([106,],[117,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,94,105,107,],[2,104,115,118,]),'instruccion':([0,2,94,104,105,107,115,118,],[3,13,3,13,3,3,13,13,]),'impresiones':([0,2,94,104,105,107,115,118,],[4,4,4,4,4,4,4,4,]),'declaracion':([0,2,94,104,105,107,115,118,],[5,5,5,5,5,5,5,5,]),'asignacion':([0,2,94,104,105,107,115,118,],[6,6,6,6,6,6,6,6,]),'funcion':([0,2,94,104,105,107,115,118,],[7,7,7,7,7,7,7,7,]),'mutable':([10,],[16,]),'expresiones':([18,26,28,39,41,45,46,47,48,49,50,51,52,53,54,55,57,59,72,98,102,103,],[25,56,58,68,68,80,81,82,83,84,85,86,87,88,89,90,91,93,101,108,112,113,]),'parametros':([20,],[37,]),'tipado':([23,],[42,]),'tipo_string':([30,],[60,]),'impresion_valores':([39,41,],[67,70,]),'tipo_datos':([43,106,122,],[73,116,124,]),'tipo_funcion':([64,65,],[95,97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','Gramatica.py',249),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','Gramatica.py',254),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','Gramatica.py',255),
  ('instruccion -> impresiones','instruccion',1,'p_instruccion','Gramatica.py',266),
  ('instruccion -> declaracion','instruccion',1,'p_instruccion','Gramatica.py',267),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','Gramatica.py',268),
  ('instruccion -> funcion','instruccion',1,'p_instruccion','Gramatica.py',269),
  ('funcion -> FUNCION MAIN PI PD LI instrucciones LD','funcion',7,'p_funciones','Gramatica.py',281),
  ('funcion -> FUNCION ID PI PD tipo_funcion LI instrucciones LD','funcion',8,'p_funciones','Gramatica.py',282),
  ('funcion -> FUNCION ID parametros PD tipo_funcion LI instrucciones LD','funcion',8,'p_funciones','Gramatica.py',283),
  ('parametros -> <empty>','parametros',0,'p_parametros','Gramatica.py',290),
  ('acceso -> PUBLICO','acceso',1,'p_accceso','Gramatica.py',294),
  ('acceso -> <empty>','acceso',0,'p_accceso','Gramatica.py',295),
  ('tipo_funcion -> RESTA MAYOR tipo_datos','tipo_funcion',3,'p_tipo_funcion','Gramatica.py',303),
  ('tipo_funcion -> RESTA MAYOR VECTOR MENOR tipo_datos MAYOR','tipo_funcion',6,'p_tipo_funcion','Gramatica.py',304),
  ('tipo_funcion -> <empty>','tipo_funcion',0,'p_tipo_funcion','Gramatica.py',305),
  ('declaracion -> LET mutable ID tipado PYC','declaracion',5,'p_declaracion','Gramatica.py',314),
  ('declaracion -> LET mutable ID tipado IGUAL expresiones PYC','declaracion',7,'p_declaracion','Gramatica.py',315),
  ('asignacion -> ID IGUAL expresiones PYC','asignacion',4,'p_asignacio','Gramatica.py',325),
  ('mutable -> MUT','mutable',1,'p_mutable','Gramatica.py',331),
  ('mutable -> <empty>','mutable',0,'p_mutable','Gramatica.py',332),
  ('tipado -> DP tipo_datos','tipado',2,'p_tipado','Gramatica.py',341),
  ('tipado -> <empty>','tipado',0,'p_tipado','Gramatica.py',342),
  ('tipo_datos -> TIPOINT','tipo_datos',1,'p_tipo_datos','Gramatica.py',350),
  ('tipo_datos -> TIPOFLOAT','tipo_datos',1,'p_tipo_datos','Gramatica.py',351),
  ('tipo_datos -> TIPOCHAR','tipo_datos',1,'p_tipo_datos','Gramatica.py',352),
  ('tipo_datos -> TIPOSTRING','tipo_datos',1,'p_tipo_datos','Gramatica.py',353),
  ('tipo_datos -> DIRSTRING','tipo_datos',1,'p_tipo_datos','Gramatica.py',354),
  ('tipo_datos -> TIPOBOOL','tipo_datos',1,'p_tipo_datos','Gramatica.py',355),
  ('impresiones -> PRINTLN PI CADENA PD PYC','impresiones',5,'p_instruccion_imprimir','Gramatica.py',377),
  ('impresiones -> PRINT PI CADENA PD PYC','impresiones',5,'p_instruccion_imprimir','Gramatica.py',378),
  ('impresiones -> PRINTLN PI CADENA COMA impresion_valores PD PYC','impresiones',7,'p_instruccion_imprimir','Gramatica.py',379),
  ('impresiones -> PRINT PI CADENA COMA impresion_valores PD PYC','impresiones',7,'p_instruccion_imprimir','Gramatica.py',380),
  ('impresion_valores -> impresion_valores COMA expresiones','impresion_valores',3,'p_imprimir_lista_valores','Gramatica.py',405),
  ('impresion_valores -> expresiones','impresion_valores',1,'p_imprimir_lista_valores','Gramatica.py',406),
  ('expresiones -> RESTA expresiones','expresiones',2,'p_expresiones','Gramatica.py',417),
  ('expresiones -> expresiones SUMA expresiones','expresiones',3,'p_expresiones','Gramatica.py',418),
  ('expresiones -> expresiones RESTA expresiones','expresiones',3,'p_expresiones','Gramatica.py',419),
  ('expresiones -> expresiones MULTI expresiones','expresiones',3,'p_expresiones','Gramatica.py',420),
  ('expresiones -> expresiones DIVI expresiones','expresiones',3,'p_expresiones','Gramatica.py',421),
  ('expresiones -> expresiones MODULO expresiones','expresiones',3,'p_expresiones','Gramatica.py',422),
  ('expresiones -> POWF PI expresiones COMA expresiones PD','expresiones',6,'p_expresiones','Gramatica.py',423),
  ('expresiones -> POW PI expresiones COMA expresiones PD','expresiones',6,'p_expresiones','Gramatica.py',424),
  ('expresiones -> expresiones MAYORIGUAL expresiones','expresiones',3,'p_expresiones','Gramatica.py',425),
  ('expresiones -> expresiones MAYOR expresiones','expresiones',3,'p_expresiones','Gramatica.py',426),
  ('expresiones -> expresiones MENORIGUAL expresiones','expresiones',3,'p_expresiones','Gramatica.py',427),
  ('expresiones -> expresiones MENOR expresiones','expresiones',3,'p_expresiones','Gramatica.py',428),
  ('expresiones -> expresiones IGUALDAD expresiones','expresiones',3,'p_expresiones','Gramatica.py',429),
  ('expresiones -> expresiones DESIGUALDAD expresiones','expresiones',3,'p_expresiones','Gramatica.py',430),
  ('expresiones -> PI expresiones PD','expresiones',3,'p_expresiones','Gramatica.py',431),
  ('expresiones -> ID','expresiones',1,'p_expresiones','Gramatica.py',432),
  ('expresiones -> ENTERO','expresiones',1,'p_expresiones','Gramatica.py',433),
  ('expresiones -> ENTERO tipo_string','expresiones',2,'p_expresiones','Gramatica.py',434),
  ('expresiones -> FLOAT','expresiones',1,'p_expresiones','Gramatica.py',435),
  ('expresiones -> CADENA','expresiones',1,'p_expresiones','Gramatica.py',436),
  ('expresiones -> TRUE','expresiones',1,'p_expresiones','Gramatica.py',437),
  ('expresiones -> FALSE','expresiones',1,'p_expresiones','Gramatica.py',438),
  ('tipo_string -> TOOWNED','tipo_string',1,'p_tipo_string','Gramatica.py',499),
  ('tipo_string -> TOSTRING','tipo_string',1,'p_tipo_string','Gramatica.py',500),
]
