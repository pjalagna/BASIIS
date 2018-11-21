
#file t2018.py
#generated for t11.txt 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def tr_1():
    global p
    logg('tr_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- hello -- ') 
    if (r == p['OK']):
        logg('push text hello ')
        datPush("hello")
        logg('after hello ')
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
    logg('final tr_1')
#end tr_1

def tr_2():
    global p
    logg('tr_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- again -- ') 
    if (r == p['OK']):
        logg('push text again ')
        datPush("again")
        logg('after again ')
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
    logg('final tr_2')
#end tr_2

def tr (x):
    global p
    logg('begin tr')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    trCtl = 1 # starting spoke
    while trCtl != 0:
        logg('loop trCtl = ' + trCtl.__str__())
        if (trCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (trCtl == 1):
            logg('call tr_1')
            tr_1()
            logg('after call tr_1')
            # test and adjust for new spoke
            trCtl = chk(trCtl)

        elif (trCtl == 2):
            logg('call tr_2')
            tr_2()
            logg('after call tr_2')
            # test and adjust for new spoke
            trCtl = chk(trCtl)

        else:
            #final
            logg('final tr')    
            trCtl = 0 # break
        #endif
    #wend
#end tr

# stream routines 

# END stream routines 

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

    # paragraph tr
    p['sy']['tr'] = tr
    #

    p['sy']['start'] = p['sy'][startpoint] 
#end main
def start(trace='off'):
    p['v']['trace'] = trace # save trace setting
    p['sy']['start'](trace) # process begins at start
#end start

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

