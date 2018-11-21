#file doVerb.py
# 2018-11-15 added code for elipsis
# 11-09-2018 changed endcode to incl; added code
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
    return(p)
#end init
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
    
    
