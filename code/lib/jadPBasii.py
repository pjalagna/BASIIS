
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
        datPush('file name?')
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
        datPush('infile')
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
#end clause jad0_jad1

def jad0(p):
    line=0
    while (0<=line):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('line is ((' + line.__str__() + "))")
        #endif
        if(line==0):
            line = 1

        elif (line==1):
            #Trace and call jad0_jad1
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call jad0_jad1')
            #endif
            jad0_jad1()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call jad0_jad1')
            #endif
            line =doJ(line)

        #final
        else:
            if (0<=line):
                datPush(p['OK'])
            else:
                datPush(p['NOK']) # nok
            #endif
            line = -3 #break
        #endif
    #wend
#end paragraph jad0


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
#end clause initPword_1

def initPword(p):
    line=0
    while (0<=line):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('line is ((' + line.__str__() + "))")
        #endif
        if(line==0):
            line = 1

        elif (line==1):
            #Trace and call initPword_1
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call initPword_1')
            #endif
            initPword_1()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call initPword_1')
            #endif
            line =doJ(line)

        #final
        else:
            if (0<=line):
                datPush(p['OK'])
            else:
                datPush(p['NOK']) # nok
            #endif
            line = -3 #break
        #endif
    #wend
#end paragraph initPword


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
        datPush('tableN')
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
        datPush('e')
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
        datPush('ok')
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
        datPush(')')
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
        datPush(';')
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
#end clause jadP_jadP1

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
        datPush('error occurred on (( check ')
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
#end clause jadP_jad2

def jadP(p):
    line=0
    while (0<=line):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('line is ((' + line.__str__() + "))")
        #endif
        if(line==0):
            line = 1

        elif (line==1):
            #Trace and call jadP_jadP1
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call jadP_jadP1')
            #endif
            jadP_jadP1()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call jadP_jadP1')
            #endif
            line =doJ(line)

        elif (line==2):
            #Trace and call jadP_jad2
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call jadP_jad2')
            #endif
            jadP_jad2()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call jadP_jad2')
            #endif
            line =doJ(line)

        #final
        else:
            if (0<=line):
                datPush(p['OK'])
            else:
                datPush(p['NOK']) # nok
            #endif
            line = -3 #break
        #endif
    #wend
#end paragraph jadP


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
        datPush('((')
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
        datPush('ok')
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
        datPush('e')
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
#end clause dbBraceCheck_dbc1

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
        datPush('nok')
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
        datPush('e')
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
#end clause dbBraceCheck_dbc2

def dbBraceCheck(p):
    line=0
    while (0<=line):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('line is ((' + line.__str__() + "))")
        #endif
        if(line==0):
            line = 1

        elif (line==1):
            #Trace and call dbBraceCheck_dbc1
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call dbBraceCheck_dbc1')
            #endif
            dbBraceCheck_dbc1()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call dbBraceCheck_dbc1')
            #endif
            line =doJ(line)

        elif (line==2):
            #Trace and call dbBraceCheck_dbc2
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call dbBraceCheck_dbc2')
            #endif
            dbBraceCheck_dbc2()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call dbBraceCheck_dbc2')
            #endif
            line =doJ(line)

        #final
        else:
            if (0<=line):
                datPush(p['OK'])
            else:
                datPush(p['NOK']) # nok
            #endif
            line = -3 #break
        #endif
    #wend
#end paragraph dbBraceCheck


def keyset_name():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('keyset_name')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ~')
        #endif
        p['sy']['~'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ~')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call [}')
        #endif
        p['sy']['[}'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [}')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call */')
        #endif
        p['sy']['*/'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after */')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call [[')
        #endif
        p['sy']['[['](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 1')
        #endif
        p['sy']['1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ]]')
        #endif
        p['sy'][']]'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push kix')
        #endif
        datPush('kix')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after kix')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push 0')
        #endif
        datPush('0')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 0')
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
            nop = raw_input('call keyset1')
        #endif
        p['sy']['keyset1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after keyset1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final keyset_name')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause keyset_name

def keyset(p):
    line=0
    while (0<=line):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('line is ((' + line.__str__() + "))")
        #endif
        if(line==0):
            line = 1

        elif (line==1):
            #Trace and call keyset_name
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call keyset_name')
            #endif
            keyset_name()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call keyset_name')
            #endif
            line =doJ(line)

        #final
        else:
            if (0<=line):
                datPush(p['OK'])
            else:
                datPush(p['NOK']) # nok
            #endif
            line = -3 #break
        #endif
    #wend
#end paragraph keyset


def keyset1_1():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('keyset1_1')
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
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call kn*kix')
        #endif
        p['sy']['kn*kix'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after kn*kix')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call keyset2')
        #endif
        p['sy']['keyset2'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after keyset2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ...')
        #endif
        p['sy']['...'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call [[')
        #endif
        p['sy']['[['](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 2')
        #endif
        p['sy']['2'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ]]')
        #endif
        p['sy'][']]'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call kt1')
        #endif
        p['sy']['kt1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after kt1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
            nop = raw_input('call 1')
        #endif
        p['sy']['1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
            nop = raw_input('call kix++')
        #endif
        p['sy']['kix++'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after kix++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tail')
        #endif
        p['sy']['tail'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final keyset1_1')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause keyset1_1

def keyset1_3():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('keyset1_3')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call kt1')
        #endif
        p['sy']['kt1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after kt1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
            nop = raw_input('call 2')
        #endif
        p['sy']['2'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final keyset1_3')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause keyset1_3

def keyset1(p):
    line=0
    while (0<=line):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('line is ((' + line.__str__() + "))")
        #endif
        if(line==0):
            line = 1

        elif (line==1):
            #Trace and call keyset1_1
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call keyset1_1')
            #endif
            keyset1_1()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call keyset1_1')
            #endif
            line =doJ(line)

        elif (line==2):
            #Trace and call keyset1_3
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call keyset1_3')
            #endif
            keyset1_3()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call keyset1_3')
            #endif
            line =doJ(line)

        #final
        else:
            if (0<=line):
                datPush(p['OK'])
            else:
                datPush(p['NOK']) # nok
            #endif
            line = -3 #break
        #endif
    #wend
#end paragraph keyset1


def keyset2_1():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('keyset2_1')
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
            nop = raw_input('call ...')
        #endif
        p['sy']['...'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call [[')
        #endif
        p['sy']['[['](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 1.1')
        #endif
        p['sy']['1.1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 1.1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ]]')
        #endif
        p['sy'][']]'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dup')
        #endif
        p['sy']['dup'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push of')
        #endif
        datPush('of')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after of')
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
            nop = raw_input('call drop')
        #endif
        p['sy']['drop'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call pfk')
        #endif
        p['sy']['pfk'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after pfk')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tail')
        #endif
        p['sy']['tail'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final keyset2_1')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause keyset2_1

def keyset2_2():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('keyset2_2')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dup')
        #endif
        p['sy']['dup'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push [')
        #endif
        datPush('[')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [')
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
            nop = raw_input('call drop')
        #endif
        p['sy']['drop'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call keyVals')
        #endif
        p['sy']['keyVals'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after keyVals')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tail')
        #endif
        p['sy']['tail'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final keyset2_2')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause keyset2_2

def keyset2_3():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('keyset2_3')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dup')
        #endif
        p['sy']['dup'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push ~')
        #endif
        datPush('~')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ~')
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
            nop = raw_input('call drop')
        #endif
        p['sy']['drop'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call keyDesc')
        #endif
        p['sy']['keyDesc'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after keyDesc')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call [[')
        #endif
        p['sy']['[['](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 4')
        #endif
        p['sy']['4'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 4')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ]]')
        #endif
        p['sy'][']]'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dup')
        #endif
        p['sy']['dup'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push ,')
        #endif
        datPush(',')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ,')
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
            nop = raw_input('call drop')
        #endif
        p['sy']['drop'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call kt1')
        #endif
        p['sy']['kt1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after kt1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 1')
        #endif
        p['sy']['1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
        nop = raw_input('final keyset2_3')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause keyset2_3

def keyset2_5():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('keyset2_5')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dup')
        #endif
        p['sy']['dup'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dup')
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
        datPush(')')
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
            nop = raw_input('call drop')
        #endif
        p['sy']['drop'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call kt1')
        #endif
        p['sy']['kt1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after kt1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 2')
        #endif
        p['sy']['2'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
        nop = raw_input('final keyset2_5')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause keyset2_5

def keyset2_6():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('keyset2_6')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push unexpected marker near ')
        #endif
        datPush('unexpected marker near ')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after unexpected marker near ')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call swap')
        #endif
        p['sy']['swap'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after swap')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call cat')
        #endif
        p['sy']['cat'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call fail')
        #endif
        p['sy']['fail'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after fail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final keyset2_6')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause keyset2_6

def keyset2(p):
    line=0
    while (0<=line):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('line is ((' + line.__str__() + "))")
        #endif
        if(line==0):
            line = 1

        elif (line==1):
            #Trace and call keyset2_1
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call keyset2_1')
            #endif
            keyset2_1()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call keyset2_1')
            #endif
            line =doJ(line)

        elif (line==2):
            #Trace and call keyset2_2
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call keyset2_2')
            #endif
            keyset2_2()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call keyset2_2')
            #endif
            line =doJ(line)

        elif (line==3):
            #Trace and call keyset2_3
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call keyset2_3')
            #endif
            keyset2_3()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call keyset2_3')
            #endif
            line =doJ(line)

        elif (line==4):
            #Trace and call keyset2_5
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call keyset2_5')
            #endif
            keyset2_5()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call keyset2_5')
            #endif
            line =doJ(line)

        elif (line==5):
            #Trace and call keyset2_6
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call keyset2_6')
            #endif
            keyset2_6()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call keyset2_6')
            #endif
            line =doJ(line)

        #final
        else:
            if (0<=line):
                datPush(p['OK'])
            else:
                datPush(p['NOK']) # nok
            #endif
            line = -3 #break
        #endif
    #wend
#end paragraph keyset2


def tagset_name():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('tagset_name')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ~')
        #endif
        p['sy']['~'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ~')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call [}')
        #endif
        p['sy']['[}'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [}')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call */')
        #endif
        p['sy']['*/'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after */')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call [[')
        #endif
        p['sy']['[['](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 1')
        #endif
        p['sy']['1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ]]')
        #endif
        p['sy'][']]'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tix')
        #endif
        p['sy']['tix'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tix')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 0')
        #endif
        p['sy']['0'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tagset1')
        #endif
        p['sy']['tagset1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tagset1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final tagset_name')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause tagset_name

def tagset(p):
    line=0
    while (0<=line):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('line is ((' + line.__str__() + "))")
        #endif
        if(line==0):
            line = 1

        elif (line==1):
            #Trace and call tagset_name
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call tagset_name')
            #endif
            tagset_name()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call tagset_name')
            #endif
            line =doJ(line)

        #final
        else:
            if (0<=line):
                datPush(p['OK'])
            else:
                datPush(p['NOK']) # nok
            #endif
            line = -3 #break
        #endif
    #wend
#end paragraph tagset


def tagset1_1():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('tagset1_1')
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
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tn*tix')
        #endif
        p['sy']['tn*tix'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tn*tix')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tagset2')
        #endif
        p['sy']['tagset2'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tagset2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ...')
        #endif
        p['sy']['...'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call [[')
        #endif
        p['sy']['[['](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 2')
        #endif
        p['sy']['2'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ]]')
        #endif
        p['sy'][']]'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tgt1')
        #endif
        p['sy']['tgt1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tgt1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
            nop = raw_input('call 1')
        #endif
        p['sy']['1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
            nop = raw_input('call tix++')
        #endif
        p['sy']['tix++'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tix++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tail')
        #endif
        p['sy']['tail'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final tagset1_1')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause tagset1_1

def tagset1_3():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('tagset1_3')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tgt1')
        #endif
        p['sy']['tgt1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tgt1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
            nop = raw_input('call 2')
        #endif
        p['sy']['2'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final tagset1_3')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause tagset1_3

def tagset1(p):
    line=0
    while (0<=line):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('line is ((' + line.__str__() + "))")
        #endif
        if(line==0):
            line = 1

        elif (line==1):
            #Trace and call tagset1_1
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call tagset1_1')
            #endif
            tagset1_1()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call tagset1_1')
            #endif
            line =doJ(line)

        elif (line==2):
            #Trace and call tagset1_3
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call tagset1_3')
            #endif
            tagset1_3()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call tagset1_3')
            #endif
            line =doJ(line)

        #final
        else:
            if (0<=line):
                datPush(p['OK'])
            else:
                datPush(p['NOK']) # nok
            #endif
            line = -3 #break
        #endif
    #wend
#end paragraph tagset1


def tagset2_1():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('tagset2_1')
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
            nop = raw_input('call ...')
        #endif
        p['sy']['...'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call [[')
        #endif
        p['sy']['[['](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 1.1')
        #endif
        p['sy']['1.1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 1.1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ]]')
        #endif
        p['sy'][']]'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dup')
        #endif
        p['sy']['dup'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push of')
        #endif
        datPush('of')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after of')
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
            nop = raw_input('call drop')
        #endif
        p['sy']['drop'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tgfk')
        #endif
        p['sy']['tgfk'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tgfk')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tail')
        #endif
        p['sy']['tail'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final tagset2_1')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause tagset2_1

def tagset2_2():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('tagset2_2')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dup')
        #endif
        p['sy']['dup'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push [')
        #endif
        datPush('[')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [')
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
            nop = raw_input('call drop')
        #endif
        p['sy']['drop'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tagVals')
        #endif
        p['sy']['tagVals'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tagVals')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tail')
        #endif
        p['sy']['tail'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final tagset2_2')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause tagset2_2

def tagset2_3():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('tagset2_3')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dup')
        #endif
        p['sy']['dup'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push ~')
        #endif
        datPush('~')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ~')
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
            nop = raw_input('call drop')
        #endif
        p['sy']['drop'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call //')
        #endif
        p['sy']['//'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after //')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tagDesc')
        #endif
        p['sy']['tagDesc'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tagDesc')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call [[')
        #endif
        p['sy']['[['](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 4')
        #endif
        p['sy']['4'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 4')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call ]]')
        #endif
        p['sy'][']]'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dup')
        #endif
        p['sy']['dup'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push ,')
        #endif
        datPush(',')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after ,')
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
            nop = raw_input('call drop')
        #endif
        p['sy']['drop'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tgt1')
        #endif
        p['sy']['tgt1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tgt1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 1')
        #endif
        p['sy']['1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
        nop = raw_input('final tagset2_3')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause tagset2_3

def tagset2_5():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('tagset2_5')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call dup')
        #endif
        p['sy']['dup'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after dup')
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
        datPush(')')
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
            nop = raw_input('call drop')
        #endif
        p['sy']['drop'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call tgt1')
        #endif
        p['sy']['tgt1'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after tgt1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call 2')
        #endif
        p['sy']['2'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after 2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
        nop = raw_input('final tagset2_5')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause tagset2_5

def tagset2_6():
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('tagset2_6')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push unexpected marker near ')
        #endif
        datPush('unexpected marker near ')
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after unexpected marker near ')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call swap')
        #endif
        p['sy']['swap'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after swap')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call cat')
        #endif
        p['sy']['cat'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
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
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call fail')
        #endif
        p['sy']['fail'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after fail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final tagset2_6')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end clause tagset2_6

def tagset2(p):
    line=0
    while (0<=line):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('line is ((' + line.__str__() + "))")
        #endif
        if(line==0):
            line = 1

        elif (line==1):
            #Trace and call tagset2_1
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call tagset2_1')
            #endif
            tagset2_1()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call tagset2_1')
            #endif
            line =doJ(line)

        elif (line==2):
            #Trace and call tagset2_2
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call tagset2_2')
            #endif
            tagset2_2()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call tagset2_2')
            #endif
            line =doJ(line)

        elif (line==3):
            #Trace and call tagset2_3
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call tagset2_3')
            #endif
            tagset2_3()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call tagset2_3')
            #endif
            line =doJ(line)

        elif (line==4):
            #Trace and call tagset2_5
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call tagset2_5')
            #endif
            tagset2_5()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call tagset2_5')
            #endif
            line =doJ(line)

        elif (line==5):
            #Trace and call tagset2_6
            if (p['v']['trace'] == 'on'):
                nop = raw_input('call tagset2_6')
            #endif
            tagset2_6()
            if (p['v']['trace'] == 'on'):
                nop = raw_input('after call tagset2_6')
            #endif
            line =doJ(line)

        #final
        else:
            if (0<=line):
                datPush(p['OK'])
            else:
                datPush(p['NOK']) # nok
            #endif
            line = -3 #break
        #endif
    #wend
#end paragraph tagset2


def main(startpoint,trace='off'):
    global p
    p = {}
    p['dat'] = [] # data stack
    p['r'] = [] # r stack
    p['v'] = {} # nds
    p['l'] = {} # lib table
    p['sy'] = {} # symbol table
    p['sy']['pop'] = datPop
    p['sy']['push'] = datPush
    p['v']['trace'] = trace
    prepSy()
    p['OK'] = 'pOK'
    p['NOK'] = 'pNOK'

    # 
    p['sy']['jad0'] = jad0
    #

    # 
    p['sy']['initPword'] = initPword
    #

    # 
    p['sy']['jadP'] = jadP
    #

    # 
    p['sy']['dbBraceCheck'] = dbBraceCheck
    #

    # 
    p['sy']['keyset'] = keyset
    #

    # 
    p['sy']['keyset1'] = keyset1
    #

    # 
    p['sy']['keyset2'] = keyset2
    #

    # 
    p['sy']['tagset'] = tagset
    #

    # 
    p['sy']['tagset1'] = tagset1
    #

    # 
    p['sy']['tagset2'] = tagset2
    #
    # test pja 7-21-2017 was p['sy']['start'] = p['sy'][startpoint] 
    p['sy']['start'] = startpoint
    # did NOT return p
    return(p)
    # end test 7-21-2017
#end main
def start(trace='off'):
    global p
    p['sy']['start'](p) # process begins at start
#end start

# helper rtns 

def doJ(line):
    global p
    J = datPop()
    if (j ==p['OK']):
        datPush( p['OK'])
        line = -1 #break
    elif (j==p['NOK']):
        line = line +1
    elif (j=='TAIL'):
        line=0
    elif (j=='FAIL'):
        datPush(p['NOK']) # nok 
        line =-2 #break
    else:
        raw_input('error bad format verbs - returned ((' + j.__str__() + "))" )
        line = -3 # break
    #endif
    return(line)
#end doJ
def datPush(val):
    global p
    p['dat'].append(val)
    if (p['v']['trace'] == 'on'):
        nop = raw_input('push('+val.__str__() + ")")
    #endif
#end datPush

def datPop():
    global p
    v = p['dat'].pop()
    if (p['v']['trace'] == 'on'):
        nop = raw_input('................pop('+ v.__str__() + ")")
    #endif
    return(v)
#end datPop

def prepSy():
    global p
    import doVerb
    p = doVerb.init(p) # load vectors
#end prepSy

def dump():
    global p
    return(p)
#end dump
def load(pin):
    global p
    p = pin
#end load

def help():
    out = " usage \n"
    out += "import NAME \n"
    out += "z = NAME.main(startpoint,trace) \n"
    out += "z =  NAME.dump() # grabs and allows passage of vectors \n"
    out += "to add externial vectors: \n"
    out += "import process \n"
    out += "z['sy']['token'] = process.subprocessName \n"
    out += "NAME.take(z) - adds vectors into process  \n"
    print(out)
#end help

