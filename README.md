# BASIIS
BNF actuator scripts (for) intelligent information Systems
keys:
"<"name">" get input token and save to name
"value" - if input is this value
special verbs:
tail. - re-executes the paragraph. 
pushback - backups the stream to allow repicking of this token
code: - special marker to envelope stream (IE bypass parsing) till endcode:

operation:
paragraphs are executed as called
clauses are executed in sequence: 
-- on failure the following clause is executed. 
-- if all clauses fail the paragraph also fails
verbs are executed in sequence. 
-- if a verb fails the clause fails.
-- if the verb is a paragraph name then that paragraph is called (IE executed in place).

input format:
start :-
[[ 1 ]] <output-filename> body .
;
body :-
[[ 1 ]] "/*" doComment tail. 
[[ 2 ]] "@endend" finalSave .
[[ 3 ]] paragraphs tail.
;
paragraphs :-
[[ 1 ]] "/*" doComment tail. 
[[ 2 ]] "@endend" pushback .
[[ 3 ]] getParagraphName ":-" doClauses  endParagraph tail.
;
doClauses :-
[[ 1 ]] "/*" doComment tail. 
[[ 2 ]] "@endend" pushback .
[[ 3 ]] doClause tail.
;
doClause :-
[[ 1 ]] "/*" doComment tail. 
[[ 2 ]] "@endend" pushback .
[[ 3 ]] "[[" <clauseName> "]]" getVerbs tail.
;
getVerbs :-
[[ 1 ]] "/*" doComment tail. 
[[ 2 ]] "@endend" pushback .
[[ 3 ]] ";" endClause .
[[ 4 ]] <verbName> tail.
;
endClause :-
[[ 1 ]] code: endcode: .
;
endParagraph :-
[[ 1 ]] code: endcode:


