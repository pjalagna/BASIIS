
#file jadPBasii.py
#generated for jadP.Basii.txt 

 
def jad0_jad1():
    global p
    
    if (p['v']['trace'] == 'on'):
        nop = raw_input('jad0_jad1')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push file name?')
        #endif
        datPush(file name?)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after file name?')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ask')
        #endif
        p['sy']['ask'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ask')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push infile')
        #endif
        datPush(infile)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after infile')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call !')
        #endif
        p['sy']['!'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call initPword')
        #endif
        p['sy']['initPword'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after initPword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call jadP')
        #endif
        p['sy']['jadP'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after jadP')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final jad0_jad1')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end jad0_jad1

def jad0 (x):
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('jad0')
        #print('dat',p['dat'])
    #endif
    datPush(p['NOK'])

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call jad0_jad1')
        #endif
        jad0_jad1()
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after call jad0_jad1')
        #endif
    #endif
    #

    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final jad0')    
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end jad0

def initPword_1():
    global p
    
    if (p['v']['trace'] == 'on'):
        nop = raw_input('initPword_1')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call code:')
        #endif
        p['sy']['code:'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after code:')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call --')
        #endif
        p['sy']['--'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after --')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call endcode:')
        #endif
        p['sy']['endcode:'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after endcode:')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final initPword_1')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end initPword_1

def initPword (x):
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('initPword')
        #print('dat',p['dat'])
    #endif
    datPush(p['NOK'])

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call initPword_1')
        #endif
        initPword_1()
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after call initPword_1')
        #endif
    #endif
    #

    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final initPword')    
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end initPword

def jadP_jadP1():
    global p
    
    if (p['v']['trace'] == 'on'):
        nop = raw_input('jadP_jadP1')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call pword')
        #endif
        p['sy']['pword'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after pword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push tableN')
        #endif
        datPush(tableN)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tableN')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call !')
        #endif
        p['sy']['!'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dbBraceCheck')
        #endif
        p['sy']['dbBraceCheck'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dbBraceCheck')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push e')
        #endif
        datPush(e)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after e')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call @')
        #endif
        p['sy']['@'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push ok')
        #endif
        datPush(ok)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ok')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call =')
        #endif
        p['sy']['='](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call keyset')
        #endif
        p['sy']['keyset'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after keyset')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tagset')
        #endif
        p['sy']['tagset'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tagset')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call pword')
        #endif
        p['sy']['pword'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after pword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push )')
        #endif
        datPush())
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after )')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call =')
        #endif
        p['sy']['='](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call actionSave')
        #endif
        p['sy']['actionSave'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after actionSave')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call pword')
        #endif
        p['sy']['pword'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after pword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push ;')
        #endif
        datPush(;)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ;')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tail.')
        #endif
        p['sy']['tail.'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final jadP_jadP1')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end jadP_jadP1

def jadP_jad2():
    global p
    
    if (p['v']['trace'] == 'on'):
        nop = raw_input('jadP_jad2')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push error occurred on (( check ')
        #endif
        datPush(error occurred on (( check )
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after error occurred on (( check ')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call msg')
        #endif
        p['sy']['msg'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final jadP_jad2')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end jadP_jad2

def jadP (x):
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('jadP')
        #print('dat',p['dat'])
    #endif
    datPush(p['NOK'])

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call jadP_jadP1')
        #endif
        jadP_jadP1()
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after call jadP_jadP1')
        #endif
    #endif
    #

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call jadP_jad2')
        #endif
        jadP_jad2()
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after call jadP_jad2')
        #endif
    #endif
    #

    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final jadP')    
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end jadP

def dbBraceCheck_dbc1():
    global p
    
    if (p['v']['trace'] == 'on'):
        nop = raw_input('dbBraceCheck_dbc1')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call pword')
        #endif
        p['sy']['pword'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after pword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push ((')
        #endif
        datPush((()
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ((')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call =')
        #endif
        p['sy']['='](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push ok')
        #endif
        datPush(ok)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ok')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push e')
        #endif
        datPush(e)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after e')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call !')
        #endif
        p['sy']['!'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final dbBraceCheck_dbc1')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end dbBraceCheck_dbc1

def dbBraceCheck_dbc2():
    global p
    
    if (p['v']['trace'] == 'on'):
        nop = raw_input('dbBraceCheck_dbc2')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push nok')
        #endif
        datPush(nok)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after nok')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push e')
        #endif
        datPush(e)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after e')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call !')
        #endif
        p['sy']['!'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final dbBraceCheck_dbc2')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end dbBraceCheck_dbc2

def dbBraceCheck (x):
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('dbBraceCheck')
        #print('dat',p['dat'])
    #endif
    datPush(p['NOK'])

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dbBraceCheck_dbc1')
        #endif
        dbBraceCheck_dbc1()
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after call dbBraceCheck_dbc1')
        #endif
    #endif
    #

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dbBraceCheck_dbc2')
        #endif
        dbBraceCheck_dbc2()
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after call dbBraceCheck_dbc2')
        #endif
    #endif
    #

    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final dbBraceCheck')    
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end dbBraceCheck
