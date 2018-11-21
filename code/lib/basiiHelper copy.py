#file basiiHelper.py
"""history
pja 11/07/2018 changed get-line to getword
-- needs to return type [Q[uoted] or S[imple]] for lit pickup
pja 11/05/2018 added verb manifest
pja 03/05/2018 added pgf name to clause name 
---------------- to eleminate clause name collisions
pja 02/28/2018 #28 added helper rtns logg and chk to hx1
-------------- added new hxp1,hxp2,hxp3
-------------- added new 
pja 02/27/2018 #27 added for tail recursion
--- NOT tested
pja 2 10 2018 edits for trace etc
-- added take(architecture_array,vectorfile)
---- adds to vectors from external files
pja 2 24 2017 made trace step via raw_input
              changed start[0] to start[p]
NEED to include an ops guide to usage for created files

pja 1 1 14 added optional main trace parameter
pja 1 1 14 added final trace po
pja 1 1 14 tested 
pja 1 1 14 amended clause template code to pass nok to next verb
pja 12 31 13 original
===================================
helper writes basii sections that are collected into a final basii file
file format is token per line
output filename
pgf :-
[[ clause ]] *verb till . .
; or @endend
===================================
test as
filename = 't1.txt'
import basiiHelper
basiiHelper.main(filename)
import t1
t1.main('on')
# setting trace
p = mbsi.dump()
p['v']['trace'] = 'on'
mbsi.start(0)

"""
def help():
    out = """
see basii helper ops guide for usage protocols
# usage
basiiHelper.main(filename)

          """
    print(out)
#end help

def main(filename):
    global sec
    sec = {}
    sec['manifest'] = {} # manifest of verbs
    sec['sy'] = {} # symbol table
    sec['input'] = filename
    """ old code
    fh = open(filename,'r')
    """
    import fioiClass
    sec['sy']['fio'] = fioiClass.fio(filename)
    sec['outfile'] = VWord()
    """ sec['outfile']= VWord() """
    prepSec()
    ffo = open(sec['outfile'],'w')
    ffo.write(sec['hx0']) #file header
    sec['mx3'] = ''
    paragraph(ffo)
    ffo.write(sec['hx2'] + sec['mx3'] + sec['hx4'])
    ffo.write(sec['hx1'])
    ffo.close()
    # fh.close()
    # write mainfest
    ffm = open(sec['outfile']+'.manifest.txt','w')
    for xm in sec['manifest'].keys():
        ffm.write(xm + '\n')
    #end for
    ffm.close
#end main
def paragraph(ffo):
    global sec
    pp = 0
    while (pp == 0):
        pgn = VWord()
        
        sec['pgn'] = pgn #27
        if (pgn.upper() == '@ENDEND'):
            pp = -1 #break
        else:
            pgnCd = VWord() # :-
            # add your name to the symbol table
            sec['mx3'] = sec['mx3'] + sec['hx3'].replace('%pn%',pgn)
            # manifest
            sec['manifest']["P:"+pgn] = 'paragraph'
            # gen pgf header
            sec['pgx1'] = sec['hxp1'] .replace('%pgn%', pgn)
            sec['pgx3'] = sec['hxp3'] .replace('%pgn%', pgn)
            # call clauses
            sec['ctlName'] = pgn #27
            sec['ctlCtr'] = 0 #27
            sec['pgx2'] = ''
            clauses(ffo)
            # write paragraph output
            ffo.write( sec['pgx1'] + sec['pgx2'] + sec['pgx3'])
            print('pgf...' + pgn )
            # record paragraph call in manifest
            sec['manifest'][pgn] = 'paragraph'
        #endif
    #wend
#end pgf
        
def clauses(ffo):
    global sec
    """
    sec['ctlName'] = pgn #27
    sec['ctlCtr'] = 0 #27
    sec['pgx2'] = '' 
    fill 'cl2'
    """
    d = 0
    while (d == 0):
        op = VWord()
        if (op == ';'):
            d = -1 # break
        else:
            cn = VWord()
            bop = VWord()
            sec['cl2'] = ''
            # add your call to paragraph
            #28 with counter
            ans = sec['hxp2'].replace('%cln%',cn)
            ans = ans.replace('%pgn%',sec['ctlName'])
            # adjust counter and replace
            sec['ctlCtr'] = sec['ctlCtr'] +1
            ans = ans.replace('%ctlctr%',sec['ctlCtr'].__str__())
            # add to clause call
            sec['pgx2'] =sec['pgx2'] + ans 
            # gen head and tail
            ans = sec['hc1'].replace('%cln%',cn)
            ans = ans.replace('%pgn%',sec['pgn'])
            sec['cl1'] = ans 
            ans = sec['hc3'].replace('%cln%',cn)
            ans = ans.replace('%pgn%',sec['pgn'])
            sec['cl3'] = ans 
            verbs()
            # write clause output
            ffo.write(sec['cl1'] + sec['cl2'] + sec['cl3'])
        #endif
    #wend
#end clauses
def verbs():
    vv = 0
    while (vv == 0):
        vn = VWord()
        if (vn == "."):
            nop = "<removed code see notes =a=>"
            vv = -1 #break
        else:
            # test for quoted string
            if (sec['sy']['ftype'] == "Q"):
                sec['cl2'] = sec['cl2'] + sec['hcl2v0'].replace('%vn%',vn)
            else:
                sec['cl2'] = sec['cl2'] + sec['hcl2vn0'].replace('%vn%',vn)
                sec['manifest'][vn] = vn # add verb to manifest 
            #endif
        #endif
    #wend
#end verbs
                    
def VWord():
    m = fh.readline()
    m = m[0:-1]
    print('getline=' + m )
    return(m)
#end getline

def prepSec():
    global sec
    # sec['sy'] = {}
    sec['hx0'] = """
#file """ + sec['outfile'] + """
#generated for """ + sec['input'] + """ \n\n """

    sec['hx1'] = """
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
    out = " usage \\n"
    out += "import NAME \\n"
    out += "z = NAME \\n"
    out += "z.main(startpoint,trace) prepares vectors \\n"
    out += "v =  NAME.dump() # grabs and allows passage of vectors \\n"
    out += "to execute: \\n"
    out += "-- z.start(trace) \\n \\n"
    out += "to add externial vectors: \\n"
    out += "v /*from dump */ = NAME.take(v,VectorFilename) - adds vectors into process via file \\n"
    out += "format of vectorFile: \\n"
    out += "-1 def main(v) sets and returns structure v \\n"
    out += "--- v['sy'][verbName] = procName \\n"
    out += "-2 def procName(v) \\n"
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

"""
    sec['hx2'] = """
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
"""
    sec['hx3'] = """
    # paragraph %pn%
    p['sy']['%pn%'] = %pn%
    #
"""
    sec['hx4'] = """
    p['sy']['start'] = p['sy'][startpoint] 
#end main
def start(trace='off'):
    p['v']['trace'] = trace # save trace setting
    p['sy']['start'](trace) # process begins at start
#end start
"""
    sec['hxp1'] = """
def %pgn% (x):
    global p
    logg('begin %pgn%')
    datPush(p['NOK']) # preset data condition
    ## point of umbrella
    %pgn%Ctl = 1 # starting spoke
    while %pgn%Ctl != 0:
        logg('loop %pgn%Ctl = ' + %pgn%Ctl.__str__())
        if (%pgn%Ctl == -1):
            nop = -1 # false test to set up elif chain
"""
    sec['hxp2'] = """
        elif (%pgn%Ctl == %ctlctr%):
            logg('call %pgn%_%cln%')
            %pgn%_%cln%()
            logg('after call %pgn%_%cln%')
            # test and adjust for new spoke
            %pgn%Ctl = chk(%pgn%Ctl)
"""


    sec['hxp3'] = """
        else:
            #final
            logg('final %pgn%')    
            %pgn%Ctl = 0 # break
        #endif
    #wend
#end %pgn%
"""
    sec['hc1'] = """
def %pgn%_%cln%():
    global p
    logg('%pgn%_%cln%')
    datPush(p['OK'])
"""
    sec['hc2'] = """
    #
    logg('process %vn%') 
    r =  p['sy']['pop']()
    if (r == p['OK']):
        logg('call %vn%')
        %vn%(p)
        logg('after %vn%')
    #endif
    #
"""
    sec['hc3'] = """
    #final
    logg('final %pgn%_%cln%')
#end %pgn%_%cln%
"""
    sec['hcl2v0'] = """
    r = p['sy']['pop']()
    logg('processing text -- %vn% -- ') 
    if (r == p['OK']):
        logg('push text %vn% ')
        datPush("%vn%")
        logg('after %vn% ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif
"""
    sec['hcl2vn0'] = """
    r = p['sy']['pop']()
    logg('processing verb ( %vn% ) ')
    if (r == p['OK']):
        logg('call %vn% ')
        p['sy']['%vn%'](p)
        logg('after %vn%')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif
"""
#end prepSec
def getSec():   
    global sec
    return(sec)
#end getSec
def VWord():
    m = sec['sy']['fio'].fpword()
    sec['sy']['previox'] = m[0]
    ans = m[1]
    sec['sy']['curiox'] = m[2]
    sec['sy']['ftype'] = m[3]
    return(ans)
#end VWord 
    
        
    
