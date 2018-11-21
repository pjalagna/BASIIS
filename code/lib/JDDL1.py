
#file JDDL1.py
#generated for JADDDL.txt 

 
def DDLStart_1():
    global p
    logg('DDLStart_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQT ) ')
    if (r == p['OK']):
        logg('call EQT ')
        p['sy']['EQT'](p)
        logg('after EQT')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( EQ_OP__OP_ ) ')
    if (r == p['OK']):
        logg('call EQ_OP__OP_ ')
        p['sy']['EQ_OP__OP_'](p)
        logg('after EQ_OP__OP_')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( keys ) ')
    if (r == p['OK']):
        logg('call keys ')
        p['sy']['keys'](p)
        logg('after keys')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( EQ_CP_ ) ')
    if (r == p['OK']):
        logg('call EQ_CP_ ')
        p['sy']['EQ_CP_'](p)
        logg('after EQ_CP_')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( tags ) ')
    if (r == p['OK']):
        logg('call tags ')
        p['sy']['tags'](p)
        logg('after tags')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( EQ_CP_ ) ')
    if (r == p['OK']):
        logg('call EQ_CP_ ')
        p['sy']['EQ_CP_'](p)
        logg('after EQ_CP_')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( actDDL ) ')
    if (r == p['OK']):
        logg('call actDDL ')
        p['sy']['actDDL'](p)
        logg('after actDDL')
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
    logg('final DDLStart_1')
#end DDLStart_1

def DDLStart_2():
    global p
    logg('DDLStart_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQR ) ')
    if (r == p['OK']):
        logg('call EQR ')
        p['sy']['EQR'](p)
        logg('after EQR')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( reltypes ) ')
    if (r == p['OK']):
        logg('call reltypes ')
        p['sy']['reltypes'](p)
        logg('after reltypes')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( EQ_SC_ ) ')
    if (r == p['OK']):
        logg('call EQ_SC_ ')
        p['sy']['EQ_SC_'](p)
        logg('after EQ_SC_')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( actRel ) ')
    if (r == p['OK']):
        logg('call actRel ')
        p['sy']['actRel'](p)
        logg('after actRel')
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
    logg('final DDLStart_2')
#end DDLStart_2

def DDLStart_2():
    global p
    logg('DDLStart_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQendend ) ')
    if (r == p['OK']):
        logg('call EQendend ')
        p['sy']['EQendend'](p)
        logg('after EQendend')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( actFinal ) ')
    if (r == p['OK']):
        logg('call actFinal ')
        p['sy']['actFinal'](p)
        logg('after actFinal')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final DDLStart_2')
#end DDLStart_2

def DDLStart (x):
    global p
    logg('begin DDLStart')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    DDLStartCtl = 1 # starting spoke
    while DDLStartCtl != 0:
        logg('loop DDLStartCtl = ' + DDLStartCtl.__str__())
        if (DDLStartCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (DDLStartCtl == 1):
            logg('call DDLStart_1')
            DDLStart_1()
            logg('after call DDLStart_1')
            # test and adjust for new spoke
            DDLStartCtl = chk(DDLStartCtl)

        elif (DDLStartCtl == 2):
            logg('call DDLStart_2')
            DDLStart_2()
            logg('after call DDLStart_2')
            # test and adjust for new spoke
            DDLStartCtl = chk(DDLStartCtl)

        elif (DDLStartCtl == 3):
            logg('call DDLStart_2')
            DDLStart_2()
            logg('after call DDLStart_2')
            # test and adjust for new spoke
            DDLStartCtl = chk(DDLStartCtl)

        else:
            #final
            logg('final DDLStart')    
            DDLStartCtl = 0 # break
        #endif
    #wend
#end DDLStart

def keys_1():
    global p
    logg('keys_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( key ) ')
    if (r == p['OK']):
        logg('call key ')
        p['sy']['key'](p)
        logg('after key')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( opkey ) ')
    if (r == p['OK']):
        logg('call opkey ')
        p['sy']['opkey'](p)
        logg('after opkey')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final keys_1')
#end keys_1

def keys (x):
    global p
    logg('begin keys')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    keysCtl = 1 # starting spoke
    while keysCtl != 0:
        logg('loop keysCtl = ' + keysCtl.__str__())
        if (keysCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (keysCtl == 1):
            logg('call keys_1')
            keys_1()
            logg('after call keys_1')
            # test and adjust for new spoke
            keysCtl = chk(keysCtl)

        else:
            #final
            logg('final keys')    
            keysCtl = 0 # break
        #endif
    #wend
#end keys

def key_1():
    global p
    logg('key_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( actKey ) ')
    if (r == p['OK']):
        logg('call actKey ')
        p['sy']['actKey'](p)
        logg('after actKey')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final key_1')
#end key_1

def key (x):
    global p
    logg('begin key')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    keyCtl = 1 # starting spoke
    while keyCtl != 0:
        logg('loop keyCtl = ' + keyCtl.__str__())
        if (keyCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (keyCtl == 1):
            logg('call key_1')
            key_1()
            logg('after call key_1')
            # test and adjust for new spoke
            keyCtl = chk(keyCtl)

        else:
            #final
            logg('final key')    
            keyCtl = 0 # break
        #endif
    #wend
#end key

def opkey_1():
    global p
    logg('opkey_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQ_C_ ) ')
    if (r == p['OK']):
        logg('call EQ_C_ ')
        p['sy']['EQ_C_'](p)
        logg('after EQ_C_')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( key ) ')
    if (r == p['OK']):
        logg('call key ')
        p['sy']['key'](p)
        logg('after key')
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
    logg('final opkey_1')
#end opkey_1

def opkey_2():
    global p
    logg('opkey_2')
    datPush(p['OK'])

    #final
    logg('final opkey_2')
#end opkey_2

def opkey (x):
    global p
    logg('begin opkey')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    opkeyCtl = 1 # starting spoke
    while opkeyCtl != 0:
        logg('loop opkeyCtl = ' + opkeyCtl.__str__())
        if (opkeyCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (opkeyCtl == 1):
            logg('call opkey_1')
            opkey_1()
            logg('after call opkey_1')
            # test and adjust for new spoke
            opkeyCtl = chk(opkeyCtl)

        elif (opkeyCtl == 2):
            logg('call opkey_2')
            opkey_2()
            logg('after call opkey_2')
            # test and adjust for new spoke
            opkeyCtl = chk(opkeyCtl)

        else:
            #final
            logg('final opkey')    
            opkeyCtl = 0 # break
        #endif
    #wend
#end opkey

def tags_1():
    global p
    logg('tags_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQ_CP_ ) ')
    if (r == p['OK']):
        logg('call EQ_CP_ ')
        p['sy']['EQ_CP_'](p)
        logg('after EQ_CP_')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( putback ) ')
    if (r == p['OK']):
        logg('call putback ')
        p['sy']['putback'](p)
        logg('after putback')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final tags_1')
#end tags_1

def tags_2():
    global p
    logg('tags_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( tag ) ')
    if (r == p['OK']):
        logg('call tag ')
        p['sy']['tag'](p)
        logg('after tag')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( opTag ) ')
    if (r == p['OK']):
        logg('call opTag ')
        p['sy']['opTag'](p)
        logg('after opTag')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final tags_2')
#end tags_2

def tags (x):
    global p
    logg('begin tags')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    tagsCtl = 1 # starting spoke
    while tagsCtl != 0:
        logg('loop tagsCtl = ' + tagsCtl.__str__())
        if (tagsCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (tagsCtl == 1):
            logg('call tags_1')
            tags_1()
            logg('after call tags_1')
            # test and adjust for new spoke
            tagsCtl = chk(tagsCtl)

        elif (tagsCtl == 2):
            logg('call tags_2')
            tags_2()
            logg('after call tags_2')
            # test and adjust for new spoke
            tagsCtl = chk(tagsCtl)

        else:
            #final
            logg('final tags')    
            tagsCtl = 0 # break
        #endif
    #wend
#end tags

def tag_1():
    global p
    logg('tag_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( actTag ) ')
    if (r == p['OK']):
        logg('call actTag ')
        p['sy']['actTag'](p)
        logg('after actTag')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final tag_1')
#end tag_1

def tag (x):
    global p
    logg('begin tag')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    tagCtl = 1 # starting spoke
    while tagCtl != 0:
        logg('loop tagCtl = ' + tagCtl.__str__())
        if (tagCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (tagCtl == 1):
            logg('call tag_1')
            tag_1()
            logg('after call tag_1')
            # test and adjust for new spoke
            tagCtl = chk(tagCtl)

        else:
            #final
            logg('final tag')    
            tagCtl = 0 # break
        #endif
    #wend
#end tag

def opTag_1():
    global p
    logg('opTag_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQ_C_ ) ')
    if (r == p['OK']):
        logg('call EQ_C_ ')
        p['sy']['EQ_C_'](p)
        logg('after EQ_C_')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( tag ) ')
    if (r == p['OK']):
        logg('call tag ')
        p['sy']['tag'](p)
        logg('after tag')
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
    logg('final opTag_1')
#end opTag_1

def opTag_2():
    global p
    logg('opTag_2')
    datPush(p['OK'])

    #final
    logg('final opTag_2')
#end opTag_2

def opTag (x):
    global p
    logg('begin opTag')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    opTagCtl = 1 # starting spoke
    while opTagCtl != 0:
        logg('loop opTagCtl = ' + opTagCtl.__str__())
        if (opTagCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (opTagCtl == 1):
            logg('call opTag_1')
            opTag_1()
            logg('after call opTag_1')
            # test and adjust for new spoke
            opTagCtl = chk(opTagCtl)

        elif (opTagCtl == 2):
            logg('call opTag_2')
            opTag_2()
            logg('after call opTag_2')
            # test and adjust for new spoke
            opTagCtl = chk(opTagCtl)

        else:
            #final
            logg('final opTag')    
            opTagCtl = 0 # break
        #endif
    #wend
#end opTag

def relTypes_1():
    global p
    logg('relTypes_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQ--_P__LT_ ) ')
    if (r == p['OK']):
        logg('call EQ--_P__LT_ ')
        p['sy']['EQ--_P__LT_'](p)
        logg('after EQ--_P__LT_')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- FOrder -- ') 
    if (r == p['OK']):
        logg('push text FOrder ')
        datPush("FOrder")
        logg('after FOrder ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- relType -- ') 
    if (r == p['OK']):
        logg('push text relType ')
        datPush("relType")
        logg('after relType ')
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
    logg('final relTypes_1')
#end relTypes_1

def relTypes_2():
    global p
    logg('relTypes_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQ_GT__P_-- ) ')
    if (r == p['OK']):
        logg('call EQ_GT__P_-- ')
        p['sy']['EQ_GT__P_--'](p)
        logg('after EQ_GT__P_--')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- BOrder -- ') 
    if (r == p['OK']):
        logg('push text BOrder ')
        datPush("BOrder")
        logg('after BOrder ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- relType -- ') 
    if (r == p['OK']):
        logg('push text relType ')
        datPush("relType")
        logg('after relType ')
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
    logg('final relTypes_2')
#end relTypes_2

def relTypes_3():
    global p
    logg('relTypes_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQ--_LT_ ) ')
    if (r == p['OK']):
        logg('call EQ--_LT_ ')
        p['sy']['EQ--_LT_'](p)
        logg('after EQ--_LT_')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- F1M -- ') 
    if (r == p['OK']):
        logg('push text F1M ')
        datPush("F1M")
        logg('after F1M ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- relType -- ') 
    if (r == p['OK']):
        logg('push text relType ')
        datPush("relType")
        logg('after relType ')
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
    logg('final relTypes_3')
#end relTypes_3

def relTypes_4():
    global p
    logg('relTypes_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQ--0_LT_ ) ')
    if (r == p['OK']):
        logg('call EQ--0_LT_ ')
        p['sy']['EQ--0_LT_'](p)
        logg('after EQ--0_LT_')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- F0M -- ') 
    if (r == p['OK']):
        logg('push text F0M ')
        datPush("F0M")
        logg('after F0M ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- relType -- ') 
    if (r == p['OK']):
        logg('push text relType ')
        datPush("relType")
        logg('after relType ')
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
    logg('final relTypes_4')
#end relTypes_4

def relTypes_5():
    global p
    logg('relTypes_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( EQ-- ) ')
    if (r == p['OK']):
        logg('call EQ-- ')
        p['sy']['EQ--'](p)
        logg('after EQ--')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- F11 -- ') 
    if (r == p['OK']):
        logg('push text F11 ')
        datPush("F11")
        logg('after F11 ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- relType -- ') 
    if (r == p['OK']):
        logg('push text relType ')
        datPush("relType")
        logg('after relType ')
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
    logg('final relTypes_5')
#end relTypes_5

def relTypes (x):
    global p
    logg('begin relTypes')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    relTypesCtl = 1 # starting spoke
    while relTypesCtl != 0:
        logg('loop relTypesCtl = ' + relTypesCtl.__str__())
        if (relTypesCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (relTypesCtl == 1):
            logg('call relTypes_1')
            relTypes_1()
            logg('after call relTypes_1')
            # test and adjust for new spoke
            relTypesCtl = chk(relTypesCtl)

        elif (relTypesCtl == 2):
            logg('call relTypes_2')
            relTypes_2()
            logg('after call relTypes_2')
            # test and adjust for new spoke
            relTypesCtl = chk(relTypesCtl)

        elif (relTypesCtl == 3):
            logg('call relTypes_3')
            relTypes_3()
            logg('after call relTypes_3')
            # test and adjust for new spoke
            relTypesCtl = chk(relTypesCtl)

        elif (relTypesCtl == 4):
            logg('call relTypes_4')
            relTypes_4()
            logg('after call relTypes_4')
            # test and adjust for new spoke
            relTypesCtl = chk(relTypesCtl)

        elif (relTypesCtl == 5):
            logg('call relTypes_5')
            relTypes_5()
            logg('after call relTypes_5')
            # test and adjust for new spoke
            relTypesCtl = chk(relTypesCtl)

        else:
            #final
            logg('final relTypes')    
            relTypesCtl = 0 # break
        #endif
    #wend
#end relTypes

# stream routines 

def EQT():
    logg ('EQT')
    needle = 'T'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def MTName(p):
    logg ('<<TName>>')
    j = p['sy']['fio'].fpwd()
    p['v'][TName'] = j
#endif MTName

def EQ((():
    logg ('EQ_OP__OP_')
    needle = '(('
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def EQ)():
    logg ('EQ_CP_')
    needle = ')'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def EQ)():
    logg ('EQ_CP_')
    needle = ')'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def EQR():
    logg ('EQR')
    needle = 'R'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def MRel1Name(p):
    logg ('<<Rel1Name>>')
    j = p['sy']['fio'].fpwd()
    p['v'][Rel1Name'] = j
#endif MRel1Name

def MRel2Name(p):
    logg ('<<Rel2Name>>')
    j = p['sy']['fio'].fpwd()
    p['v'][Rel2Name'] = j
#endif MRel2Name

def EQ;():
    logg ('EQ_SC_')
    needle = ';'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def EQendend():
    logg ('EQendend')
    needle = 'endend'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def MKeyName(p):
    logg ('<<KeyName>>')
    j = p['sy']['fio'].fpwd()
    p['v'][KeyName'] = j
#endif MKeyName

def EQ,():
    logg ('EQ_C_')
    needle = ','
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def EQ)():
    logg ('EQ_CP_')
    needle = ')'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def MTagName(p):
    logg ('<<TagName>>')
    j = p['sy']['fio'].fpwd()
    p['v'][TagName'] = j
#endif MTagName

def EQ,():
    logg ('EQ_C_')
    needle = ','
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def EQ--#<():
    logg ('EQ--_P__LT_')
    needle = '--#<'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def EQ>#--():
    logg ('EQ_GT__P_--')
    needle = '>#--'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def EQ--<():
    logg ('EQ--_LT_')
    needle = '--<'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def EQ--0<():
    logg ('EQ--0_LT_')
    needle = '--0<'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

def EQ--():
    logg ('EQ--')
    needle = '--'
    needle = needle.upper()
    return(eqeq(needle))
#end EQmark

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

    # paragraph DDLStart
    p['sy']['DDLStart'] = DDLStart
    #

    # paragraph keys
    p['sy']['keys'] = keys
    #

    # paragraph key
    p['sy']['key'] = key
    #

    # paragraph opkey
    p['sy']['opkey'] = opkey
    #

    # paragraph tags
    p['sy']['tags'] = tags
    #

    # paragraph tag
    p['sy']['tag'] = tag
    #

    # paragraph opTag
    p['sy']['opTag'] = opTag
    #

    # paragraph relTypes
    p['sy']['relTypes'] = relTypes
    #

    p['sy']['start'] = p['sy'][startpoint] 
#end main
def start(trace='off'):
    p['v']['trace'] = trace # save trace setting
    p['sy']['start'](trace) # process begins at start
#end start

# helper rtns 
def eqeq(needle)
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
    elif (okn == p['...']):
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

