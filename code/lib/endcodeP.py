# file endcodeP.py
"""
pja 3-15-2017 orig

test as
-- after ppP
import endcodeP
p = endcodeP.init(p)

"""
def init(p):
    p['sy']['endcode'] = endcode
    return(p)
#end init

def endcode(p):
    pn = p['sy']['pop']()
    pnc = pn + "P"
    p['c'][pn] = __import__(pnc)
    p = p['c'][pn].init(p)
    p['sy']['push'](p['OK'])
#end endcode
