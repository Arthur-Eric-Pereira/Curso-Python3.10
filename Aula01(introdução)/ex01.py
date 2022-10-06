#ex01: PADRÃO DE CORES ANSI:
'''

------------------------------------------------
   text:    [cor]        back:       style:
    30  -  Branco   -     40        0 none
    31  -  Vermelho -     41        1 NEGRITO
    32  -  Verde    -     42        4 _underline_
    33  -  Amarelo  -     43        7 N3G4T1V3
    34  -  Azul     -     44        
    35  -  Magenta  -     45        
    36  -  Ciano    -     46        
    37  -  Cinza    -     47        
------------------------------------------------
COMANDO:
\033[style; text; backm  ...  \033[m
    
'''

print(f'\033[1;36;43m->Testando as cores no Python...\033[m')
