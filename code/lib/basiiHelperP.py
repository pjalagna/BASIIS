#file basiiHelperP.py
"""history
pja 03-02-2017 cloned from basiiHelper
-------------- added pword pickup instead of getline
===================================
helper writes basii sections that are collected into a final basii file
file format is Basii token + output filename
output filename
pgf :- 
[[ clause# ]] verb till .
; 
or @endend
===================================
test as
filename = 't1.txt'
import basiiHelperP
basiiHelperP.main(filename)
import t1
t1.main('on')
# setting trace
p = mbsi.dump()
p['v']['trace'] = 'on'
mbsi.start(0)

"""
def help():
    out = """
basiis helper ops guide
# usage basiiHelperP.main(filename)

          """
    print(out)
#end help
def pword():
    global fi,nds
    j = fi.fpword()
    if (nds['trace'] == 'on'):
        logg ('pword =(' + j.__str__() + ")")
    #endif
    return(j)
#end pword
def main(filename):
    import fioiClass
    global fi
    fi = fioiClass.fio(filename)
    global sec
    sec = {}
    sec['input'] = filename
    sec['outfile']= pword()
    prepSec()
    ffo = open(sec['outfile'],'w')
    ffo.write(sec['hx0']) #file header
    sec['mx3'] = ''
    paragraph(fh,ffo)
    ffo.write(sec['hx2'] + sec['mx3'] + sec['hx4'])
    ffo.write(sec['hx1'])
    ffo.close()
    fh.close()
#end main
def paragraph(fh,ffo):
    global sec
    pp = 0
    while (pp == 0):
        pgn = pword()
        if (pgn.upper() == '@ENDEND'):
            pp = -1 #break
        else:
            # add your name to the symbol table
            sec['mx3'] = sec['mx3'] + sec['hx3'].replace('%pn%',pgn)
            # gen pgf header
            sec['pgx1'] = sec['hxp1'] .replace('%pgn%', pgn)
            sec['pgx3'] = sec['hxp3'] .replace('%pgn%', pgn)
            # call clauses
            sec['pgx2'] = ''
            clauses(fh,ffo)
            # write paragraph output
            ffo.write( sec['pgx1'] + sec['pgx2'] + sec['pgx3'])
            print('pgf...' + pgn )
        #endif
    #wend
#end pgf
        
def clauses(fh,ffo):
    global sec
    d = 0
    while (d == 0):
        op = pword()
        if (op == ';'):
            d = -1 # break
        else:
            cn = pword()
            bop = pword()
            sec['cl2'] = ''
            # add your call to paragraph
            sec['pgx2'] =sec['pgx2'] + sec['hxp2'].replace('%cln%',cn)
            # gen head and tail
            sec['cl1'] = sec['hc1'].replace('%cln%',cn)
            sec['cl3'] = sec['hc3'].replace('%cln%',cn)
            verbs(fh)
            # write clause output
            ffo.write(sec['cl1'] + sec['cl2'] + sec['cl3'])
        #endif
    #wend
#end clauses
def verbs(fh):
    vv = 0
    while (vv == 0):
        vn = pword()
        if (vn == "."):
            nop = "<removed code see notes =a=>"
            vv = -1 #break
        else:
            if (vn[0] == '"'):
                sec['cl2'] = sec['cl2'] + """
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('push """ + vn + """')
        #endif
        datPush(""" + vn + """)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after """ + vn + """')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    """
            else:
                sec['cl2'] = sec['cl2'] + """
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call """ + vn + """')
        #endif
        p['sy']['""" + vn + """'](p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after """ + vn + """')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    """

            #endif
        #endif
    #wend
#end verbs
            
    
        
def pword():
    m = fh.readline()
    m = m[0:-1]
    return(m)
#end getline

def prepSec():
    global sec
    sec['sy'] = {}
    sec['hx0'] = """
#file """ + sec['outfile'] + """
#generated for """ + sec['input'] + """ \n\n """

    sec['hx1'] = """
# helper rtns 
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

def help():
    out = " usage \\n"
    out += "import NAME \\n"
    out += "z = NAME.main(startpoint,trace) \\n"
    out += "z =  NAME.dump() # grabs and allows passage of vectors \\n"
    out += "to add externial vectors: \\n"
    out += "import process \\n"
    out += "z['sy']['token'] = process.subprocessName \\n"
    out += "NAME.take(z) - adds vectors into process  \\n"
    print(out)
#end help

"""
    sec['hx2'] = """
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
"""
    sec['hx3'] = """
    # 
    p['sy']['%pn%'] = %pn%
    #
"""
    sec['hx4'] = """
        p['sy']['start'] = p['sy'][startpoint] 
#end main
def start(trace='off'):
    p['sy']['start'](trace) # process begins at start
#end start
"""
    sec['hxp1'] = """
def %pgn% (x):
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input('%pgn%')
        #print('dat',p['dat'])
    #endif
    datPush(p['NOK'])
"""
    sec['hxp2'] = """
    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call %cln%')
        #endif
        %cln%()
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after call %cln%')
        #endif
    #endif
    #
"""
    sec['hxp3'] = """
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final %pgn%')    
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end %pgn%
"""
    sec['hc1'] = """
def %cln%():
    global p
    
    if (p['v']['trace'] == 'on'):
        nop = raw_input('%cln%')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])
"""
    sec['hc2'] = """
    # 
    r =  p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            nop = raw_input('call %vn%')
        #endif
        %vn%(p)
        if (p['v']['trace'] == 'on'):
            nop = raw_input('after %vn%')
        #endif
    #endif
    #
"""
    sec['hc3'] = """
    #final
    if (p['v']['trace'] == 'on'):
        nop = raw_input('final %cln%')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end %cln%
"""
#end prepSec
    

    
        
    