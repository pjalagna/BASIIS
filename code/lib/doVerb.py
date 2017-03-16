#file doVerb.py
def init(p):
    # load symbol table with all known verbs
    p['sy']['msg'] = msg
    p['sy']['='] = eq
    p['sy']['!'] = bang
    p['sy']['@'] = att
    p['sy']['endcode:'] = endcode
    p['sy']['code:'] = code
    return(p)
#end init
def code(p):
    """ syntatic sugar """
    p['sy']['push'](p['OK'])
#end code
def endcode(p):
    """ NEEDS WORK """
    """ add to symbol table """
    if (p['v']['trace'] == 'on'):
        print('endcode:')
    #endif
    m = p['sy']['pop']()  #program name
    # import file <name>P.py
    # do p = init<name>(p)
    # push ok
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
    
    
