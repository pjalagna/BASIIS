# file askP.py
""" 
pja 03-27-2017 added annoncement
uses p vector object 

"""
def initaskP(p):
    p['sy']['ask'] = ask
    return(p)
#end initaskP
def ask(p):
    # pop lit
    dd = p['sy']['pop']()
    print("***************** question *****************")
    ans = raw_input(dd+"? ")
    print("********************************************")
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end ask

