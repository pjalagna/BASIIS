#file doVerb.py
"""
pja 11-25-2018 added tail., swap , drop
paj 2018-11-15 added code for elipsis
pja 11-09-2018 changed endcode to incl; added code
"""
def init(p):
    # load symbol table with all known verbs
    p['sy']['msg'] = msg
    p['sy']['='] = eq
    p['sy']['!'] = bang
    p['sy']['@'] = att
    p['sy']['incl:'] = incl
    p['sy']['code:'] = code
    p['sy']['...'] = elipsis
    p['sy']['dumpNDS'] = dumpNDS
    p['sy']['ask'] = ask
    p['sy']['tail.'] = tail
    p['sy']['swap'] = swap
    p['sy']['drop'] = drop
    p['sy']['dup'] = dup
    p['sy']['dots'] = dots
    p['sy']['dot'] = dot
    p['sy']['verb'] = verb
    p['sy']['dumpDAT'] = dumpDAT
    return(p)
#end init
def dumpDAT(p):
    print(p['dat'].__str__())
    p['sy']['push'](p['OK']) # status
#end dumpDAT

def verb(p):
    vn = p['sy']['pop']()
    print('vn=(' + vn + ")")
    p['sy'][vn](p) # as dangerous as eval
    p['sy']['push'](p['OK']) # status
#end verb
def dots(p):
    print("dot=(" + p['sy']['pop']() + ")")
    p['sy']['push'](p['OK']) # status
#end dots
def dot(p):
    print("dot=(" + p['sy']['pop']() + ")")
    print("dot2=(" + p['sy']['pop']() + ")")
    # no status
#end dots

def dup(p):
   a = p['sy']['pop']()
   p['sy']['push'](a)
   p['sy']['push'](a)
   p['sy']['push'](p['OK']) # status
#end dup
def drop(p):
    p['sy']['pop']()
    p['sy']['push'](p['OK'])
#end drop
def swap(p):
    a = p['sy']['pop']()
    b = p['sy']['pop']()
    p['sy']['push'](a)
    p['sy']['push'](b)
    p['sy']['push'](p['OK']) # status
#end swap
def tail(p):
    p['sy']['push']('tail.') # will be caught by pgf
#end tail

def ask(p):
    """ get from operator input """
    p['sy']['msg'](p) # print question
    j = raw_input('>? ')
    p['sy']['push'](j)
    p['sy']['push'](p['OK'])
#end ask
    
def dumpNDS(p):
    """ development routine prints p['v'] """
    print(p['v'])
    raw_input('>?')
    p['sy']['push'](p['OK'])
#end dumpNDS

def elipsis(p):
    """ exit to next clause """
    p['sy']['push'] ( '...' )
    # do not set ok nok status
# end elipsis


   
def code(p):
    """ syntatic sugar """
    p['sy']['push'](p['OK'])
#end code
def incl(p):
    """ NEEDS WORK """
    """ add to symbol table """
    if (p['v']['trace'] == 'on'):
        print('endcode:')
    #endif
    m = p['sy']['pop']()  #program name
    # import file <m>P.py
    k = __import__ (m+'P.py')
    # add to symbol table
    p['sy'][m+'P.py'] = k
    # do p = m.init(p)
    p = k.init(p)
    # push ok
    p['sy']['push'](p['OK'])
#end incl
def msg(p):
    if (p['v']['trace'] == 'on'):
        print('msg')
    #endif
    m = p['sy']['pop']()
    print(m)
    p['sy']['push'](p['OK'])
#end msg
def bang(p):
    if (p['v']['trace'] == 'on'):
        print('bang')
    #endif
    ad = p['sy']['pop']()
    vval = p['sy']['pop']()
    p['v'][ad] = vval
    p['sy']['push'](p['OK'])
#endif
def att(p):
    if (p['v']['trace'] == 'on'):
        print('att')
    #endif
    ad = p['sy']['pop']()
    p['sy']['push'](p['v'][ad])
    p['sy']['push'](p['OK'])
#end att
def eq(p):
    if (p['v']['trace'] == 'on'):
        print('eq')
    #endif
    op1 = p['sy']['pop']()
    op2 = p['sy']['pop']()
    if (op1 == op2):
       p['sy']['push'](p['OK'])
    else:
       p['sy']['push'](p['NOK'])
    #endif
#end eq
    
    
