
#file pfgi.py
#generated for pgfi.txt 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def masterLoop_1():
    global p
    logg('masterLoop_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- >>?  -- ') 
    if (r == p['OK']):
        logg('push text >>?  ')
        datPush(">>? ")
        logg('after >>?  ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ask ) ')
    if (r == p['OK']):
        logg('call ask ')
        p['sy']['ask'](p)
        logg('after ask')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( dup ) ')
    if (r == p['OK']):
        logg('call dup ')
        p['sy']['dup'](p)
        logg('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- command -- ') 
    if (r == p['OK']):
        logg('push text command ')
        datPush("command")
        logg('after command ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final masterLoop_1')
#end masterLoop_1

def masterLoop_2():
    global p
    logg('masterLoop_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- command -- ') 
    if (r == p['OK']):
        logg('push text command ')
        datPush("command")
        logg('after command ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- done -- ') 
    if (r == p['OK']):
        logg('push text done ')
        datPush("done")
        logg('after done ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final masterLoop_2')
#end masterLoop_2

def masterLoop_3():
    global p
    logg('masterLoop_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- command -- ') 
    if (r == p['OK']):
        logg('push text command ')
        datPush("command")
        logg('after command ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- push -- ') 
    if (r == p['OK']):
        logg('push text push ')
        datPush("push")
        logg('after push ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( <<var>> ) ')
    if (r == p['OK']):
        logg('call <<var>> ')
        p['sy']['<<var>>'](p)
        logg('after <<var>>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- <<var>> -- ') 
    if (r == p['OK']):
        logg('push text <<var>> ')
        datPush("<<var>>")
        logg('after <<var>> ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final masterLoop_3')
#end masterLoop_3

def masterLoop_4():
    global p
    logg('masterLoop_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- command -- ') 
    if (r == p['OK']):
        logg('push text command ')
        datPush("command")
        logg('after command ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- dump -- ') 
    if (r == p['OK']):
        logg('push text dump ')
        datPush("dump")
        logg('after dump ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- not sure -- ') 
    if (r == p['OK']):
        logg('push text not sure ')
        datPush("not sure")
        logg('after not sure ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( msg ) ')
    if (r == p['OK']):
        logg('call msg ')
        p['sy']['msg'](p)
        logg('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final masterLoop_4')
#end masterLoop_4

def masterLoop_5():
    global p
    logg('masterLoop_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- command -- ') 
    if (r == p['OK']):
        logg('push text command ')
        datPush("command")
        logg('after command ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- trace -- ') 
    if (r == p['OK']):
        logg('push text trace ')
        datPush("trace")
        logg('after trace ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- <<var>> -- ') 
    if (r == p['OK']):
        logg('push text <<var>> ')
        datPush("<<var>>")
        logg('after <<var>> ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- trace -- ') 
    if (r == p['OK']):
        logg('push text trace ')
        datPush("trace")
        logg('after trace ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final masterLoop_5')
#end masterLoop_5

def masterLoop_6():
    global p
    logg('masterLoop_6')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- command -- ') 
    if (r == p['OK']):
        logg('push text command ')
        datPush("command")
        logg('after command ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- dots -- ') 
    if (r == p['OK']):
        logg('push text dots ')
        datPush("dots")
        logg('after dots ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( dots ) ')
    if (r == p['OK']):
        logg('call dots ')
        p['sy']['dots'](p)
        logg('after dots')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final masterLoop_6')
#end masterLoop_6

def masterLoop (x):
    global p
    logg('begin masterLoop')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    masterLoopCtl = 1 # starting spoke
    while masterLoopCtl != 0:
        logg('loop masterLoopCtl = ' + masterLoopCtl.__str__())
        if (masterLoopCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (masterLoopCtl == 1):
            logg('call masterLoop_1')
            masterLoop_1()
            logg('after call masterLoop_1')
            # test and adjust for new spoke
            masterLoopCtl = chk(masterLoopCtl)

        elif (masterLoopCtl == 2):
            logg('call masterLoop_2')
            masterLoop_2()
            logg('after call masterLoop_2')
            # test and adjust for new spoke
            masterLoopCtl = chk(masterLoopCtl)

        elif (masterLoopCtl == 3):
            logg('call masterLoop_3')
            masterLoop_3()
            logg('after call masterLoop_3')
            # test and adjust for new spoke
            masterLoopCtl = chk(masterLoopCtl)

        elif (masterLoopCtl == 4):
            logg('call masterLoop_4')
            masterLoop_4()
            logg('after call masterLoop_4')
            # test and adjust for new spoke
            masterLoopCtl = chk(masterLoopCtl)

        elif (masterLoopCtl == 5):
            logg('call masterLoop_5')
            masterLoop_5()
            logg('after call masterLoop_5')
            # test and adjust for new spoke
            masterLoopCtl = chk(masterLoopCtl)

        elif (masterLoopCtl == 6):
            logg('call masterLoop_6')
            masterLoop_6()
            logg('after call masterLoop_6')
            # test and adjust for new spoke
            masterLoopCtl = chk(masterLoopCtl)

        else:
            #final
            logg('final masterLoop')    
            masterLoopCtl = 0 # break
        #endif
    #wend
#end masterLoop

# stream routines 

def Mvar(p):
    logg ('<<<<var>>>>')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    p['v']['<<var>>'] = j
    p['sy']['push'](p['OK']) # status
#endif Mvar

# END stream routines 

def main(startpoint,trace='off'):
    global p
    p = {}
    p['c'] = {} # classes
    p['v'] = {} # nds
    p['dat'] = [] # data stack
    p['r'] = [] # r stack
    p['l'] = {} # lib table
    p['sy'] = {} # symbol table
    p['sy']['pop'] = datPop
    p['sy']['push'] = datPush
    p['OK'] = 'pOK'
    p['NOK'] = 'pNOK'
    prepSy()
    p['v']['trace'] = trace
    if ( p['v']['trace'] != 'off'):
        print('end main')
    #endif

    # paragraph masterLoop
    p['sy']['masterLoop'] = masterLoop
    #

    # paragraph <<var>>
    p['sy']['<<var>>'] = Mvar
    #

    p['sy']['start'] = p['sy'][startpoint] 
#end main
def start(trace='off'):
    p['v']['trace'] = trace # save trace setting
    p['sy']['start'](trace) # process begins at start
#end start

#code additions 


# helper rtns 
def eqeq(needle):
    global p
    logg('begin eqeq - ' + needle )
    op1 = p['sy']['pop']()
    op1 = op1.upper()
    op2 = needle.upper()
    if (op1 == op2):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#end eqeq

def logg(strin):
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input(strin)  
    #endif
#end logg
def chk(ctl):
    # tests ok/nok/tail/... of verb return to adjust ctl 
    global p
    okn = p['sy']['pop']()
    logg('chk-okn ' + okn.__str__())
    if (okn == 'tail.'):
        ans = 1
    elif (okn == p['NOK']):
        ans = ctl + 1
    elif (okn == '...'):
        ans = ctl + 1
    else:
        ans = 0 # clause passed 
        datPush(p['OK']) # leave ok on stack
    #endif
    logg('chk-ret=' + ans.__str__())
    return(ans)
#end chk

def datPush(val):
    global p
    p['dat'].append(val)
    logg('push('+val.__str__() + ")")
#end datPush

def datPop():
    global p
    v = p['dat'].pop()
    logg('................pop('+ v.__str__() + ")")
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

def help():
    out = " usage \n"
    out += "import NAME \n"
    out += "z = NAME \n"
    out += "z.main(startpoint,trace) prepares vectors \n"
    out += "v =  NAME.dump() # grabs and allows passage of vectors \n"
    out += "to execute: \n"
    out += "-- z.start(trace) \n \n"
    out += "to add externial vectors: \n"
    out += "v /*from dump */ = NAME.take(v,VectorFilename) - adds vectors into process via file \n"
    out += "format of vectorFile: \n"
    out += "-1 def main(v) sets and returns structure v \n"
    out += "--- v['sy'][verbName] = procName \n"
    out += "-2 def procName(v) \n"
    print(out)
#end help

def take(p,VectorFile):
    # given a P set file - add vectors to architecture 
    # do wild import
    j = __import__( VectorFile ) # no .py extension
    # run x.main(p)
    p = j.main(p)
    return(p) #ret p
#end take

