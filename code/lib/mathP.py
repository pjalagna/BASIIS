# file mathP.py
"""
pja 3-15-2017 orig

test as
p['sy']['push']('math')
p['sy']['endcode'](p)
p['sy']['push']('5')
p['sy']['push']('12')
p['sy']['+'](p)
p['dat']


"""
def init(p):
    p['sy']['+'] = plus
    p['sy']['-'] = neg
    p['sy']['/'] = div
    p['sy']['*'] = mult
    p['sy']['='] = eq
    p['sy']['!='] = neq
    p['sy']['<'] = gtr
    p['sy']['>'] = less
    p['sy']['++'] = incr
    p['sy']['--'] = decr
    return(p)
#end init
def plus(p):
    if (p['v']['trace'] == 'on'):
        print('begin plus')
    #endif
    op2 = p['sy']['pop']()
    op1 = p['sy']['pop']()
    ans = float(op1) + float(op2)
    p['sy']['push'](ans.__str__())
    p['sy']['push'](p['OK'])
#end plus
def neg(p):
    if (p['v']['trace'] == 'on'):
        print('begin neg')
    #endif
    op2 = p['sy']['pop']()
    op1 = p['sy']['pop']()
    ans = float(op1) - float(op2)
    p['sy']['push'](ans.__str__())
    p['sy']['push'](p['OK'])
#end neg
def mult(p):
    if (p['v']['trace'] == 'on'):
        print('begin mult')
    #endif
    op2 = p['sy']['pop']()
    op1 = p['sy']['pop']()
    ans = float(op1) * float(op2)
    p['sy']['push'](ans.__str__())
    p['sy']['push'](p['OK'])
#end mult
def div(p):
    if (p['v']['trace'] == 'on'):
        print('begin div')
    #endif
    op2 = p['sy']['pop']()
    op1 = p['sy']['pop']()
    ans = float(op1) / float(op2)
    p['sy']['push'](ans.__str__())
    p['sy']['push'](p['OK'])
#end div
def incr(p):
    if (p['v']['trace'] == 'on'):
        print('begin incr')
    #endif
    adr = p['sy']['pop']() # addr
    vval = p['sy']['@'](p)
    nop = p['sy']['pop']() #returned ok
    ans = float(vval) + 1
    p['sy']['push'](ans.__str__()) #data
    p['sy']['push'](addr) #address
    p['sy']['!'](p)
    nop = p['sy']['pop']() #returned ok
    p['sy']['push'](p['OK'])
#end incr
def decr(p):
    if (p['v']['trace'] == 'on'):
        print('begin decr')
    #endif
    adr = p['sy']['pop']() # addr
    vval = p['sy']['@'](p)
    nop = p['sy']['pop']() #returned ok
    ans = float(vval) - 1
    p['sy']['push'](ans.__str__()) #data
    p['sy']['push'](addr) #address
    p['sy']['!'](p)
    nop = p['sy']['pop']() #returned ok
    p['sy']['push'](p['OK'])
#end decr

##### logicals #####
def eq(p):
    if (p['v']['trace'] == 'on'):
        print('begin eq')
    #endif
    op2 = p['sy']['pop']()
    op1 = p['sy']['pop']()
    if (op1 == op2):
        p['sy']['push'](p['OK']) #ok
    else:
        p['sy']['push'](p['NOK'])#nok
    #endif
#end eq
def neq(p):
    if (p['v']['trace'] == 'on'):
        print('begin neq')
    #endif
    op2 = p['sy']['pop']()
    op1 = p['sy']['pop']()
    if (op1 != op2):
        p['sy']['push'](p['OK']) #ok
    else:
        p['sy']['push'](p['NOK'])#nok
    #endif
#end neq
def gtr(p):
    if (p['v']['trace'] == 'on'):
        print('begin gtr')
    #endif
    op2 = p['sy']['pop']()
    op1 = p['sy']['pop']()
    if (op1 < op2):
        p['sy']['push'](p['OK']) #ok
    else:
        p['sy']['push'](p['NOK'])#nok
    #endif
#end gtr
def less(p):
    if (p['v']['trace'] == 'on'):
        print('begin less')
    #endif
    op2 = p['sy']['pop']()
    op1 = p['sy']['pop']()
    if (op1 > op2):
        p['sy']['push'](p['OK']) #ok
    else:
        p['sy']['push'](p['NOK'])#nok
    #endif
#end less
    
    
       
    
