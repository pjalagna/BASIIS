
#file ddlgen.py
#generated for ddlgen.txt 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def here1_1():
    global p
    logg('here1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- NOTE infile set from fioiP  -- ') 
    if (r == p['OK']):
        logg('push text NOTE infile set from fioiP  ')
        datPush("NOTE infile set from fioiP ")
        logg('after NOTE infile set from fioiP  ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- ./out/ -- ') 
    if (r == p['OK']):
        logg('push text ./out/ ')
        datPush("./out/")
        logg('after ./out/ ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- dirLoc -- ') 
    if (r == p['OK']):
        logg('push text dirLoc ')
        datPush("dirLoc")
        logg('after dirLoc ')
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
    logg('processing text -- dirLoc -- ') 
    if (r == p['OK']):
        logg('push text dirLoc ')
        datPush("dirLoc")
        logg('after dirLoc ')
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
    logg('processing text -- infile -- ') 
    if (r == p['OK']):
        logg('push text infile ')
        datPush("infile")
        logg('after infile ')
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
    logg('processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- .out.txt -- ') 
    if (r == p['OK']):
        logg('push text .out.txt ')
        datPush(".out.txt")
        logg('after .out.txt ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- outfloc -- ') 
    if (r == p['OK']):
        logg('push text outfloc ')
        datPush("outfloc")
        logg('after outfloc ')
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
    logg('processing text -- outfloc -- ') 
    if (r == p['OK']):
        logg('push text outfloc ')
        datPush("outfloc")
        logg('after outfloc ')
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
    logg('processing text -- outfloc -- ') 
    if (r == p['OK']):
        logg('push text outfloc ')
        datPush("outfloc")
        logg('after outfloc ')
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
    logg('processing verb ( fclear ) ')
    if (r == p['OK']):
        logg('call fclear ')
        p['sy']['fclear'](p)
        logg('after fclear')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text --   -- ') 
    if (r == p['OK']):
        logg('push text   ')
        datPush(" ")
        logg('after   ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- flList -- ') 
    if (r == p['OK']):
        logg('push text flList ')
        datPush("flList")
        logg('after flList ')
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
    logg('processing text --   -- ') 
    if (r == p['OK']):
        logg('push text   ')
        datPush(" ")
        logg('after   ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('processing text --   -- ') 
    if (r == p['OK']):
        logg('push text   ')
        datPush(" ")
        logg('after   ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- pkList -- ') 
    if (r == p['OK']):
        logg('push text pkList ')
        datPush("pkList")
        logg('after pkList ')
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
    logg('processing text --   -- ') 
    if (r == p['OK']):
        logg('push text   ')
        datPush(" ")
        logg('after   ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- ftsw1 -- ') 
    if (r == p['OK']):
        logg('push text ftsw1 ')
        datPush("ftsw1")
        logg('after ftsw1 ')
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
    logg('processing text --   -- ') 
    if (r == p['OK']):
        logg('push text   ')
        datPush(" ")
        logg('after   ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- ftsw2 -- ') 
    if (r == p['OK']):
        logg('push text ftsw2 ')
        datPush("ftsw2")
        logg('after ftsw2 ')
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
    logg('processing text -- \n CREATE TABLE IF NOT EXISTS %sna  (  -- ') 
    if (r == p['OK']):
        logg('push text \n CREATE TABLE IF NOT EXISTS %sna  (  ')
        datPush("\n CREATE TABLE IF NOT EXISTS %sna  ( ")
        logg('after \n CREATE TABLE IF NOT EXISTS %sna  (  ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s1 -- ') 
    if (r == p['OK']):
        logg('push text s1 ')
        datPush("s1")
        logg('after s1 ')
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
    logg('processing text --  %cn ,  -- ') 
    if (r == p['OK']):
        logg('push text  %cn ,  ')
        datPush(" %cn , ")
        logg('after  %cn ,  ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s2 -- ') 
    if (r == p['OK']):
        logg('push text s2 ')
        datPush("s2")
        logg('after s2 ')
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
    logg('processing text -- \n   %cn REFERENCES %fkn ( %fkc ) ,  -- ') 
    if (r == p['OK']):
        logg('push text \n   %cn REFERENCES %fkn ( %fkc ) ,  ')
        datPush("\n   %cn REFERENCES %fkn ( %fkc ) , ")
        logg('after \n   %cn REFERENCES %fkn ( %fkc ) ,  ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s2a -- ') 
    if (r == p['OK']):
        logg('push text s2a ')
        datPush("s2a")
        logg('after s2a ')
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
    logg('processing text --  primary key ( -- ') 
    if (r == p['OK']):
        logg('push text  primary key ( ')
        datPush(" primary key (")
        logg('after  primary key ( ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s3a -- ') 
    if (r == p['OK']):
        logg('push text s3a ')
        datPush("s3a")
        logg('after s3a ')
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
    logg('processing text --  ) \n );  -- ') 
    if (r == p['OK']):
        logg('push text  ) \n );  ')
        datPush(" ) \n ); ")
        logg('after  ) \n );  ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s4 -- ') 
    if (r == p['OK']):
        logg('push text s4 ')
        datPush("s4")
        logg('after s4 ')
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
    logg('processing verb ( ddlstart ) ')
    if (r == p['OK']):
        logg('call ddlstart ')
        p['sy']['ddlstart'](p)
        logg('after ddlstart')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ddlend ) ')
    if (r == p['OK']):
        logg('call ddlend ')
        p['sy']['ddlend'](p)
        logg('after ddlend')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final here1_1')
#end here1_1

def here1 (x):
    global p
    logg('begin here1')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    here1Ctl = 1 # starting spoke
    while here1Ctl != 0:
        logg('loop here1Ctl = ' + here1Ctl.__str__())
        if (here1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (here1Ctl == 1):
            logg('call here1_1')
            here1_1()
            logg('after call here1_1')
            # test and adjust for new spoke
            here1Ctl = chk(here1Ctl)

        else:
            #final
            logg('final here1')    
            here1Ctl = 0 # break
        #endif
    #wend
#end here1

def ddlstart_1():
    global p
    logg('ddlstart_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==S ) ')
    if (r == p['OK']):
        logg('call ==S ')
        p['sy']['==S'](p)
        logg('after ==S')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( <<sna>> ) ')
    if (r == p['OK']):
        logg('call <<sna>> ')
        p['sy']['<<sna>>'](p)
        logg('after <<sna>>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( SAct ) ')
    if (r == p['OK']):
        logg('call SAct ')
        p['sy']['SAct'](p)
        logg('after SAct')
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
    logg('processing verb ( ds2 ) ')
    if (r == p['OK']):
        logg('call ds2 ')
        p['sy']['ds2'](p)
        logg('after ds2')
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
    logg('final ddlstart_1')
#end ddlstart_1

def ddlstart (x):
    global p
    logg('begin ddlstart')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    ddlstartCtl = 1 # starting spoke
    while ddlstartCtl != 0:
        logg('loop ddlstartCtl = ' + ddlstartCtl.__str__())
        if (ddlstartCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (ddlstartCtl == 1):
            logg('call ddlstart_1')
            ddlstart_1()
            logg('after call ddlstart_1')
            # test and adjust for new spoke
            ddlstartCtl = chk(ddlstartCtl)

        else:
            #final
            logg('final ddlstart')    
            ddlstartCtl = 0 # break
        #endif
    #wend
#end ddlstart

def ds2_1():
    global p
    logg('ds2_1')
    datPush(p['OK'])

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
    logg('processing verb ( FAct ) ')
    if (r == p['OK']):
        logg('call FAct ')
        p['sy']['FAct'](p)
        logg('after FAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final ds2_1')
#end ds2_1

def ds2_2():
    global p
    logg('ds2_2')
    datPush(p['OK'])

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
    logg('processing verb ( FAct ) ')
    if (r == p['OK']):
        logg('call FAct ')
        p['sy']['FAct'](p)
        logg('after FAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final ds2_2')
#end ds2_2

def ds2 (x):
    global p
    logg('begin ds2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    ds2Ctl = 1 # starting spoke
    while ds2Ctl != 0:
        logg('loop ds2Ctl = ' + ds2Ctl.__str__())
        if (ds2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (ds2Ctl == 1):
            logg('call ds2_1')
            ds2_1()
            logg('after call ds2_1')
            # test and adjust for new spoke
            ds2Ctl = chk(ds2Ctl)

        elif (ds2Ctl == 2):
            logg('call ds2_2')
            ds2_2()
            logg('after call ds2_2')
            # test and adjust for new spoke
            ds2Ctl = chk(ds2Ctl)

        else:
            #final
            logg('final ds2')    
            ds2Ctl = 0 # break
        #endif
    #wend
#end ds2

def keys_1():
    global p
    logg('keys_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( keyin ) ')
    if (r == p['OK']):
        logg('call keyin ')
        p['sy']['keyin'](p)
        logg('after keyin')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( key2 ) ')
    if (r == p['OK']):
        logg('call key2 ')
        p['sy']['key2'](p)
        logg('after key2')
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

def keyin_1():
    global p
    logg('keyin_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( <<kn>> ) ')
    if (r == p['OK']):
        logg('call <<kn>> ')
        p['sy']['<<kn>>'](p)
        logg('after <<kn>>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( keyin2 ) ')
    if (r == p['OK']):
        logg('call keyin2 ')
        p['sy']['keyin2'](p)
        logg('after keyin2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final keyin_1')
#end keyin_1

def keyin (x):
    global p
    logg('begin keyin')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    keyinCtl = 1 # starting spoke
    while keyinCtl != 0:
        logg('loop keyinCtl = ' + keyinCtl.__str__())
        if (keyinCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (keyinCtl == 1):
            logg('call keyin_1')
            keyin_1()
            logg('after call keyin_1')
            # test and adjust for new spoke
            keyinCtl = chk(keyinCtl)

        else:
            #final
            logg('final keyin')    
            keyinCtl = 0 # break
        #endif
    #wend
#end keyin

def keyin2_1():
    global p
    logg('keyin2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==@@ ) ')
    if (r == p['OK']):
        logg('call ==@@ ')
        p['sy']['==@@'](p)
        logg('after ==@@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( <<fkTable>> ) ')
    if (r == p['OK']):
        logg('call <<fkTable>> ')
        p['sy']['<<fkTable>>'](p)
        logg('after <<fkTable>>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( <<fkCol>> ) ')
    if (r == p['OK']):
        logg('call <<fkCol>> ')
        p['sy']['<<fkCol>>'](p)
        logg('after <<fkCol>>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( FKKAct ) ')
    if (r == p['OK']):
        logg('call FKKAct ')
        p['sy']['FKKAct'](p)
        logg('after FKKAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final keyin2_1')
#end keyin2_1

def keyin2_2():
    global p
    logg('keyin2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( KAct ) ')
    if (r == p['OK']):
        logg('call KAct ')
        p['sy']['KAct'](p)
        logg('after KAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final keyin2_2')
#end keyin2_2

def keyin2 (x):
    global p
    logg('begin keyin2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    keyin2Ctl = 1 # starting spoke
    while keyin2Ctl != 0:
        logg('loop keyin2Ctl = ' + keyin2Ctl.__str__())
        if (keyin2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (keyin2Ctl == 1):
            logg('call keyin2_1')
            keyin2_1()
            logg('after call keyin2_1')
            # test and adjust for new spoke
            keyin2Ctl = chk(keyin2Ctl)

        elif (keyin2Ctl == 2):
            logg('call keyin2_2')
            keyin2_2()
            logg('after call keyin2_2')
            # test and adjust for new spoke
            keyin2Ctl = chk(keyin2Ctl)

        else:
            #final
            logg('final keyin2')    
            keyin2Ctl = 0 # break
        #endif
    #wend
#end keyin2

def key2_1():
    global p
    logg('key2_1')
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
    logg('processing verb ( keyin ) ')
    if (r == p['OK']):
        logg('call keyin ')
        p['sy']['keyin'](p)
        logg('after keyin')
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
    logg('final key2_1')
#end key2_1

def key2_2():
    global p
    logg('key2_2')
    datPush(p['OK'])

    #final
    logg('final key2_2')
#end key2_2

def key2 (x):
    global p
    logg('begin key2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    key2Ctl = 1 # starting spoke
    while key2Ctl != 0:
        logg('loop key2Ctl = ' + key2Ctl.__str__())
        if (key2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (key2Ctl == 1):
            logg('call key2_1')
            key2_1()
            logg('after call key2_1')
            # test and adjust for new spoke
            key2Ctl = chk(key2Ctl)

        elif (key2Ctl == 2):
            logg('call key2_2')
            key2_2()
            logg('after call key2_2')
            # test and adjust for new spoke
            key2Ctl = chk(key2Ctl)

        else:
            #final
            logg('final key2')    
            key2Ctl = 0 # break
        #endif
    #wend
#end key2

def tags_1():
    global p
    logg('tags_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( tagin ) ')
    if (r == p['OK']):
        logg('call tagin ')
        p['sy']['tagin'](p)
        logg('after tagin')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( tag2 ) ')
    if (r == p['OK']):
        logg('call tag2 ')
        p['sy']['tag2'](p)
        logg('after tag2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final tags_1')
#end tags_1

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

        else:
            #final
            logg('final tags')    
            tagsCtl = 0 # break
        #endif
    #wend
#end tags

def tagin_1():
    global p
    logg('tagin_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( <<tn>> ) ')
    if (r == p['OK']):
        logg('call <<tn>> ')
        p['sy']['<<tn>>'](p)
        logg('after <<tn>>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( tagin2 ) ')
    if (r == p['OK']):
        logg('call tagin2 ')
        p['sy']['tagin2'](p)
        logg('after tagin2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final tagin_1')
#end tagin_1

def tagin (x):
    global p
    logg('begin tagin')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    taginCtl = 1 # starting spoke
    while taginCtl != 0:
        logg('loop taginCtl = ' + taginCtl.__str__())
        if (taginCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (taginCtl == 1):
            logg('call tagin_1')
            tagin_1()
            logg('after call tagin_1')
            # test and adjust for new spoke
            taginCtl = chk(taginCtl)

        else:
            #final
            logg('final tagin')    
            taginCtl = 0 # break
        #endif
    #wend
#end tagin

def tagin2_1():
    global p
    logg('tagin2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==@@ ) ')
    if (r == p['OK']):
        logg('call ==@@ ')
        p['sy']['==@@'](p)
        logg('after ==@@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( <<fkTable>> ) ')
    if (r == p['OK']):
        logg('call <<fkTable>> ')
        p['sy']['<<fkTable>>'](p)
        logg('after <<fkTable>>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( <<fkCol>> ) ')
    if (r == p['OK']):
        logg('call <<fkCol>> ')
        p['sy']['<<fkCol>>'](p)
        logg('after <<fkCol>>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( FKTAct ) ')
    if (r == p['OK']):
        logg('call FKTAct ')
        p['sy']['FKTAct'](p)
        logg('after FKTAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final tagin2_1')
#end tagin2_1

def tagin2_2():
    global p
    logg('tagin2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( TAct ) ')
    if (r == p['OK']):
        logg('call TAct ')
        p['sy']['TAct'](p)
        logg('after TAct')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final tagin2_2')
#end tagin2_2

def tagin2 (x):
    global p
    logg('begin tagin2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    tagin2Ctl = 1 # starting spoke
    while tagin2Ctl != 0:
        logg('loop tagin2Ctl = ' + tagin2Ctl.__str__())
        if (tagin2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (tagin2Ctl == 1):
            logg('call tagin2_1')
            tagin2_1()
            logg('after call tagin2_1')
            # test and adjust for new spoke
            tagin2Ctl = chk(tagin2Ctl)

        elif (tagin2Ctl == 2):
            logg('call tagin2_2')
            tagin2_2()
            logg('after call tagin2_2')
            # test and adjust for new spoke
            tagin2Ctl = chk(tagin2Ctl)

        else:
            #final
            logg('final tagin2')    
            tagin2Ctl = 0 # break
        #endif
    #wend
#end tagin2

def tag2_1():
    global p
    logg('tag2_1')
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
    logg('processing verb ( tagin ) ')
    if (r == p['OK']):
        logg('call tagin ')
        p['sy']['tagin'](p)
        logg('after tagin')
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
    logg('final tag2_1')
#end tag2_1

def tag2_2():
    global p
    logg('tag2_2')
    datPush(p['OK'])

    #final
    logg('final tag2_2')
#end tag2_2

def tag2 (x):
    global p
    logg('begin tag2')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    tag2Ctl = 1 # starting spoke
    while tag2Ctl != 0:
        logg('loop tag2Ctl = ' + tag2Ctl.__str__())
        if (tag2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (tag2Ctl == 1):
            logg('call tag2_1')
            tag2_1()
            logg('after call tag2_1')
            # test and adjust for new spoke
            tag2Ctl = chk(tag2Ctl)

        elif (tag2Ctl == 2):
            logg('call tag2_2')
            tag2_2()
            logg('after call tag2_2')
            # test and adjust for new spoke
            tag2Ctl = chk(tag2Ctl)

        else:
            #final
            logg('final tag2')    
            tag2Ctl = 0 # break
        #endif
    #wend
#end tag2

def SAct_1():
    global p
    logg('SAct_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('processing text -- <<sna>> -- ') 
    if (r == p['OK']):
        logg('push text <<sna>> ')
        datPush("<<sna>>")
        logg('after <<sna>> ')
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
    logg('processing text -- %sna -- ') 
    if (r == p['OK']):
        logg('push text %sna ')
        datPush("%sna")
        logg('after %sna ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s1 -- ') 
    if (r == p['OK']):
        logg('push text s1 ')
        datPush("s1")
        logg('after s1 ')
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
    logg('processing verb ( strReplace ) ')
    if (r == p['OK']):
        logg('call strReplace ')
        p['sy']['strReplace'](p)
        logg('after strReplace')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('final SAct_1')
#end SAct_1

def SAct (x):
    global p
    logg('begin SAct')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    SActCtl = 1 # starting spoke
    while SActCtl != 0:
        logg('loop SActCtl = ' + SActCtl.__str__())
        if (SActCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (SActCtl == 1):
            logg('call SAct_1')
            SAct_1()
            logg('after call SAct_1')
            # test and adjust for new spoke
            SActCtl = chk(SActCtl)

        else:
            #final
            logg('final SAct')    
            SActCtl = 0 # break
        #endif
    #wend
#end SAct

def KAct_1():
    global p
    logg('KAct_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- pkList -- ') 
    if (r == p['OK']):
        logg('push text pkList ')
        datPush("pkList")
        logg('after pkList ')
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
    logg('processing text -- <<kn>> -- ') 
    if (r == p['OK']):
        logg('push text <<kn>> ')
        datPush("<<kn>>")
        logg('after <<kn>> ')
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
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text --  ,  -- ') 
    if (r == p['OK']):
        logg('push text  ,  ')
        datPush(" , ")
        logg('after  ,  ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- pkList -- ') 
    if (r == p['OK']):
        logg('push text pkList ')
        datPush("pkList")
        logg('after pkList ')
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
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('processing verb ( crlf ) ')
    if (r == p['OK']):
        logg('call crlf ')
        p['sy']['crlf'](p)
        logg('after crlf')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- <<kn>> -- ') 
    if (r == p['OK']):
        logg('push text <<kn>> ')
        datPush("<<kn>>")
        logg('after <<kn>> ')
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
    logg('processing text -- %cn -- ') 
    if (r == p['OK']):
        logg('push text %cn ')
        datPush("%cn")
        logg('after %cn ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s2 -- ') 
    if (r == p['OK']):
        logg('push text s2 ')
        datPush("s2")
        logg('after s2 ')
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
    logg('processing verb ( strReplace ) ')
    if (r == p['OK']):
        logg('call strReplace ')
        p['sy']['strReplace'](p)
        logg('after strReplace')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('final KAct_1')
#end KAct_1

def KAct (x):
    global p
    logg('begin KAct')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    KActCtl = 1 # starting spoke
    while KActCtl != 0:
        logg('loop KActCtl = ' + KActCtl.__str__())
        if (KActCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (KActCtl == 1):
            logg('call KAct_1')
            KAct_1()
            logg('after call KAct_1')
            # test and adjust for new spoke
            KActCtl = chk(KActCtl)

        else:
            #final
            logg('final KAct')    
            KActCtl = 0 # break
        #endif
    #wend
#end KAct

def TAct_1():
    global p
    logg('TAct_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('processing verb ( crlf ) ')
    if (r == p['OK']):
        logg('call crlf ')
        p['sy']['crlf'](p)
        logg('after crlf')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- <<tn>> -- ') 
    if (r == p['OK']):
        logg('push text <<tn>> ')
        datPush("<<tn>>")
        logg('after <<tn>> ')
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
    logg('processing text -- %cn -- ') 
    if (r == p['OK']):
        logg('push text %cn ')
        datPush("%cn")
        logg('after %cn ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s2 -- ') 
    if (r == p['OK']):
        logg('push text s2 ')
        datPush("s2")
        logg('after s2 ')
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
    logg('processing verb ( strReplace ) ')
    if (r == p['OK']):
        logg('call strReplace ')
        p['sy']['strReplace'](p)
        logg('after strReplace')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('final TAct_1')
#end TAct_1

def TAct (x):
    global p
    logg('begin TAct')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    TActCtl = 1 # starting spoke
    while TActCtl != 0:
        logg('loop TActCtl = ' + TActCtl.__str__())
        if (TActCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (TActCtl == 1):
            logg('call TAct_1')
            TAct_1()
            logg('after call TAct_1')
            # test and adjust for new spoke
            TActCtl = chk(TActCtl)

        else:
            #final
            logg('final TAct')    
            TActCtl = 0 # break
        #endif
    #wend
#end TAct

def FAct_1():
    global p
    logg('FAct_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('processing verb ( crlf ) ')
    if (r == p['OK']):
        logg('call crlf ')
        p['sy']['crlf'](p)
        logg('after crlf')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s3a -- ') 
    if (r == p['OK']):
        logg('push text s3a ')
        datPush("s3a")
        logg('after s3a ')
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
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- pkList -- ') 
    if (r == p['OK']):
        logg('push text pkList ')
        datPush("pkList")
        logg('after pkList ')
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
    logg('processing verb ( strRemove ) ')
    if (r == p['OK']):
        logg('call strRemove ')
        p['sy']['strRemove'](p)
        logg('after strRemove')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( strRemove ) ')
    if (r == p['OK']):
        logg('call strRemove ')
        p['sy']['strRemove'](p)
        logg('after strRemove')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s4 -- ') 
    if (r == p['OK']):
        logg('push text s4 ')
        datPush("s4")
        logg('after s4 ')
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
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- outfloc -- ') 
    if (r == p['OK']):
        logg('push text outfloc ')
        datPush("outfloc")
        logg('after outfloc ')
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
    logg('processing verb ( fout ) ')
    if (r == p['OK']):
        logg('call fout ')
        p['sy']['fout'](p)
        logg('after fout')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text --   -- ') 
    if (r == p['OK']):
        logg('push text   ')
        datPush(" ")
        logg('after   ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('processing text --   -- ') 
    if (r == p['OK']):
        logg('push text   ')
        datPush(" ")
        logg('after   ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- pkList -- ') 
    if (r == p['OK']):
        logg('push text pkList ')
        datPush("pkList")
        logg('after pkList ')
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
    logg('final FAct_1')
#end FAct_1

def FAct (x):
    global p
    logg('begin FAct')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    FActCtl = 1 # starting spoke
    while FActCtl != 0:
        logg('loop FActCtl = ' + FActCtl.__str__())
        if (FActCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (FActCtl == 1):
            logg('call FAct_1')
            FAct_1()
            logg('after call FAct_1')
            # test and adjust for new spoke
            FActCtl = chk(FActCtl)

        else:
            #final
            logg('final FAct')    
            FActCtl = 0 # break
        #endif
    #wend
#end FAct

def FKKAct_1():
    global p
    logg('FKKAct_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('processing text -- <<kn>> -- ') 
    if (r == p['OK']):
        logg('push text <<kn>> ')
        datPush("<<kn>>")
        logg('after <<kn>> ')
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
    logg('processing text -- %cn -- ') 
    if (r == p['OK']):
        logg('push text %cn ')
        datPush("%cn")
        logg('after %cn ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s2a -- ') 
    if (r == p['OK']):
        logg('push text s2a ')
        datPush("s2a")
        logg('after s2a ')
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
    logg('processing verb ( strReplace ) ')
    if (r == p['OK']):
        logg('call strReplace ')
        p['sy']['strReplace'](p)
        logg('after strReplace')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- save -- ') 
    if (r == p['OK']):
        logg('push text save ')
        datPush("save")
        logg('after save ')
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
    logg('processing text -- <<fkTable>> -- ') 
    if (r == p['OK']):
        logg('push text <<fkTable>> ')
        datPush("<<fkTable>>")
        logg('after <<fkTable>> ')
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
    logg('processing text -- %fkn -- ') 
    if (r == p['OK']):
        logg('push text %fkn ')
        datPush("%fkn")
        logg('after %fkn ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- save -- ') 
    if (r == p['OK']):
        logg('push text save ')
        datPush("save")
        logg('after save ')
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
    logg('processing verb ( strReplace ) ')
    if (r == p['OK']):
        logg('call strReplace ')
        p['sy']['strReplace'](p)
        logg('after strReplace')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- save -- ') 
    if (r == p['OK']):
        logg('push text save ')
        datPush("save")
        logg('after save ')
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
    logg('processing text -- <<fkCol>> -- ') 
    if (r == p['OK']):
        logg('push text <<fkCol>> ')
        datPush("<<fkCol>>")
        logg('after <<fkCol>> ')
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
    logg('processing text -- %fkc -- ') 
    if (r == p['OK']):
        logg('push text %fkc ')
        datPush("%fkc")
        logg('after %fkc ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- save -- ') 
    if (r == p['OK']):
        logg('push text save ')
        datPush("save")
        logg('after save ')
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
    logg('processing verb ( strReplace ) ')
    if (r == p['OK']):
        logg('call strReplace ')
        p['sy']['strReplace'](p)
        logg('after strReplace')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('final FKKAct_1')
#end FKKAct_1

def FKKAct (x):
    global p
    logg('begin FKKAct')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    FKKActCtl = 1 # starting spoke
    while FKKActCtl != 0:
        logg('loop FKKActCtl = ' + FKKActCtl.__str__())
        if (FKKActCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (FKKActCtl == 1):
            logg('call FKKAct_1')
            FKKAct_1()
            logg('after call FKKAct_1')
            # test and adjust for new spoke
            FKKActCtl = chk(FKKActCtl)

        else:
            #final
            logg('final FKKAct')    
            FKKActCtl = 0 # break
        #endif
    #wend
#end FKKAct

def FKTAct_1():
    global p
    logg('FKTAct_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('processing text -- <<tn>> -- ') 
    if (r == p['OK']):
        logg('push text <<tn>> ')
        datPush("<<tn>>")
        logg('after <<tn>> ')
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
    logg('processing text -- %cn -- ') 
    if (r == p['OK']):
        logg('push text %cn ')
        datPush("%cn")
        logg('after %cn ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s2a -- ') 
    if (r == p['OK']):
        logg('push text s2a ')
        datPush("s2a")
        logg('after s2a ')
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
    logg('processing verb ( strReplace ) ')
    if (r == p['OK']):
        logg('call strReplace ')
        p['sy']['strReplace'](p)
        logg('after strReplace')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- save -- ') 
    if (r == p['OK']):
        logg('push text save ')
        datPush("save")
        logg('after save ')
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
    logg('processing text -- <<fkTable>> -- ') 
    if (r == p['OK']):
        logg('push text <<fkTable>> ')
        datPush("<<fkTable>>")
        logg('after <<fkTable>> ')
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
    logg('processing text -- %fkn -- ') 
    if (r == p['OK']):
        logg('push text %fkn ')
        datPush("%fkn")
        logg('after %fkn ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- save -- ') 
    if (r == p['OK']):
        logg('push text save ')
        datPush("save")
        logg('after save ')
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
    logg('processing verb ( strReplace ) ')
    if (r == p['OK']):
        logg('call strReplace ')
        p['sy']['strReplace'](p)
        logg('after strReplace')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- save -- ') 
    if (r == p['OK']):
        logg('push text save ')
        datPush("save")
        logg('after save ')
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
    logg('processing text -- <<fkCol>> -- ') 
    if (r == p['OK']):
        logg('push text <<fkCol>> ')
        datPush("<<fkCol>>")
        logg('after <<fkCol>> ')
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
    logg('processing text -- %fkc -- ') 
    if (r == p['OK']):
        logg('push text %fkc ')
        datPush("%fkc")
        logg('after %fkc ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- save -- ') 
    if (r == p['OK']):
        logg('push text save ')
        datPush("save")
        logg('after save ')
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
    logg('processing verb ( strReplace ) ')
    if (r == p['OK']):
        logg('call strReplace ')
        p['sy']['strReplace'](p)
        logg('after strReplace')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- s1o -- ') 
    if (r == p['OK']):
        logg('push text s1o ')
        datPush("s1o")
        logg('after s1o ')
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
    logg('final FKTAct_1')
#end FKTAct_1

def FKTAct (x):
    global p
    logg('begin FKTAct')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    FKTActCtl = 1 # starting spoke
    while FKTActCtl != 0:
        logg('loop FKTActCtl = ' + FKTActCtl.__str__())
        if (FKTActCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (FKTActCtl == 1):
            logg('call FKTAct_1')
            FKTAct_1()
            logg('after call FKTAct_1')
            # test and adjust for new spoke
            FKTActCtl = chk(FKTActCtl)

        else:
            #final
            logg('final FKTAct')    
            FKTActCtl = 0 # break
        #endif
    #wend
#end FKTAct

# stream routines 

def EQS(p):
    logg ('==S')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    needle = 'S'
    if (j.upper() == needle):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
        p['sy']['pback'](p)
        p['sy']['pop']() # absorb pback ok
    #endif
#end EQS

def Msna(p):
    logg ('<<<<sna>>>>')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    p['v']['<<sna>>'] = j
    p['sy']['push'](p['OK']) # status
#endif Msna

def EQ_OP__OP_(p):
    logg ('==((')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    needle = '(('
    if (j.upper() == needle):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
        p['sy']['pback'](p)
        p['sy']['pop']() # absorb pback ok
    #endif
#end EQ_OP__OP_

def EQ_CP__CP_(p):
    logg ('==))')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    needle = '))'
    if (j.upper() == needle):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
        p['sy']['pback'](p)
        p['sy']['pop']() # absorb pback ok
    #endif
#end EQ_CP__CP_

def EQ_CP_(p):
    logg ('==)')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    needle = ')'
    if (j.upper() == needle):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
        p['sy']['pback'](p)
        p['sy']['pop']() # absorb pback ok
    #endif
#end EQ_CP_

def EQ_CP_(p):
    logg ('==)')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    needle = ')'
    if (j.upper() == needle):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
        p['sy']['pback'](p)
        p['sy']['pop']() # absorb pback ok
    #endif
#end EQ_CP_

def Mkn(p):
    logg ('<<<<kn>>>>')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    p['v']['<<kn>>'] = j
    p['sy']['push'](p['OK']) # status
#endif Mkn

def EQ_A__A_(p):
    logg ('==@@')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    needle = '@@'
    if (j.upper() == needle):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
        p['sy']['pback'](p)
        p['sy']['pop']() # absorb pback ok
    #endif
#end EQ_A__A_

def MfkTable(p):
    logg ('<<<<fkTable>>>>')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    p['v']['<<fkTable>>'] = j
    p['sy']['push'](p['OK']) # status
#endif MfkTable

def MfkCol(p):
    logg ('<<<<fkCol>>>>')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    p['v']['<<fkCol>>'] = j
    p['sy']['push'](p['OK']) # status
#endif MfkCol

def EQ_C_(p):
    logg ('==,')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    needle = ','
    if (j.upper() == needle):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
        p['sy']['pback'](p)
        p['sy']['pop']() # absorb pback ok
    #endif
#end EQ_C_

def Mtn(p):
    logg ('<<<<tn>>>>')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    p['v']['<<tn>>'] = j
    p['sy']['push'](p['OK']) # status
#endif Mtn

def EQ_A__A_(p):
    logg ('==@@')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    needle = '@@'
    if (j.upper() == needle):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
        p['sy']['pback'](p)
        p['sy']['pop']() # absorb pback ok
    #endif
#end EQ_A__A_

def MfkTable(p):
    logg ('<<<<fkTable>>>>')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    p['v']['<<fkTable>>'] = j
    p['sy']['push'](p['OK']) # status
#endif MfkTable

def MfkCol(p):
    logg ('<<<<fkCol>>>>')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    p['v']['<<fkCol>>'] = j
    p['sy']['push'](p['OK']) # status
#endif MfkCol

def EQ_C_(p):
    logg ('==,')
    p['sy']['pword'](p)
    p['sy']['pop']() #ok
    j = p['sy']['pop']()
    j = j.__str__()
    needle = ','
    if (j.upper() == needle):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
        p['sy']['pback'](p)
        p['sy']['pop']() # absorb pback ok
    #endif
#end EQ_C_

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

    # externl service vector file
    import strP
    p = strP.main(p)

    # externl service vector file
    import fioiP
    p = fioiP.main(p)

    # externl service vector file
    import filesP
    p = filesP.main(p)

    # paragraph here1
    p['sy']['here1'] = here1
    #

    # paragraph ddlstart
    p['sy']['ddlstart'] = ddlstart
    #

    # paragraph ==S
    p['sy']['==S'] = EQS
    #

    # paragraph <<sna>>
    p['sy']['<<sna>>'] = Msna
    #

    # paragraph ==((
    p['sy']['==(('] = EQ_OP__OP_
    #

    # paragraph ds2
    p['sy']['ds2'] = ds2
    #

    # paragraph ==))
    p['sy']['==))'] = EQ_CP__CP_
    #

    # paragraph ==)
    p['sy']['==)'] = EQ_CP_
    #

    # paragraph ==)
    p['sy']['==)'] = EQ_CP_
    #

    # paragraph keys
    p['sy']['keys'] = keys
    #

    # paragraph keyin
    p['sy']['keyin'] = keyin
    #

    # paragraph <<kn>>
    p['sy']['<<kn>>'] = Mkn
    #

    # paragraph keyin2
    p['sy']['keyin2'] = keyin2
    #

    # paragraph ==@@
    p['sy']['==@@'] = EQ_A__A_
    #

    # paragraph <<fkTable>>
    p['sy']['<<fkTable>>'] = MfkTable
    #

    # paragraph <<fkCol>>
    p['sy']['<<fkCol>>'] = MfkCol
    #

    # paragraph key2
    p['sy']['key2'] = key2
    #

    # paragraph ==,
    p['sy']['==,'] = EQ_C_
    #

    # paragraph tags
    p['sy']['tags'] = tags
    #

    # paragraph tagin
    p['sy']['tagin'] = tagin
    #

    # paragraph <<tn>>
    p['sy']['<<tn>>'] = Mtn
    #

    # paragraph tagin2
    p['sy']['tagin2'] = tagin2
    #

    # paragraph ==@@
    p['sy']['==@@'] = EQ_A__A_
    #

    # paragraph <<fkTable>>
    p['sy']['<<fkTable>>'] = MfkTable
    #

    # paragraph <<fkCol>>
    p['sy']['<<fkCol>>'] = MfkCol
    #

    # paragraph tag2
    p['sy']['tag2'] = tag2
    #

    # paragraph ==,
    p['sy']['==,'] = EQ_C_
    #

    # paragraph SAct
    p['sy']['SAct'] = SAct
    #

    # paragraph KAct
    p['sy']['KAct'] = KAct
    #

    # paragraph TAct
    p['sy']['TAct'] = TAct
    #

    # paragraph FAct
    p['sy']['FAct'] = FAct
    #

    # paragraph FKKAct
    p['sy']['FKKAct'] = FKKAct
    #

    # paragraph FKTAct
    p['sy']['FKTAct'] = FKTAct
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

