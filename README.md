# BASIIS</br>
BNF actuator scripts (for) intelligent information Systems</br>
</br>
# overview:</br>
inspired by BNF https://docs.oracle.com/cd/E19798-01/821-1841/bnbug/index.html </br>
BASIIS describes the parsing of a stream and the actions required to fulfill its execution. </br>
the programatic flow was inspired by FORTH https://www.forth.com/forth/ </br>

# example helloJoe:</br>
def helloJoe :-</br>
[[ 1 ]] "hello " </br>
        "your name" ask </br>
        cats msg .</br>
;</br>
</br>
# explanation </br>
execution is stack based (ala FORTH)</br>
"def" announces the paragraphName ('helloJoe') and ":-" announces the clauses</br>
- literals are pushed onto the stack </br>
-- stack view (("hello",,))</br>
-- stack view (("hello","your name",,))</br>
- ask is an executable verb that requests input - via the prompt - (and places that on the stack)</br>
-- stack view (("hello",/name/,,))</br>
- cats - another verb that concatinates 2 entries on the stack with a space between them eg "hello /name/" replaces (("hello",/name/))</br>
-- stack view (("hello",/name/,,"hello /name/"))</br>
- msg - another verb that prints the top of stack entry onto the screen.</br>
-- stack view ((,,)) ie empty</br>
- . (period) - the end of clause marker.</br>
        

# comments:
pascal comment symbols "/\*" to "\*/" (non-nested) 

# verbs:
all verbs are FORTH based and contained in the file "DoVerb.py".

# special verbs:</br>
-- pwd - gets a "word" from the stream and puts it on the data stack</br>
-- -  words are space ended OR quoted strings.</br>
-- "..." - execute next clause .<br/>
-- tail. - re-executes the paragraph. </br>
-- pushback - backups the stream to allow repicking of this token</br>
-- "code:" - special marker to envelope stream (IE bypass parsing) till "endcode:"</br>
=======</br>
</br>
</br>
# operation:</br>
paragraphs are executed as called</br>
clauses are executed in sequence: </br>
-- on failure the following clause is executed. </br>
-- if all clauses fail the paragraph also fails</br>
verbs are executed in sequence. </br>
-- if a verb fails the clause fails.</br>
-- if the verb is a paragraph name then that paragraph is called (IE executed in place).</br>
=======</br>

# basiiHelper.py
basiiHelper is a "compiler" of BNF into executible python code
it expects a script file with the following format:
"<" outputFilename ">"
[ /paragraph/ ]*
"@endend"
