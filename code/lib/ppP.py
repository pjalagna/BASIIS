# file ppP.py
"""
pja 3-15-2017 orig

test as
p = {}
import ppP
p = ppP.setP(p)
p['sy']['load'](p)


"""
def setP(p):
    p = {}
    p['dat'] = [] # data stack
    p['r'] = [] # r stack
    p['v'] = {} # nds
    p['l'] = {} # lib table
    p['sy'] = {} # symbol table
    p['c'] = {} # class table
    p['sy']['pop'] = datPop
    p['sy']['push'] = datPush
    p['sy']['dump'] = dump
    p['sy']['load'] = load
    p['v']['trace'] = 'on'
    p['OK'] = 'pOK'
    p['NOK'] = 'pNOK'
    return(p)
#end setP
def datPush(val):
    global p
    p['dat'].append(val)
    if (p['v']['trace'] == 'on'):
        nop = raw_input('push('+val.__str__() + ")")
    #endif
#end datPush
def datPop():
    global p
    v = p['dat'].pop()
    if (p['v']['trace'] == 'on'):
        nop = raw_input('................pop('+ v.__str__() + ")")
    #endif
    return(v)
#end datPop
def dump():
    global p
    return(p)
#end dump
def load(pin):
    global p
    p = pin
#end load

