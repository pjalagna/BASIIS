# file fioiP.py
""" set vectors for fioiClass 
pja 3-15-2017 orig

"""
def init(p):
    inFile = p['sy']['pop']()
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
    ans = p['c']['fioi'].fpword()
    p['v']['Cword'] = ans # full structure
    p['sy']['push'](ans[1].__str__()) # just word
    p['sy']['push'](p['OK'])
#end Pfpword
def Pfpback(p):
    if (p['v']['trace'] == 'on'):
        print('begin Pfpback')
    #endif
    struct1 = p['v']['Cword'][0] # ioxold, word, ioxNew,type
    ans = p['c']['fioi'].fpback([struct1 , struct1, struct1 ])
    p['v']['Cword'] = ans # 0, '', ioxOld
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
