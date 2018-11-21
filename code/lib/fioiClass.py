# file fioiClass.py
# pja 11-09-2018 a) added data prev-iox, curtype w/gets
# --- b) added fpwd() response to -> (token) ; sets self.prev-iox, self.cur-type
# --- c) changed fwhite to skip /* -- */ comments
# --- d) added fpbk() resets self.prev-iox, self.cur-type
# --- d1) added data prev-type -- internal usage
# pja 3-04-2017 tested fpword
# pja 9-24-12 edits to stop till, tillor, ctill on eof
# ------------ edits to clip targetCH to targetCH[0]
# pja 10-17-2012 changed print to #rint
# pja 1-4-13 added getAlpha getNums getAnum
# pja 2-27-13 added type to fpword to transmit "Q" for quoted string "S" for simple string
# notes:
# LALR(n) considerations:
# --- local fpwd,fpback only hold 1 last prev-iox. 
# --- these locals would need to be stacks
# fioi , fioo , get/set iox, flookup , fwhite, ftill,  fctill, ftillor
# fpword, fpback
# fpwd, fpbk
""" test as
import fioiClass
j = fioiClass.fio('tryfi.txt')
j.fpwd()
j.fpwd()
j.fpbk()
"""
class fio():
    def __init__(self,fNa):
        self.fh = open(fNa,'r')
        self.prev_iox = 0
        self.cur_type = '' # unknown at start
    # end init
    def getPrev_iox(self):
        return(self.prev_iox)
    #end getPrev_iox
    def getCur_type(self):
        return(self.cur_type)
    # end getCur_type
    def fioi(self):
        p0 = self.fioxGet()
        ans = self.fh.read(1)
        # test for eof
        p1 = self.fioxGet() # iox after read
        if ( p0 == p1 ):
            ans = '@eofeof'
        #endif
        #rint ('ioi=(',ans,")")
        return(ans)
    # end fioi
    
    def fgetSize(self):
        return(self.fsz)
    #end fgetSize
    
    def fioo(self):
        #rint('ioo')
        j = self.fh.tell()
        j = j -1
        self.fh.seek(j) # resets file pointer
    # end fioo
    
    def fioxGet(self):
        return( self.fh.tell() )
    # end fioxGet
    
    def fioxSet(self,pos):
        self.fh.seek(pos)
    # end fioxSet
    
    def flookup(self,target):
        p1 = self.fioxGet()
        #rint ('p1=',p1)
        c = 0
        for d in range(0,target.__len__()):
            t = self.fioi()
            t = t.__str__()
            #rint ('t=(',t,")")
            #rint ('tar[d]=(',target[d],")")
            if (t != target[d].__str__()):
                c = -1
            #endif
        # end for
        if (c != 0):
            self.fioxSet(p1) # drop back to where you were
        # end if
        return(c) # 0 = ok , -1 = nok
    # end flookup
    def fwhite(self):
        #rint('white called')
        c = 0
        while (c==0):
            m = self.fioi()
            m = m.__str__()
            if (m == ' '):
                c = 0 # stay in loop
            elif (m == chr(8)):
                c = 0 # stay in loop
            elif (m == '\n'):
                c = 0 # stay in loop
            elif (m == '/'):
                self.fwhiteLoop2()
                c = 1 # break
            else:
                c = -1
            # endif
        #wend
        self.fioo() # back up one
    # end fwhite
    
    def fwhiteLoop2(self):
		""" test for /* """
		#rint('loop2')
		p2 = self.fioi()
		#rint('loop2 ioi (' + p2 + ')')
		if (p2 != '*'):
			self.fioo() # back 1 to /
			#exit
		else:
			#begin loop2
			c2 = 0
			while (c2==0):
				#rint('loop2 - loop')
				p3 = self.fioi()
				#rint('p3 (' + p3 + ")")
				if (p3 != '*'):
					c2 = 0 # continue
				else:
					p4 = self.fioi()
					#rint('p4 (' + p4 + ")")
					if (p4 != '/'):
						c2 = 0 # continue
					else:
						self.fioi() # ahead beyond /
						c2 = -1 # break
					#endif p4
				#endif p3
			#wend c2
		#endif p2     
    #end fwhiteLoop2
    
    def ftill(self,targetCH):
        """ skip till target """
        c = 1
        while (c==1):
            j = self.fioi()
            if (j.__str__() == targetCH[0]):
                self.fioo() # put last back
                c = 0
            elif (j.__str__() == '@eofeof'):
                c = -1
            #endif
        #wend
        return(c) # 0 = ok -1 = eof
    #end ftill
    def ftillor(self,targetCHS):
        """ skip till any in target """
        c = 1
        while (c==1):
            j = self.fioi()
            if (j.__str__() == '@eofeof'):
                c = -1 # eof
            else:  
                for m in targetCHS :
                    if (j.__str__() == m ):
                        c = 0
                        self.fioo() # put last back
                    #endif
                #end for
            #endif
        #wend
        
    #end ftillor
    
    def fctill(self,targetCH):
        """ collect till target """
        ans = ''
        c = 1
        while (c==1):
            j = self.fioi()
            if (j.__str__() == '@eofeof'):
                ans = '@eofeof'
                c = -1
            elif (j.__str__() == targetCH[0] ):
                c = 0
            else:
                ans = ans + j.__str__()
            #endif
        #wend
        self.fioo() # put last back
        return(ans)
    #end fctill
    def fctillor(self,targetCHS):
        """ collect till any in target """
        ans = ''
        c = 1
        while (c==1):
            j = self.fioi()
            if (j.__str__() == '@eofeof'):
                c = -1
                ans = '@eofeof'
            else:
                for m in targetCHS:
                    if (j.__str__() == m ):
                        c = 0
                    #endif
                #end for
                if (c != 0):
                    ans = ans + j.__str__()
                #endif
            #endif
        #wend
        self.fioo() # put last back
        return(ans)
    #end fctill
    def fpword(self):
        """ g: [na,na,iox-current] \n
            returns [iox-old,word,iox-new,type] type="Q" for quoted strings , "S" for simple string
        """
        ioxOld = self.fioxGet()
        self.fwhite()
        j = self.fioi()
        self.fioo()
        # if quote grab till next quote
        if (j == '"'):
            ty = "Q"
            w1 = self.fioi() # burn the \q
            wd = self.fctill('"')
            x = self.fioi() # burn the end \q
        else:
            ty = "S"
            wd = self.fctillor([' ','\n'])
        #endif
        ioxNew = self.fioxGet()
        return([ioxOld,wd,ioxNew,ty])
    #end fpword
    def fpwd(self):
        """ adaptor for fpword -> [ioxOld,wd,ioxNew,ty]
            sets internal prev-iox, cur-type
        """
        struct = self.fpword()
        # [ioxOld,wd,ioxNew,ty] # iox already set from fpword
        # set prev-iox
        self.prev_iox = struct[0]
        # set cur-type
        self.cur_type = struct[3]
        # ret token
        return(struct[1])
    #end fpwd
    def fpback(self,struct):
        """ g: [ioxOld,n/a,n/a]
            resets iox to old
        """
        self.fioxSet(struct[0])
        # adjust struct for return
        return([0, ' ',struct[0]])
    #end def
    def fpbk(self):
        """ converter for fpback -> [ioxOld,wd,ioxNew,ty]
        """
        struct = [0,' ',0,' ']
        struct[0] = self.prev_iox
        self.fpback(struct)
        # set type to unknown
        self.cur_type = ''
    #end fpbk
    def fgetAlpha(self):
        """ a-zA-Z """
        ioxOld = self.fioxGet()
        ans = ''
        # the first token must be Alpha
	aZ = 'qwertyuiopajklzxcvbnmdsfgh_QWERTYUIOPAJKLZXCVBNMDSFGH'
	t = self.fioi()
	try:
            m = aZ.index(t)
            ans = t
            a1 = 1
        except:
            a1 = -1
        finally:
            nop = 1
        if (a1 == 1):
            # collect till fail
            c = 0
            while (c==0):
                t1 = self.fioi()
                try:
                    m = aZ.index(t1)
                    ans += t1
                except:
                    c = -1 #break
                    self.fioo() # put the last one back
                finally:
                    nop = 1
                #end try
        else:
            self.fioxSet(ioxOld)
            ans = ''
        #endif
	
        return(ans)
    #end Alpha
    def fgetNum(self):
        """ a-zA-Z """
        ioxOld = self.fioxGet()
        ans = ''
        # the first token must be Alpha
	aZ = '0123456789.'
	t = self.fioi()
	try:
            m = aZ.index(t)
            ans = t
            a1 = 1
        except:
            a1 = -1
        finally:
            nop = 1
        if (a1 == 1):
            # collect till fail
            c = 0
            while (c==0):
                t1 = self.fioi()
                try:
                    m = aZ.index(t1)
                    ans += t1
                except:
                    c = -1 #break
                    self.fioo() # put the last one back
                finally:
                    nop = 1
                #end try
        else:
            self.fioxSet(ioxOld)
            ans = ''
        #endif
	
        return(ans)
    #end fgetNum
    def fgetANum(self):
        """ a-zA-Z """
        ioxOld = self.fioxGet()
        ans = ''
        # the first token must be Alpha
	aZ = '0123456789.qwertyuiopajklzxcvbnmdsfgh_QWERTYUIOPAJKLZXCVBNMDSFGH'
	t = self.fioi()
	try:
            m = aZ.index(t)
            ans = t
            a1 = 1
        except:
            a1 = -1
        finally:
            nop = 1
        if (a1 == 1):
            # collect till fail
            c = 0
            while (c==0):
                t1 = self.fioi()
                try:
                    m = aZ.index(t1)
                    ans += t1
                except:
                    c = -1 #break
                    self.fioo() # put the last one back
                finally:
                    nop = 1
                #end try
        else:
            self.fioxSet(ioxOld)
            ans = ''
        #endif
	
        return(ans)
    #end fgetANum
        
# end class
