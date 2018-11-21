
#file ScreenProto.py
#generated for screenBNF.txt 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def Smain_1():
    global p
    logg('Smain_1')
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
    logg('processing verb ( screenStuffs ) ')
    if (r == p['OK']):
        logg('call screenStuffs ')
        p['sy']['screenStuffs'](p)
        logg('after screenStuffs')
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
    logg('processing verb ( screenAct ) ')
    if (r == p['OK']):
        logg('call screenAct ')
        p['sy']['screenAct'](p)
        logg('after screenAct')
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
    logg('final Smain_1')
#end Smain_1

def Smain_2():
    global p
    logg('Smain_2')
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

    r = p['sy']['pop']()
    logg('processing verb ( finalAct ) ')
    if (r == p['OK']):
        logg('call finalAct ')
        p['sy']['finalAct'](p)
        logg('after finalAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Smain_2')
#end Smain_2

def Smain (x):
    global p
    logg('begin Smain')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    SmainCtl = 1 # starting spoke
    while SmainCtl != 0:
        logg('loop SmainCtl = ' + SmainCtl.__str__())
        if (SmainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (SmainCtl == 1):
            logg('call Smain_1')
            Smain_1()
            logg('after call Smain_1')
            # test and adjust for new spoke
            SmainCtl = chk(SmainCtl)

        elif (SmainCtl == 2):
            logg('call Smain_2')
            Smain_2()
            logg('after call Smain_2')
            # test and adjust for new spoke
            SmainCtl = chk(SmainCtl)

        else:
            #final
            logg('final Smain')    
            SmainCtl = 0 # break
        #endif
    #wend
#end Smain

def screenStuffs_1():
    global p
    logg('screenStuffs_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( screenStuff ) ')
    if (r == p['OK']):
        logg('call screenStuff ')
        p['sy']['screenStuff'](p)
        logg('after screenStuff')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( screenStuff2 ) ')
    if (r == p['OK']):
        logg('call screenStuff2 ')
        p['sy']['screenStuff2'](p)
        logg('after screenStuff2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final screenStuffs_1')
#end screenStuffs_1

def screenStuffs (x):
    global p
    logg('begin screenStuffs')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    screenStuffsCtl = 1 # starting spoke
    while screenStuffsCtl != 0:
        logg('loop screenStuffsCtl = ' + screenStuffsCtl.__str__())
        if (screenStuffsCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (screenStuffsCtl == 1):
            logg('call screenStuffs_1')
            screenStuffs_1()
            logg('after call screenStuffs_1')
            # test and adjust for new spoke
            screenStuffsCtl = chk(screenStuffsCtl)

        else:
            #final
            logg('final screenStuffs')    
            screenStuffsCtl = 0 # break
        #endif
    #wend
#end screenStuffs

def screenStuff_1():
    global p
    logg('screenStuff_1')
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
    logg('processing verb ( lineFinalAct ) ')
    if (r == p['OK']):
        logg('call lineFinalAct ')
        p['sy']['lineFinalAct'](p)
        logg('after lineFinalAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final screenStuff_1')
#end screenStuff_1

def screenStuff_2():
    global p
    logg('screenStuff_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==script ) ')
    if (r == p['OK']):
        logg('call ==script ')
        p['sy']['==script'](p)
        logg('after ==script')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( scriptStuff ) ')
    if (r == p['OK']):
        logg('call scriptStuff ')
        p['sy']['scriptStuff'](p)
        logg('after scriptStuff')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final screenStuff_2')
#end screenStuff_2

def screenStuff_3():
    global p
    logg('screenStuff_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==attribute ) ')
    if (r == p['OK']):
        logg('call ==attribute ')
        p['sy']['==attribute'](p)
        logg('after ==attribute')
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
    logg('processing verb ( AStuffs ) ')
    if (r == p['OK']):
        logg('call AStuffs ')
        p['sy']['AStuffs'](p)
        logg('after AStuffs')
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
    logg('processing verb ( ARecAct ) ')
    if (r == p['OK']):
        logg('call ARecAct ')
        p['sy']['ARecAct'](p)
        logg('after ARecAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final screenStuff_3')
#end screenStuff_3

def screenStuff_4():
    global p
    logg('screenStuff_4')
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
    logg('processing verb ( sendStuffs ) ')
    if (r == p['OK']):
        logg('call sendStuffs ')
        p['sy']['sendStuffs'](p)
        logg('after sendStuffs')
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
    logg('processing verb ( sendListAct ) ')
    if (r == p['OK']):
        logg('call sendListAct ')
        p['sy']['sendListAct'](p)
        logg('after sendListAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final screenStuff_4')
#end screenStuff_4

def screenStuff (x):
    global p
    logg('begin screenStuff')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    screenStuffCtl = 1 # starting spoke
    while screenStuffCtl != 0:
        logg('loop screenStuffCtl = ' + screenStuffCtl.__str__())
        if (screenStuffCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (screenStuffCtl == 1):
            logg('call screenStuff_1')
            screenStuff_1()
            logg('after call screenStuff_1')
            # test and adjust for new spoke
            screenStuffCtl = chk(screenStuffCtl)

        elif (screenStuffCtl == 2):
            logg('call screenStuff_2')
            screenStuff_2()
            logg('after call screenStuff_2')
            # test and adjust for new spoke
            screenStuffCtl = chk(screenStuffCtl)

        elif (screenStuffCtl == 3):
            logg('call screenStuff_3')
            screenStuff_3()
            logg('after call screenStuff_3')
            # test and adjust for new spoke
            screenStuffCtl = chk(screenStuffCtl)

        elif (screenStuffCtl == 4):
            logg('call screenStuff_4')
            screenStuff_4()
            logg('after call screenStuff_4')
            # test and adjust for new spoke
            screenStuffCtl = chk(screenStuffCtl)

        else:
            #final
            logg('final screenStuff')    
            screenStuffCtl = 0 # break
        #endif
    #wend
#end screenStuff

def screenStuff2_1():
    global p
    logg('screenStuff2_1')
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
    logg('processing verb ( screenStuff ) ')
    if (r == p['OK']):
        logg('call screenStuff ')
        p['sy']['screenStuff'](p)
        logg('after screenStuff')
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
    logg('final screenStuff2_1')
#end screenStuff2_1

def screenStuff2_2():
    global p
    logg('screenStuff2_2')
    datPush(p['OK'])

    #final
    logg('final screenStuff2_2')
#end screenStuff2_2

def screenStuff2 (x):
    global p
    logg('begin screenStuff2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    screenStuff2Ctl = 1 # starting spoke
    while screenStuff2Ctl != 0:
        logg('loop screenStuff2Ctl = ' + screenStuff2Ctl.__str__())
        if (screenStuff2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (screenStuff2Ctl == 1):
            logg('call screenStuff2_1')
            screenStuff2_1()
            logg('after call screenStuff2_1')
            # test and adjust for new spoke
            screenStuff2Ctl = chk(screenStuff2Ctl)

        elif (screenStuff2Ctl == 2):
            logg('call screenStuff2_2')
            screenStuff2_2()
            logg('after call screenStuff2_2')
            # test and adjust for new spoke
            screenStuff2Ctl = chk(screenStuff2Ctl)

        else:
            #final
            logg('final screenStuff2')    
            screenStuff2Ctl = 0 # break
        #endif
    #wend
#end screenStuff2

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
    logg('processing verb ( lineStuff2 ) ')
    if (r == p['OK']):
        logg('call lineStuff2 ')
        p['sy']['lineStuff2'](p)
        logg('after lineStuff2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final lineStuffs_1')
#end lineStuffs_1

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
    logg('processing verb ( ==fn ) ')
    if (r == p['OK']):
        logg('call ==fn ')
        p['sy']['==fn'](p)
        logg('after ==fn')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( fnAct ) ')
    if (r == p['OK']):
        logg('call fnAct ')
        p['sy']['fnAct'](p)
        logg('after fnAct')
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
    logg('processing verb ( ==: ) ')
    if (r == p['OK']):
        logg('call ==: ')
        p['sy']['==:'](p)
        logg('after ==:')
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
    logg('final lineStuff_2')
#end lineStuff_2

def lineStuff_3():
    global p
    logg('lineStuff_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( LitAct ) ')
    if (r == p['OK']):
        logg('call LitAct ')
        p['sy']['LitAct'](p)
        logg('after LitAct')
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

def lineStuff2_1():
    global p
    logg('lineStuff2_1')
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
    logg('final lineStuff2_1')
#end lineStuff2_1

def lineStuff2_2():
    global p
    logg('lineStuff2_2')
    datPush(p['OK'])

    #final
    logg('final lineStuff2_2')
#end lineStuff2_2

def lineStuff2 (x):
    global p
    logg('begin lineStuff2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    lineStuff2Ctl = 1 # starting spoke
    while lineStuff2Ctl != 0:
        logg('loop lineStuff2Ctl = ' + lineStuff2Ctl.__str__())
        if (lineStuff2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (lineStuff2Ctl == 1):
            logg('call lineStuff2_1')
            lineStuff2_1()
            logg('after call lineStuff2_1')
            # test and adjust for new spoke
            lineStuff2Ctl = chk(lineStuff2Ctl)

        elif (lineStuff2Ctl == 2):
            logg('call lineStuff2_2')
            lineStuff2_2()
            logg('after call lineStuff2_2')
            # test and adjust for new spoke
            lineStuff2Ctl = chk(lineStuff2Ctl)

        else:
            #final
            logg('final lineStuff2')    
            lineStuff2Ctl = 0 # break
        #endif
    #wend
#end lineStuff2

def AStuffs_1():
    global p
    logg('AStuffs_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( AStuff ) ')
    if (r == p['OK']):
        logg('call AStuff ')
        p['sy']['AStuff'](p)
        logg('after AStuff')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( AStuff2 ) ')
    if (r == p['OK']):
        logg('call AStuff2 ')
        p['sy']['AStuff2'](p)
        logg('after AStuff2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final AStuffs_1')
#end AStuffs_1

def AStuffs (x):
    global p
    logg('begin AStuffs')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    AStuffsCtl = 1 # starting spoke
    while AStuffsCtl != 0:
        logg('loop AStuffsCtl = ' + AStuffsCtl.__str__())
        if (AStuffsCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (AStuffsCtl == 1):
            logg('call AStuffs_1')
            AStuffs_1()
            logg('after call AStuffs_1')
            # test and adjust for new spoke
            AStuffsCtl = chk(AStuffsCtl)

        else:
            #final
            logg('final AStuffs')    
            AStuffsCtl = 0 # break
        #endif
    #wend
#end AStuffs

def AStuff_1():
    global p
    logg('AStuff_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( === ) ')
    if (r == p['OK']):
        logg('call === ')
        p['sy']['==='](p)
        logg('after ===')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( CVAct ) ')
    if (r == p['OK']):
        logg('call CVAct ')
        p['sy']['CVAct'](p)
        logg('after CVAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final AStuff_1')
#end AStuff_1

def AStuff (x):
    global p
    logg('begin AStuff')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    AStuffCtl = 1 # starting spoke
    while AStuffCtl != 0:
        logg('loop AStuffCtl = ' + AStuffCtl.__str__())
        if (AStuffCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (AStuffCtl == 1):
            logg('call AStuff_1')
            AStuff_1()
            logg('after call AStuff_1')
            # test and adjust for new spoke
            AStuffCtl = chk(AStuffCtl)

        else:
            #final
            logg('final AStuff')    
            AStuffCtl = 0 # break
        #endif
    #wend
#end AStuff

def AStuff2_1():
    global p
    logg('AStuff2_1')
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
    logg('processing verb ( AStuff ) ')
    if (r == p['OK']):
        logg('call AStuff ')
        p['sy']['AStuff'](p)
        logg('after AStuff')
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
    logg('final AStuff2_1')
#end AStuff2_1

def AStuff2_2():
    global p
    logg('AStuff2_2')
    datPush(p['OK'])

    #final
    logg('final AStuff2_2')
#end AStuff2_2

def AStuff2 (x):
    global p
    logg('begin AStuff2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    AStuff2Ctl = 1 # starting spoke
    while AStuff2Ctl != 0:
        logg('loop AStuff2Ctl = ' + AStuff2Ctl.__str__())
        if (AStuff2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (AStuff2Ctl == 1):
            logg('call AStuff2_1')
            AStuff2_1()
            logg('after call AStuff2_1')
            # test and adjust for new spoke
            AStuff2Ctl = chk(AStuff2Ctl)

        elif (AStuff2Ctl == 2):
            logg('call AStuff2_2')
            AStuff2_2()
            logg('after call AStuff2_2')
            # test and adjust for new spoke
            AStuff2Ctl = chk(AStuff2Ctl)

        else:
            #final
            logg('final AStuff2')    
            AStuff2Ctl = 0 # break
        #endif
    #wend
#end AStuff2

def scriptStuff_1():
    global p
    logg('scriptStuff_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==begin ) ')
    if (r == p['OK']):
        logg('call ==begin ')
        p['sy']['==begin'](p)
        logg('after ==begin')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( textNotNameEnd ) ')
    if (r == p['OK']):
        logg('call textNotNameEnd ')
        p['sy']['textNotNameEnd'](p)
        logg('after textNotNameEnd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ==end ) ')
    if (r == p['OK']):
        logg('call ==end ')
        p['sy']['==end'](p)
        logg('after ==end')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( addJSLibAct ) ')
    if (r == p['OK']):
        logg('call addJSLibAct ')
        p['sy']['addJSLibAct'](p)
        logg('after addJSLibAct')
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
    logg('final scriptStuff_1')
#end scriptStuff_1

def scriptStuff_2():
    global p
    logg('scriptStuff_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==include ) ')
    if (r == p['OK']):
        logg('call ==include ')
        p['sy']['==include'](p)
        logg('after ==include')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( JSFileAct ) ')
    if (r == p['OK']):
        logg('call JSFileAct ')
        p['sy']['JSFileAct'](p)
        logg('after JSFileAct')
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
    logg('final scriptStuff_2')
#end scriptStuff_2

def scriptStuff_3():
    global p
    logg('scriptStuff_3')
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
    logg('final scriptStuff_3')
#end scriptStuff_3

def scriptStuff_4():
    global p
    logg('scriptStuff_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==use ) ')
    if (r == p['OK']):
        logg('call ==use ')
        p['sy']['==use'](p)
        logg('after ==use')
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
    logg('final scriptStuff_4')
#end scriptStuff_4

def scriptStuff (x):
    global p
    logg('begin scriptStuff')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    scriptStuffCtl = 1 # starting spoke
    while scriptStuffCtl != 0:
        logg('loop scriptStuffCtl = ' + scriptStuffCtl.__str__())
        if (scriptStuffCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (scriptStuffCtl == 1):
            logg('call scriptStuff_1')
            scriptStuff_1()
            logg('after call scriptStuff_1')
            # test and adjust for new spoke
            scriptStuffCtl = chk(scriptStuffCtl)

        elif (scriptStuffCtl == 2):
            logg('call scriptStuff_2')
            scriptStuff_2()
            logg('after call scriptStuff_2')
            # test and adjust for new spoke
            scriptStuffCtl = chk(scriptStuffCtl)

        elif (scriptStuffCtl == 3):
            logg('call scriptStuff_3')
            scriptStuff_3()
            logg('after call scriptStuff_3')
            # test and adjust for new spoke
            scriptStuffCtl = chk(scriptStuffCtl)

        elif (scriptStuffCtl == 4):
            logg('call scriptStuff_4')
            scriptStuff_4()
            logg('after call scriptStuff_4')
            # test and adjust for new spoke
            scriptStuffCtl = chk(scriptStuffCtl)

        else:
            #final
            logg('final scriptStuff')    
            scriptStuffCtl = 0 # break
        #endif
    #wend
#end scriptStuff

def sendStuffs_1():
    global p
    logg('sendStuffs_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( sendStuff ) ')
    if (r == p['OK']):
        logg('call sendStuff ')
        p['sy']['sendStuff'](p)
        logg('after sendStuff')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( sendStuff2 ) ')
    if (r == p['OK']):
        logg('call sendStuff2 ')
        p['sy']['sendStuff2'](p)
        logg('after sendStuff2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final sendStuffs_1')
#end sendStuffs_1

def sendStuffs (x):
    global p
    logg('begin sendStuffs')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    sendStuffsCtl = 1 # starting spoke
    while sendStuffsCtl != 0:
        logg('loop sendStuffsCtl = ' + sendStuffsCtl.__str__())
        if (sendStuffsCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (sendStuffsCtl == 1):
            logg('call sendStuffs_1')
            sendStuffs_1()
            logg('after call sendStuffs_1')
            # test and adjust for new spoke
            sendStuffsCtl = chk(sendStuffsCtl)

        else:
            #final
            logg('final sendStuffs')    
            sendStuffsCtl = 0 # break
        #endif
    #wend
#end sendStuffs

def sendStuff_1():
    global p
    logg('sendStuff_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( sendAct ) ')
    if (r == p['OK']):
        logg('call sendAct ')
        p['sy']['sendAct'](p)
        logg('after sendAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final sendStuff_1')
#end sendStuff_1

def sendStuff (x):
    global p
    logg('begin sendStuff')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    sendStuffCtl = 1 # starting spoke
    while sendStuffCtl != 0:
        logg('loop sendStuffCtl = ' + sendStuffCtl.__str__())
        if (sendStuffCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (sendStuffCtl == 1):
            logg('call sendStuff_1')
            sendStuff_1()
            logg('after call sendStuff_1')
            # test and adjust for new spoke
            sendStuffCtl = chk(sendStuffCtl)

        else:
            #final
            logg('final sendStuff')    
            sendStuffCtl = 0 # break
        #endif
    #wend
#end sendStuff

def sendStuff2_1():
    global p
    logg('sendStuff2_1')
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
    logg('processing verb ( sendStuff ) ')
    if (r == p['OK']):
        logg('call sendStuff ')
        p['sy']['sendStuff'](p)
        logg('after sendStuff')
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
    logg('final sendStuff2_1')
#end sendStuff2_1

def sendStuff2_2():
    global p
    logg('sendStuff2_2')
    datPush(p['OK'])

    #final
    logg('final sendStuff2_2')
#end sendStuff2_2

def sendStuff2 (x):
    global p
    logg('begin sendStuff2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    sendStuff2Ctl = 1 # starting spoke
    while sendStuff2Ctl != 0:
        logg('loop sendStuff2Ctl = ' + sendStuff2Ctl.__str__())
        if (sendStuff2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (sendStuff2Ctl == 1):
            logg('call sendStuff2_1')
            sendStuff2_1()
            logg('after call sendStuff2_1')
            # test and adjust for new spoke
            sendStuff2Ctl = chk(sendStuff2Ctl)

        elif (sendStuff2Ctl == 2):
            logg('call sendStuff2_2')
            sendStuff2_2()
            logg('after call sendStuff2_2')
            # test and adjust for new spoke
            sendStuff2Ctl = chk(sendStuff2Ctl)

        else:
            #final
            logg('final sendStuff2')    
            sendStuff2Ctl = 0 # break
        #endif
    #wend
#end sendStuff2

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

def MLNumber(p):
    logg ('<<<<LNumber>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<LNumber>>'] = j
#endif MLNumber

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

def EQscript(p):
    logg ('==script')
    needle = 'script'
    needle = needle.upper()
    return(eqeq(needle))
#end EQscript

def EQattribute(p):
    logg ('==attribute')
    needle = 'attribute'
    needle = needle.upper()
    return(eqeq(needle))
#end EQattribute

def MAttributeElementname(p):
    logg ('<<<<AttributeElementname>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<AttributeElementname>>'] = j
#endif MAttributeElementname

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

def EQsendList(p):
    logg ('==sendList')
    needle = 'sendList'
    needle = needle.upper()
    return(eqeq(needle))
#end EQsendList

def MsendListName(p):
    logg ('<<<<sendListName>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<sendListName>>'] = j
#endif MsendListName

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

def EQ_C_(p):
    logg ('==,')
    needle = ','
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_C_

def EQfn(p):
    logg ('==fn')
    needle = 'fn'
    needle = needle.upper()
    return(eqeq(needle))
#end EQfn

def MfnName(p):
    logg ('<<<<fnName>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<fnName>>'] = j
#endif MfnName

def EQ_OP_(p):
    logg ('==(')
    needle = '('
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_OP_

def METype(p):
    logg ('<<<<EType>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<EType>>'] = j
#endif METype

def EQ_CO_(p):
    logg ('==:')
    needle = ':'
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_CO_

def MEName(p):
    logg ('<<<<EName>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<EName>>'] = j
#endif MEName

def EQ_CP_(p):
    logg ('==)')
    needle = ')'
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_CP_

def Mliteral(p):
    logg ('<<<<literal>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<literal>>'] = j
#endif Mliteral

def EQ_C_(p):
    logg ('==,')
    needle = ','
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_C_

def MAttName(p):
    logg ('<<<<AttName>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<AttName>>'] = j
#endif MAttName

def EQ_EQ_(p):
    logg ('===')
    needle = '='
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_EQ_

def MATTValue(p):
    logg ('<<<<ATTValue>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<ATTValue>>'] = j
#endif MATTValue

def EQ_C_(p):
    logg ('==,')
    needle = ','
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_C_

def EQbegin(p):
    logg ('==begin')
    needle = 'begin'
    needle = needle.upper()
    return(eqeq(needle))
#end EQbegin

def Mname(p):
    logg ('<<<<name>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<name>>'] = j
#endif Mname

def Mname(p):
    logg ('<<<<name>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<name>>'] = j
#endif Mname

def EQend(p):
    logg ('==end')
    needle = 'end'
    needle = needle.upper()
    return(eqeq(needle))
#end EQend

def EQinclude(p):
    logg ('==include')
    needle = 'include'
    needle = needle.upper()
    return(eqeq(needle))
#end EQinclude

def MJSFilename(p):
    logg ('<<<<JSFilename>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<JSFilename>>'] = j
#endif MJSFilename

def EQ_C_(p):
    logg ('==,')
    needle = ','
    needle = needle.upper()
    return(eqeq(needle))
#end EQ_C_

def EQuse(p):
    logg ('==use')
    needle = 'use'
    needle = needle.upper()
    return(eqeq(needle))
#end EQuse

def MJSLibName(p):
    logg ('<<<<JSLibName>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<JSLibName>>'] = j
#endif MJSLibName

def MsendName(p):
    logg ('<<<<sendName>>>>')
    j = p['sy']['fio'].fpwd()
    p['v']['<<sendName>>'] = j
#endif MsendName

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

    # paragraph Smain
    p['sy']['Smain'] = Smain
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

    # paragraph screenStuffs
    p['sy']['screenStuffs'] = screenStuffs
    #

    # paragraph screenStuff
    p['sy']['screenStuff'] = screenStuff
    #

    # paragraph ==line
    p['sy']['==line'] = EQline
    #

    # paragraph <<LNumber>>
    p['sy']['<<LNumber>>'] = MLNumber
    #

    # paragraph ==(
    p['sy']['==('] = EQ_OP_
    #

    # paragraph ==)
    p['sy']['==)'] = EQ_CP_
    #

    # paragraph ==script
    p['sy']['==script'] = EQscript
    #

    # paragraph ==attribute
    p['sy']['==attribute'] = EQattribute
    #

    # paragraph <<AttributeElementname>>
    p['sy']['<<AttributeElementname>>'] = MAttributeElementname
    #

    # paragraph ==(
    p['sy']['==('] = EQ_OP_
    #

    # paragraph ==)
    p['sy']['==)'] = EQ_CP_
    #

    # paragraph ==sendList
    p['sy']['==sendList'] = EQsendList
    #

    # paragraph <<sendListName>>
    p['sy']['<<sendListName>>'] = MsendListName
    #

    # paragraph ==(
    p['sy']['==('] = EQ_OP_
    #

    # paragraph ==)
    p['sy']['==)'] = EQ_CP_
    #

    # paragraph screenStuff2
    p['sy']['screenStuff2'] = screenStuff2
    #

    # paragraph ==,
    p['sy']['==,'] = EQ_C_
    #

    # paragraph lineStuffs
    p['sy']['lineStuffs'] = lineStuffs
    #

    # paragraph lineStuff
    p['sy']['lineStuff'] = lineStuff
    #

    # paragraph ==fn
    p['sy']['==fn'] = EQfn
    #

    # paragraph <<fnName>>
    p['sy']['<<fnName>>'] = MfnName
    #

    # paragraph ==(
    p['sy']['==('] = EQ_OP_
    #

    # paragraph <<EType>>
    p['sy']['<<EType>>'] = METype
    #

    # paragraph ==:
    p['sy']['==:'] = EQ_CO_
    #

    # paragraph <<EName>>
    p['sy']['<<EName>>'] = MEName
    #

    # paragraph ==)
    p['sy']['==)'] = EQ_CP_
    #

    # paragraph <<literal>>
    p['sy']['<<literal>>'] = Mliteral
    #

    # paragraph lineStuff2
    p['sy']['lineStuff2'] = lineStuff2
    #

    # paragraph ==,
    p['sy']['==,'] = EQ_C_
    #

    # paragraph AStuffs
    p['sy']['AStuffs'] = AStuffs
    #

    # paragraph AStuff
    p['sy']['AStuff'] = AStuff
    #

    # paragraph <<AttName>>
    p['sy']['<<AttName>>'] = MAttName
    #

    # paragraph ===
    p['sy']['==='] = EQ_EQ_
    #

    # paragraph <<ATTValue>>
    p['sy']['<<ATTValue>>'] = MATTValue
    #

    # paragraph AStuff2
    p['sy']['AStuff2'] = AStuff2
    #

    # paragraph ==,
    p['sy']['==,'] = EQ_C_
    #

    # paragraph scriptStuff
    p['sy']['scriptStuff'] = scriptStuff
    #

    # paragraph ==begin
    p['sy']['==begin'] = EQbegin
    #

    # paragraph <<name>>
    p['sy']['<<name>>'] = Mname
    #

    # paragraph <<name>>
    p['sy']['<<name>>'] = Mname
    #

    # paragraph ==end
    p['sy']['==end'] = EQend
    #

    # paragraph ==include
    p['sy']['==include'] = EQinclude
    #

    # paragraph <<JSFilename>>
    p['sy']['<<JSFilename>>'] = MJSFilename
    #

    # paragraph ==,
    p['sy']['==,'] = EQ_C_
    #

    # paragraph ==use
    p['sy']['==use'] = EQuse
    #

    # paragraph <<JSLibName>>
    p['sy']['<<JSLibName>>'] = MJSLibName
    #

    # paragraph sendStuffs
    p['sy']['sendStuffs'] = sendStuffs
    #

    # paragraph sendStuff
    p['sy']['sendStuff'] = sendStuff
    #

    # paragraph <<sendName>>
    p['sy']['<<sendName>>'] = MsendName
    #

    # paragraph sendStuff2
    p['sy']['sendStuff2'] = sendStuff2
    #

    # paragraph ==,
    p['sy']['==,'] = EQ_C_
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

