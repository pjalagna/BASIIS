# file fioiP.py
""" set vectors for fioiClass 
pja 11-24-2018 changed def name to main
--- for compatibility with basiiHelper, pgf
- fixed problem of timing. when includes are called there is nothing on the stack.
pja 3-15-2017 orig

"""
def main(p):
    p['sy']['push']('input fileName? ')
    p['sy']['ask'](p)
    p['sy']['pop']() # ok
    inFile = p['sy']['pop']()
    p['v']['infile'] = inFile # save NDS
    p['c']['fioiClass'] = __import__('fioiClass')
    p['c']['fioi'] = p['c']['fioiClass'].fio(inFile)
    p['sy']['fioi'] = Pfioi
    p['sy']['fioo'] = Pfioo
    p['sy']['pword'] = Pfpword
    p['sy']['pback'] = Pfpback
    return(p)
#end init

def Pfioo(p):
    if (p['v']['trace'] == 'on'):
        print('begin Pfioo')
    #endif
    p['c']['fioi'].fioo()
    p['sy']['push'](p['OK'])
#end Pfioo
def Pfioi(p):
    if (p['v']['trace'] == 'on'):
        print('begin Pfioi')
    #endif
    ans = p['c']['fioi'].fioi()
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end Pfioi
def Pfpword(p):
    if (p['v']['trace'] == 'on'):
        print('begin Pfpword')
    #endif
    ans = p['c']['fioi'].fpwd()
    
    p['sy']['push'](ans) # just word
    p['sy']['push'](p['OK'])
#end Pfpword
def Pfpback(p):
    if (p['v']['trace'] == 'on'):
        print('begin Pfpback')
    #endif
    p['c']['fioi'].fpbk()
    p['sy']['push'](p['OK'])
#end Pfpback

    """
    fgetSize
fioo
fioxGet
fioxSet
flookup
fwhite
ftill
ftillor
fctill
fctillor
fpword
fpback
fgetAlpha
fgetNum
fgetAnum
"""
