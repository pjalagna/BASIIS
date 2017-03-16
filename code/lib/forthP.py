# file forthP.py
""" inserts all stack verbs into symbol table and class table
pja 3-15-2017 orig

test as
p['sy']['push']('forth')
p['sy']['endcode'](p)
p['dat']
p['sy']['push']('box')
p['sy']['dup'](p)
p['dat']

"""
def init(p):
    p['sy']['dup'] = dup
    p['sy']['drop'] = drop
    p['sy']['cat'] = cat
    p['sy']['swap'] = swap
    ## p['sy']['slice'] = slice # "str" ==> f,m,l
    ## p['sy']['pslice'] = pslice # num ==> f,m,l
    ## p['sy']['roll'] = roll
    return(p)
#end init
def dup(p):
    if (p['v']['trace'] == 'on'):
        print('dup begin')
    #end if
    op1 = p['sy']['pop']()
    p['sy']['push'](op1) 
    p['sy']['push'](op1)
    p['sy']['push'](p['OK'])
#end dup
def drop(p):
    if (p['v']['trace'] == 'on'):
        print('drop begin')
    #end if
    op1 = p['sy']['pop']()
    p['sy']['push'](p['OK'])
#end drop
def cat(p):
    if (p['v']['trace'] == 'on'):
        print('cat begin')
    #end if
    op1 = p['sy']['pop']()
    op2 = p['sy']['pop']()
    opc = op2 + op1
    p['sy']['push'](opc) 
    p['sy']['push'](p['OK'])
#end cat
def swap(p):
    if (p['v']['trace'] == 'on'):
        print('swap begin')
    #end if
    op1 = p['sy']['pop']()
    op2 = p['sy']['pop']()
    p['sy']['push'](op1) 
    p['sy']['push'](op2)
    p['sy']['push'](p['OK'])
#end swap
def roll(p):
    if (p['v']['trace'] == 'on'):
        print('roll begin')
    #end if
    op1 = p['sy']['pop']()
    op2 = p['sy']['pop']()
    op3 = p['sy']['pop']()
    p['sy']['push'](op1) 
    p['sy']['push'](op2)
    p['sy']['push'](op3)
    p['sy']['push'](p['OK'])
#end roll
    
