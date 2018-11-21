def eqeq(needle)
    trace
    op1 = pop()
    op1 = op1.upper()
    op2 = needle.upper()
    if (op1 == op2):
        push ok
    else:
        push nok
    #endif
#end eqeq
