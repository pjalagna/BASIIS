# file filesP.py
"""
pja 11-26-2018 orig

secondary files for file maintenance

test as
# platform
p = {}
p['OK'] = "ok"
p['NOK'] = "nok"
p['sy'] = {}
p['dat'] = []
# recreate push pop
p['sy']['pop'] = p['dat'].pop # no parens
p['sy']['push'] = p['dat'].append # no parens
import time
# test
import filesP
p = filesP.main(p)
fn = './out/tt1.txt'
p['sy']['push']('hello you') 
p['sy']['push'](fn)
p['sy']['fout'](p)
j = p['sy']['pop']() #ok
j #see
p['dat'] #check
p['sy']['push']( time.asctime() + '\n')
p['sy']['push'](fn)
p['sy']['fout'](p)
p['dat'] # dump to check
j = p['sy']['pop']() #ok
j #see
p['dat'] # check clean
# read test
p['sy']['push'](fn)
p['sy']['fin'](p)
j = p['sy']['pop']() #ok status
j #see
jx = p['sy']['pop']() #txt
print(jx) #see
p['dat'] # check clean
# fclear test
p['sy']['push'](fn)
p['sy']['fclear'](p)
j = p['sy']['pop']() #ok status
j #see
p['dat'] # check clean
# read again to test
p['sy']['push'](fn)
p['sy']['fin'](p)
j = p['sy']['pop']() #ok status
j #see
jx = p['sy']['pop']() #txt
print(jx) #see
p['dat'] # check clean


========= raw test ==============
fn = './out/tt1.txt'
import time
filesP.fout(fn , time.asctime() + '\n')
filesP.fout(fn , 'hello you1')
filesP.fout(fn , 'hello you2')
j = filesP.fin(fn)
print(j)
filesP.fclear(fn)
j2 = filesP.fin(fn)
print(j2)
"""
def main(p):
    p['sy']['fout'] = foutP
    p['sy']['fin'] = finP
    p['sy']['fclear'] = fclearP
    return(p)
#end main
def foutP(p):
    fn = p['sy']['pop']()
    txt = p['sy']['pop']()
    fout(fn,txt)
    p['sy']['push'](p['OK'])
#end foutP
def fout(fn,txt):
    th = open(fn,'a')
    th.write(txt)
    th.close() # to clear file open limits
#end fout
def finP(p):
    fn = p['sy']['pop']()
    ans = fin(fn)
    p['sy']['push'](fstr(ans))
    p['sy']['push'](p['OK'])
def fstr(inp):
    ans2 = ''
    # convert to one string
    for x in range(inp.__len__()):
        ans2 = ans2 + inp[x]
    #endfor
    return(ans2)
#end fstr
def fin(fn):
    th = open(fn,'r')
    ans = th.readlines()
    th.close() # to clear file open limits
    return(ans)
#end fin
def fclearP(p):
    fn = p['sy']['pop']()
    fclear(fn)
    p['sy']['push'](p['OK'])
#end fclearP
def fclear(fn):
    th = open(fn,'w')
    th.close() # to clear file open limits
#end fclear


