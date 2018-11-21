
#file s2a.py
#generated for s2.txt 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def SMain_1():
    global p
    logg('SMain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- Script file -- ') 
    if (r == p['OK']):
        logg('push text Script file ')
        datPush("Script file")
        logg('after Script file ')
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
    logg('processing text -- SCFile -- ') 
    if (r == p['OK']):
        logg('push text SCFile ')
        datPush("SCFile")
        logg('after SCFile ')
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
    logg('processing verb ( dumpNDS ) ')
    if (r == p['OK']):
        logg('call dumpNDS ')
        p['sy']['dumpNDS'](p)
        logg('after dumpNDS')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( init_s2a ) ')
    if (r == p['OK']):
        logg('call init_s2a ')
        p['sy']['init_s2a'](p)
        logg('after init_s2a')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( Smain2 ) ')
    if (r == p['OK']):
        logg('call Smain2 ')
        p['sy']['Smain2'](p)
        logg('after Smain2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final SMain_1')
#end SMain_1

def SMain (x):
    global p
    logg('begin SMain')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    SMainCtl = 1 # starting spoke
    while SMainCtl != 0:
        logg('loop SMainCtl = ' + SMainCtl.__str__())
        if (SMainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (SMainCtl == 1):
            logg('call SMain_1')
            SMain_1()
            logg('after call SMain_1')
            # test and adjust for new spoke
            SMainCtl = chk(SMainCtl)

        else:
            #final
            logg('final SMain')    
            SMainCtl = 0 # break
        #endif
    #wend
#end SMain

def Smain2_1():
    global p
    logg('Smain2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==screen ) ')
    if (r == p['OK']):
        logg('call ==screen ')
        p['sy']['==screen'](p)
        logg('after ==screen')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ==(( ) ')
    if (r == p['OK']):
        logg('call ==(( ')
        p['sy']['==(('](p)
        logg('after ==((')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( lineStuffs ) ')
    if (r == p['OK']):
        logg('call lineStuffs ')
        p['sy']['lineStuffs'](p)
        logg('after lineStuffs')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ==)) ) ')
    if (r == p['OK']):
        logg('call ==)) ')
        p['sy']['==))'](p)
        logg('after ==))')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( dumpNDS ) ')
    if (r == p['OK']):
        logg('call dumpNDS ')
        p['sy']['dumpNDS'](p)
        logg('after dumpNDS')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Smain2_1')
#end Smain2_1

def Smain2_2():
    global p
    logg('Smain2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==;; ) ')
    if (r == p['OK']):
        logg('call ==;; ')
        p['sy']['==;;'](p)
        logg('after ==;;')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Smain2_2')
#end Smain2_2

def Smain2 (x):
    global p
    logg('begin Smain2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    Smain2Ctl = 1 # starting spoke
    while Smain2Ctl != 0:
        logg('loop Smain2Ctl = ' + Smain2Ctl.__str__())
        if (Smain2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (Smain2Ctl == 1):
            logg('call Smain2_1')
            Smain2_1()
            logg('after call Smain2_1')
            # test and adjust for new spoke
            Smain2Ctl = chk(Smain2Ctl)

        elif (Smain2Ctl == 2):
            logg('call Smain2_2')
            Smain2_2()
            logg('after call Smain2_2')
            # test and adjust for new spoke
            Smain2Ctl = chk(Smain2Ctl)

        else:
            #final
            logg('final Smain2')    
            Smain2Ctl = 0 # break
        #endif
    #wend
#end Smain2

def lineStuffs_1():
    global p
    logg('lineStuffs_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( lineStuff ) ')
    if (r == p['OK']):
        logg('call lineStuff ')
        p['sy']['lineStuff'](p)
        logg('after lineStuff')
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
    logg('final lineStuffs_1')
#end lineStuffs_1

def lineStuffs_2():
    global p
    logg('lineStuffs_2')
    datPush(p['OK'])

    #final
    logg('final lineStuffs_2')
#end lineStuffs_2

def lineStuffs (x):
    global p
    logg('begin lineStuffs')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    lineStuffsCtl = 1 # starting spoke
    while lineStuffsCtl != 0:
        logg('loop lineStuffsCtl = ' + lineStuffsCtl.__str__())
        if (lineStuffsCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (lineStuffsCtl == 1):
            logg('call lineStuffs_1')
            lineStuffs_1()
            logg('after call lineStuffs_1')
            # test and adjust for new spoke
            lineStuffsCtl = chk(lineStuffsCtl)

        elif (lineStuffsCtl == 2):
            logg('call lineStuffs_2')
            lineStuffs_2()
            logg('after call lineStuffs_2')
            # test and adjust for new spoke
            lineStuffsCtl = chk(lineStuffsCtl)

        else:
            #final
            logg('final lineStuffs')    
            lineStuffsCtl = 0 # break
        #endif
    #wend
#end lineStuffs

def lineStuff_1():
    global p
    logg('lineStuff_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==line ) ')
    if (r == p['OK']):
        logg('call ==line ')
        p['sy']['==line'](p)
        logg('after ==line')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ==( ) ')
    if (r == p['OK']):
        logg('call ==( ')
        p['sy']['==('](p)
        logg('after ==(')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( lineNumStuffs ) ')
    if (r == p['OK']):
        logg('call lineNumStuffs ')
        p['sy']['lineNumStuffs'](p)
        logg('after lineNumStuffs')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ==) ) ')
    if (r == p['OK']):
        logg('call ==) ')
        p['sy']['==)'](p)
        logg('after ==)')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( dumpNDS ) ')
    if (r == p['OK']):
        logg('call dumpNDS ')
        p['sy']['dumpNDS'](p)
        logg('after dumpNDS')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final lineStuff_1')
#end lineStuff_1

def lineStuff_2():
    global p
    logg('lineStuff_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==attributes ) ')
    if (r == p['OK']):
        logg('call ==attributes ')
        p['sy']['==attributes'](p)
        logg('after ==attributes')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( dumpNDS ) ')
    if (r == p['OK']):
        logg('call dumpNDS ')
        p['sy']['dumpNDS'](p)
        logg('after dumpNDS')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final lineStuff_2')
#end lineStuff_2

def lineStuff_3():
    global p
    logg('lineStuff_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==sendList ) ')
    if (r == p['OK']):
        logg('call ==sendList ')
        p['sy']['==sendList'](p)
        logg('after ==sendList')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( dumpNDS ) ')
    if (r == p['OK']):
        logg('call dumpNDS ')
        p['sy']['dumpNDS'](p)
        logg('after dumpNDS')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final lineStuff_3')
#end lineStuff_3

def lineStuff (x):
    global p
    logg('begin lineStuff')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    lineStuffCtl = 1 # starting spoke
    while lineStuffCtl != 0:
        logg('loop lineStuffCtl = ' + lineStuffCtl.__str__())
        if (lineStuffCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (lineStuffCtl == 1):
            logg('call lineStuff_1')
            lineStuff_1()
            logg('after call lineStuff_1')
            # test and adjust for new spoke
            lineStuffCtl = chk(lineStuffCtl)

        elif (lineStuffCtl == 2):
            logg('call lineStuff_2')
            lineStuff_2()
            logg('after call lineStuff_2')
            # test and adjust for new spoke
            lineStuffCtl = chk(lineStuffCtl)

        elif (lineStuffCtl == 3):
            logg('call lineStuff_3')
            lineStuff_3()
            logg('after call lineStuff_3')
            # test and adjust for new spoke
            lineStuffCtl = chk(lineStuffCtl)

        else:
            #final
            logg('final lineStuff')    
            lineStuffCtl = 0 # break
        #endif
    #wend
#end lineStuff

def lineNumStuffs_1():
    global p
    logg('lineNumStuffs_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( pos0 ) ')
    if (r == p['OK']):
        logg('call pos0 ')
        p['sy']['pos0'](p)
        logg('after pos0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( lineNumStuff ) ')
    if (r == p['OK']):
        logg('call lineNumStuff ')
        p['sy']['lineNumStuff'](p)
        logg('after lineNumStuff')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( lineNumStuff2 ) ')
    if (r == p['OK']):
        logg('call lineNumStuff2 ')
        p['sy']['lineNumStuff2'](p)
        logg('after lineNumStuff2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ; ) ')
    if (r == p['OK']):
        logg('call ; ')
        p['sy'][';'](p)
        logg('after ;')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( pos0 ) ')
    if (r == p['OK']):
        logg('call pos0 ')
        p['sy']['pos0'](p)
        logg('after pos0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( :- ) ')
    if (r == p['OK']):
        logg('call :- ')
        p['sy'][':-'](p)
        logg('after :-')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( [[ ) ')
    if (r == p['OK']):
        logg('call [[ ')
        p['sy']['[['](p)
        logg('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( 1 ) ')
    if (r == p['OK']):
        logg('call 1 ')
        p['sy']['1'](p)
        logg('after 1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ]] ) ')
    if (r == p['OK']):
        logg('call ]] ')
        p['sy'][']]'](p)
        logg('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- 0 -- ') 
    if (r == p['OK']):
        logg('push text 0 ')
        datPush("0")
        logg('after 0 ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- pos -- ') 
    if (r == p['OK']):
        logg('push text pos ')
        datPush("pos")
        logg('after pos ')
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

    #final
    logg('final lineNumStuffs_1')
#end lineNumStuffs_1

def lineNumStuffs (x):
    global p
    logg('begin lineNumStuffs')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    lineNumStuffsCtl = 1 # starting spoke
    while lineNumStuffsCtl != 0:
        logg('loop lineNumStuffsCtl = ' + lineNumStuffsCtl.__str__())
        if (lineNumStuffsCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (lineNumStuffsCtl == 1):
            logg('call lineNumStuffs_1')
            lineNumStuffs_1()
            logg('after call lineNumStuffs_1')
            # test and adjust for new spoke
            lineNumStuffsCtl = chk(lineNumStuffsCtl)

        else:
            #final
            logg('final lineNumStuffs')    
            lineNumStuffsCtl = 0 # break
        #endif
    #wend
#end lineNumStuffs

def lineNumStuff_0():
    global p
    logg('lineNumStuff_0')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( pos1 ) ')
    if (r == p['OK']):
        logg('call pos1 ')
        p['sy']['pos1'](p)
        logg('after pos1')
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

    r = p['sy']['pop']()
    logg('processing verb ( [[ ) ')
    if (r == p['OK']):
        logg('call [[ ')
        p['sy']['[['](p)
        logg('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( 1 ) ')
    if (r == p['OK']):
        logg('call 1 ')
        p['sy']['1'](p)
        logg('after 1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ]] ) ')
    if (r == p['OK']):
        logg('call ]] ')
        p['sy'][']]'](p)
        logg('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ==E ) ')
    if (r == p['OK']):
        logg('call ==E ')
        p['sy']['==E'](p)
        logg('after ==E')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( EAct ) ')
    if (r == p['OK']):
        logg('call EAct ')
        p['sy']['EAct'](p)
        logg('after EAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final lineNumStuff_0')
#end lineNumStuff_0

def lineNumStuff_2():
    global p
    logg('lineNumStuff_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( LAct ) ')
    if (r == p['OK']):
        logg('call LAct ')
        p['sy']['LAct'](p)
        logg('after LAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final lineNumStuff_2')
#end lineNumStuff_2

def lineNumStuff (x):
    global p
    logg('begin lineNumStuff')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    lineNumStuffCtl = 1 # starting spoke
    while lineNumStuffCtl != 0:
        logg('loop lineNumStuffCtl = ' + lineNumStuffCtl.__str__())
        if (lineNumStuffCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (lineNumStuffCtl == 1):
            logg('call lineNumStuff_0')
            lineNumStuff_0()
            logg('after call lineNumStuff_0')
            # test and adjust for new spoke
            lineNumStuffCtl = chk(lineNumStuffCtl)

        elif (lineNumStuffCtl == 2):
            logg('call lineNumStuff_2')
            lineNumStuff_2()
            logg('after call lineNumStuff_2')
            # test and adjust for new spoke
            lineNumStuffCtl = chk(lineNumStuffCtl)

        else:
            #final
            logg('final lineNumStuff')    
            lineNumStuffCtl = 0 # break
        #endif
    #wend
#end lineNumStuff

def lineNumStuff2_1():
    global p
    logg('lineNumStuff2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==, ) ')
    if (r == p['OK']):
        logg('call ==, ')
        p['sy']['==,'](p)
        logg('after ==,')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( lineNumStuff ) ')
    if (r == p['OK']):
        logg('call lineNumStuff ')
        p['sy']['lineNumStuff'](p)
        logg('after lineNumStuff')
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
    logg('final lineNumStuff2_1')
#end lineNumStuff2_1

def lineNumStuff2_2():
    global p
    logg('lineNumStuff2_2')
    datPush(p['OK'])

    #final
    logg('final lineNumStuff2_2')
#end lineNumStuff2_2

def lineNumStuff2 (x):
    global p
    logg('begin lineNumStuff2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    lineNumStuff2Ctl = 1 # starting spoke
    while lineNumStuff2Ctl != 0:
        logg('loop lineNumStuff2Ctl = ' + lineNumStuff2Ctl.__str__())
        if (lineNumStuff2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (lineNumStuff2Ctl == 1):
            logg('call lineNumStuff2_1')
            lineNumStuff2_1()
            logg('after call lineNumStuff2_1')
            # test and adjust for new spoke
            lineNumStuff2Ctl = chk(lineNumStuff2Ctl)

        elif (lineNumStuff2Ctl == 2):
            logg('call lineNumStuff2_2')
            lineNumStuff2_2()
            logg('after call lineNumStuff2_2')
            # test and adjust for new spoke
            lineNumStuff2Ctl = chk(lineNumStuff2Ctl)

        else:
            #final
            logg('final lineNumStuff2')    
            lineNumStuff2Ctl = 0 # break
        #endif
    #wend
#end lineNumStuff2

def EAct_1():
    global p
    logg('EAct_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( dumpNDS ) ')
    if (r == p['OK']):
        logg('call dumpNDS ')
        p['sy']['dumpNDS'](p)
        logg('after dumpNDS')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final EAct_1')
#end EAct_1

def EAct (x):
    global p
    logg('begin EAct')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    EActCtl = 1 # starting spoke
    while EActCtl != 0:
        logg('loop EActCtl = ' + EActCtl.__str__())
        if (EActCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (EActCtl == 1):
            logg('call EAct_1')
            EAct_1()
            logg('after call EAct_1')
            # test and adjust for new spoke
            EActCtl = chk(EActCtl)

        else:
            #final
            logg('final EAct')    
            EActCtl = 0 # break
        #endif
    #wend
#end EAct

def LAct_1():
    global p
    logg('LAct_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( dumpNDS ) ')
    if (r == p['OK']):
        logg('call dumpNDS ')
        p['sy']['dumpNDS'](p)
        logg('after dumpNDS')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final LAct_1')
#end LAct_1

def LAct (x):
    global p
    logg('begin LAct')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    LActCtl = 1 # starting spoke
    while LActCtl != 0:
        logg('loop LActCtl = ' + LActCtl.__str__())
        if (LActCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (LActCtl == 1):
            logg('call LAct_1')
            LAct_1()
            logg('after call LAct_1')
            # test and adjust for new spoke
            LActCtl = chk(LActCtl)

        else:
            #final
            logg('final LAct')    
            LActCtl = 0 # break
        #endif
    #wend
#end LAct

def pos1_1():
    global p
    logg('pos1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- pos -- ') 
    if (r == p['OK']):
        logg('push text pos ')
        datPush("pos")
        logg('after pos ')
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
    logg('processing verb ( + ) ')
    if (r == p['OK']):
        logg('call + ')
        p['sy']['+'](p)
        logg('after +')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- pos -- ') 
    if (r == p['OK']):
        logg('push text pos ')
        datPush("pos")
        logg('after pos ')
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

    #final
    logg('final pos1_1')
#end pos1_1

def pos1 (x):
    global p
    logg('begin pos1')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    pos1Ctl = 1 # starting spoke
    while pos1Ctl != 0:
        logg('loop pos1Ctl = ' + pos1Ctl.__str__())
        if (pos1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (pos1Ctl == 1):
            logg('call pos1_1')
            pos1_1()
            logg('after call pos1_1')
            # test and adjust for new spoke
            pos1Ctl = chk(pos1Ctl)

        else:
            #final
            logg('final pos1')    
            pos1Ctl = 0 # break
        #endif
    #wend
#end pos1

# stream routines 

def EQscreen(p):
    logg ('==screen')
    needle = 'screen'
    needle = needle.upper()
    return(eqeq(needle))
#end EQscreen

def MSName(p):
    logg ('<<<<SName>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<SName>>'] = j
#endif MSName

def EQ_OP__OP_(p):
    logg ('==((')
    needle = '(('
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_OP__OP_

def EQ_CP__CP_(p):
    logg ('==))')
    needle = '))'
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_CP__CP_

def EQ_SC__SC_(p):
    logg ('==;;')
    needle = ';;'
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_SC__SC_

def EQline(p):
    logg ('==line')
    needle = 'line'
    needle = needle.upper()
    return(eqeq(needle))
#end EQline

def MLineNum(p):
    logg ('<<<<LineNum>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<LineNum>>'] = j
#endif MLineNum

def EQ_OP_(p):
    logg ('==(')
    needle = '('
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_OP_

def EQ_CP_(p):
    logg ('==)')
    needle = ')'
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_CP_

def EQattributes(p):
    logg ('==attributes')
    needle = 'attributes'
    needle = needle.upper()
    return(eqeq(needle))
#end EQattributes

def EQsendList(p):
    logg ('==sendList')
    needle = 'sendList'
    needle = needle.upper()
    return(eqeq(needle))
#end EQsendList

def EQE(p):
    logg ('==E')
    needle = 'E'
    needle = needle.upper()
    return(eqeq(needle))
#end EQE

def MEname(p):
    logg ('<<<<Ename>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<Ename>>'] = j
#endif MEname

def MLitValue(p):
    logg ('<<<<LitValue>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<LitValue>>'] = j
#endif MLitValue

def EQ_C_(p):
    logg ('==,')
    needle = ','
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_C_

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

    # paragraph SMain
    p['sy']['SMain'] = SMain
    #

    # paragraph Smain2
    p['sy']['Smain2'] = Smain2
    #

    # paragraph ==screen
    p['sy']['==screen'] = EQscreen
    #

    # paragraph <<SName>>
    p['sy']['<<SName>>'] = MSName
    #

    # paragraph ==((
    p['sy']['==(('] = EQ_OP__OP_
    #

    # paragraph ==))
    p['sy']['==))'] = EQ_CP__CP_
    #

    # paragraph ==;;
    p['sy']['==;;'] = EQ_SC__SC_
    #

    # paragraph lineStuffs
    p['sy']['lineStuffs'] = lineStuffs
    #

    # paragraph lineStuff
    p['sy']['lineStuff'] = lineStuff
    #

    # paragraph ==line
    p['sy']['==line'] = EQline
    #

    # paragraph <<LineNum>>
    p['sy']['<<LineNum>>'] = MLineNum
    #

    # paragraph ==(
    p['sy']['==('] = EQ_OP_
    #

    # paragraph ==)
    p['sy']['==)'] = EQ_CP_
    #

    # paragraph ==attributes
    p['sy']['==attributes'] = EQattributes
    #

    # paragraph ==sendList
    p['sy']['==sendList'] = EQsendList
    #

    # paragraph lineNumStuffs
    p['sy']['lineNumStuffs'] = lineNumStuffs
    #

    # paragraph lineNumStuff
    p['sy']['lineNumStuff'] = lineNumStuff
    #

    # paragraph ==E
    p['sy']['==E'] = EQE
    #

    # paragraph <<Ename>>
    p['sy']['<<Ename>>'] = MEname
    #

    # paragraph <<LitValue>>
    p['sy']['<<LitValue>>'] = MLitValue
    #

    # paragraph lineNumStuff2
    p['sy']['lineNumStuff2'] = lineNumStuff2
    #

    # paragraph ==,
    p['sy']['==,'] = EQ_C_
    #

    # paragraph EAct
    p['sy']['EAct'] = EAct
    #

    # paragraph LAct
    p['sy']['LAct'] = LAct
    #

    # paragraph pos1
    p['sy']['pos1'] = pos1
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

