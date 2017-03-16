# file verbs.py
"""
pja 3-15-2017 orig

test as
import verbs
p = {}
p = verbs.init(p)
"""
def init(p):
    p = {}
    import ppP
    p = ppP.setP(p)
    p['sy']['load'](p)
    import endcodeP
    p = endcodeP.init(p)
    p['sy']['push']('forth')
    p['sy']['endcode'](p)
    p['sy']['push']('math')
    p['sy']['endcode'](p)
    p['sy']['push']('nds')
    p['sy']['endcode'](p)
    p['sy']['push']('ndsP.py') #parse file to test
    p['sy']['push']('fioi')
    p['sy']['endcode'](p)
    return(p)
#end init


