
#file t0208.py
#generated for t11.txt 

 
def Tstart_st():
    global p
    logg('Tstart_st')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( a ) ')
    if (r == p['OK']):
        logg('call a ')
        p['sy']['a'](p)
        logg('after a')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( b ) ')
    if (r == p['OK']):
        logg('call b ')
        p['sy']['b'](p)
        logg('after b')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Tstart_st')
#end Tstart_st

def Tstart (x):
    global p
    logg('begin Tstart')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    TstartCtl = 1 # starting spoke
    while TstartCtl != 0:
        logg('loop TstartCtl = ' + TstartCtl.__str__())
        if (TstartCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (TstartCtl == 1):
            logg('call Tstart_st')
            Tstart_st()
            logg('after call Tstart_st')
            # test and adjust for new spoke
            TstartCtl = chk(TstartCtl)

        else:
            #final
            logg('final Tstart')    
            TstartCtl = 0 # break
        #endif
    #wend
#end Tstart

def a_aa():
    global p
    logg('a_aa')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- hello a;a  -- ') 
    if (r == p['OK']):
        logg('push text hello a;a  ')
        datPush("hello a;a ")
        logg('after hello a;a  ')
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
    logg('final a_aa')
#end a_aa

def a (x):
    global p
    logg('begin a')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    aCtl = 1 # starting spoke
    while aCtl != 0:
        logg('loop aCtl = ' + aCtl.__str__())
        if (aCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (aCtl == 1):
            logg('call a_aa')
            a_aa()
            logg('after call a_aa')
            # test and adjust for new spoke
            aCtl = chk(aCtl)

        else:
            #final
            logg('final a')    
            aCtl = 0 # break
        #endif
    #wend
#end a

def b_bb1():
    global p
    logg('b_bb1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- E -- ') 
    if (r == p['OK']):
        logg('push text E ')
        datPush("E")
        logg('after E ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- 1 -- ') 
    if (r == p['OK']):
        logg('push text 1 ')
        datPush("1")
        logg('after 1 ')
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
    logg('processing text -- ! -- ') 
    if (r == p['OK']):
        logg('push text ! ')
        datPush("!")
        logg('after ! ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- @ -- ') 
    if (r == p['OK']):
        logg('push text @ ')
        datPush("@")
        logg('after @ ')
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
    logg('processing text -- yep -- ') 
    if (r == p['OK']):
        logg('push text yep ')
        datPush("yep")
        logg('after yep ')
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
    logg('final b_bb1')
#end b_bb1

def b_bb2():
    global p
    logg('b_bb2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- nope  -- ') 
    if (r == p['OK']):
        logg('push text nope  ')
        datPush("nope ")
        logg('after nope  ')
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
    logg('final b_bb2')
#end b_bb2

def b (x):
    global p
    logg('begin b')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    bCtl = 1 # starting spoke
    while bCtl != 0:
        logg('loop bCtl = ' + bCtl.__str__())
        if (bCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (bCtl == 1):
            logg('call b_bb1')
            b_bb1()
            logg('after call b_bb1')
            # test and adjust for new spoke
            bCtl = chk(bCtl)

        elif (bCtl == 2):
            logg('call b_bb2')
            b_bb2()
            logg('after call b_bb2')
            # test and adjust for new spoke
            bCtl = chk(bCtl)

        else:
            #final
            logg('final b')    
            bCtl = 0 # break
        #endif
    #wend
#end b

def main(startpoint,trace='off'):
    global p
    p = {}
    p['v'] = {} # nds
    p['v']['trace'] = trace
    if ( p['v']['trace'] != 'off'):
        print('begin main')
    #endif
    p['dat'] = [] # data stack
    p['r'] = [] # r stack
    p['l'] = {} # lib table
    p['sy'] = {} # symbol table
    p['sy']['pop'] = datPop
    p['sy']['push'] = datPush
    prepSy()
    p['OK'] = 'pOK'
    p['NOK'] = 'pNOK'

    # paragraph Tstart
    p['sy']['Tstart'] = Tstart
    #

    # paragraph a
    p['sy']['a'] = a
    #

    # paragraph b
    p['sy']['b'] = b
    #

    p['sy']['start'] = p['sy'][startpoint] 
#end main
def start(trace='off'):
    p['v']['trace'] = trace # save trace setting
    p['sy']['start'](trace) # process begins at start
#end start

# helper rtns 
def logg(strin):
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input(strin)  
    #endif
#end logg
def chk(ctl):
    # tests ok/nok/tail of verb return to adjust ctl 
    global p
    okn = p['sy']['pop']()
    logg('chk-okn ' + okn.__str__())
    if (okn == 'tail.'):
        ans = 1
    elif (okn == p['NOK']):
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

