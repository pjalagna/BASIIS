# file SQSQ.py
"""
character converter for protected reads/writes
pja 11/10/2018 orig

test as
import SQSQ
t = SQSQ
a = 'abcd#$.-()<>%'
b = t.SQin(a)
b
c = t.SQout(b)
"""
def SQin(strin):
    a = strin
    a = a.replace('!','_B_')
    a = a.replace('.','_PD_')
    a = a.replace('@','_A_')
    a = a.replace('#','_P_')
    a = a.replace('%','_PC_')
    a = a.replace('(','_OP_')
    a = a.replace(')','_CP_')
    a = a.replace('<','_LT_')
    a = a.replace('>','_GT_')
    a = a.replace('?','_H_')
    a = a.replace(';','_SC_')
    a = a.replace(',','_C_')
    a = a.replace(':','_CO_')
    a = a.replace('&','_AN_')
    a = a.replace('*','_AM_')
    a = a.replace('=','_EQ_')
    return(a)
#end SQin

def SQout(strin):
    a = strin
    a = a.replace('_B_','!')
    a = a.replace('_PD_','.')
    a = a.replace('_A_','@')
    a = a.replace('_P_','#')
    a = a.replace('_PC_','%')
    a = a.replace('_OP_', '(')
    a = a.replace('_CP_',')')
    a = a.replace('_LT_','<')
    a = a.replace('_GT_','>')
    a = a.replace('_H_','?')
    a = a.replace('_SC_',';')
    a = a.replace('_C_',',')
    a = a.replace('_CO_',':')
    a = a.replace('_AN_','&')
    a = a.replace('_AM_','*')
    a = a.replace('_EQ_','=')
    return(a)
#end SQout

