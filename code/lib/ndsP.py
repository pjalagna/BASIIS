# file ndsP.py
"""
pja 3-15-2017 orig

test as
p['sy']['push']('nds')
p['sy']['endcode'](p)
p['sy']['push']('you') # data
p['sy']['push'] ('tu') # adder
p['sy']['!'](p)
p['sy']['push']('tu')
p['sy']['@'](p)
"""
def init(p):
    p['sy']['@'] = att
    p['sy']['!'] = bang
    return(p)
#end init
def att(p):
    K = p['sy']['pop']()
    j = p['v'][K]
    p['sy']['push'](j)
    p['sy']['push'](p['OK'])
#end att
def bang(p):
    K = p['sy']['pop']()
    D = p['sy']['pop']()
    p['v'][K] = D
    p['sy']['push'](p['OK'])
#end bang
    
    
