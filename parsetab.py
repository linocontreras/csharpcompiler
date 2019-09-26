
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGNMENT BOOLEAN_LITERAL CONST DIVIDE ELSE IDENTIFIER IF INTEGER_LITERAL LBRACKET LPAREN MINUS PLUS RBRACKET REAL_LITERAL RPAREN SEMICOLON STRING_LITERAL TIMES TYPE WHILEstart : statement_liststatement_list : statement_list statement\n                          | emptystatement : asignment\n                 | CONST asignmentasignment : TYPE IDENTIFIER ASSIGNMENT INTEGER_LITERAL SEMICOLONempty :'
    
_lr_action_items = {'CONST':([0,2,3,4,5,8,12,],[-7,6,-3,-2,-4,-5,-6,]),'TYPE':([0,2,3,4,5,6,8,12,],[-7,7,-3,-2,-4,7,-5,-6,]),'$end':([0,1,2,3,4,5,8,12,],[-7,0,-1,-3,-2,-4,-5,-6,]),'IDENTIFIER':([7,],[9,]),'ASSIGNMENT':([9,],[10,]),'INTEGER_LITERAL':([10,],[11,]),'SEMICOLON':([11,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'statement_list':([0,],[2,]),'empty':([0,],[3,]),'statement':([2,],[4,]),'asignment':([2,6,],[5,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statement_list','start',1,'p_start','syntax.py',10),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','syntax.py',14),
  ('statement_list -> empty','statement_list',1,'p_statement_list','syntax.py',15),
  ('statement -> asignment','statement',1,'p_statement','syntax.py',22),
  ('statement -> CONST asignment','statement',2,'p_statement','syntax.py',23),
  ('asignment -> TYPE IDENTIFIER ASSIGNMENT INTEGER_LITERAL SEMICOLON','asignment',5,'p_asignment','syntax.py',27),
  ('empty -> <empty>','empty',0,'p_empty','syntax.py',31),
]
