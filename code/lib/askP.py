# file askP.py
""" uses p vector object """
def initaskP(p):
    p['sy']['ask'] = ask
    return(p)
#end initaskP
def ask(p):
    # pop lit
    dd = p['sy']['pop']()
    ans = raw_input(dd+"? ")
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end ask

