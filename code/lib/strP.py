# file strP.py
""" history
pja 11-23-2018 orig

test as
# same as basiiHelper
# define datpop, dattpush
def datPush(val):
    global p
    p['dat'].append(val)
    #logg('push('+val.__str__() + ")")
#end datPush

def datPop():
    global p
    v = p['dat'].pop()
    #logg('................pop('+ v.__str__() + ")")
    return(v)
#end datPop

def dump():
    global p
    return(p)
#end dump

p = {}
p['v'] = {} # nds
p['dat'] = [] # data stack
p['r'] = [] # r stack
p['l'] = {} # lib table
p['sy'] = {} # symbol table
p['sy']['pop'] = datPop
p['sy']['push'] = datPush
p['OK'] = 'pOK'
p['NOK'] = 'pNOK'

# end copy of basiiHelper
import strP
p = strP.main(p)

p['sy']['push']('was') # replacement
p['sy']['push']('am') # needle
p['sy']['push']('i am one are you') # haystack
p['sy']['strReplace'](p)

p['sy']['pop']()  # grab ok
p['sy']['pop']() # changed am to was

p['sy']['push']('front to')
p['sy']['push']('back')
p['sy']['cats'](p)
p['sy']['pop']()  # grab ok
p['sy']['pop']() # should say 'front to back' note space
"""
def main(p):
    p['sy']['strReplace'] = strReplace
    p['sy']['cat'] = cat
    p['sy']['cats'] = cats
    p['sy']['crlf'] = crlf
    p['sy']['strRemove'] = strRemove
    p['sy']['dots'] = dots
    return(p)
#end main
def dots(p):
    """ prints from stack ('abc',,) & print """
    ans = p['sy']['pop']()
    print(ans.__str__())
    p['sy']['push'](p['OK'])
#end dots
def strRemove(p):
    """ removes last char from string ('abcd',,'abc')"""
    ss = p['sy']['pop']()
    ss1 = ss.__str__()
    ans = ss1[0:-1]
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end strRemove
def strReplace(p):
    """ (haystack,needle,sol,,replacementHaystack) """
    haystack = p['sy']['pop']()
    needle = p['sy']['pop']()
    sol = p['sy']['pop']()
    ans = haystack.replace(needle,sol)
    p['sy']['push'](ans)
    p['sy']['push'](p['OK']) # pgf compatable
#end strReplace
def cat(p):
    """ (b,a,,ab) """
    b = p['sy']['pop']()
    a = p['sy']['pop']()
    ans = a + b
    p['sy']['push'](ans)
    p['sy']['push'](p['OK']) # pgf compatable
#end cat    
def cats(p):
    """ (b,a,,a" "b) """
    b = p['sy']['pop']()
    a = p['sy']['pop']()
    ans = a + ' ' + b
    p['sy']['push'](ans)
    p['sy']['push'](p['OK']) # pgf compatable
#end cats
def crlf(p):
    ans = "\n"
    p['sy']['push'](ans)
    p['sy']['push'](p['OK']) # pgf compatable
#end crlf
      
  