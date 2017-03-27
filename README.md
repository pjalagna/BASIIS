# BASIIS
BNF actuator scripts (for) intelligent information Systems
keys:
<br />"!"name"!" get input token and save to name
<br />"value" - if input is this value
<br />special verbs:
<br />tail. - re-executes the paragraph. 
<br />pushback - backups the stream to allow repicking of this token
<br />code: - special marker to envelope stream till endcode:

operation:
<br />paragraphs are executed as called
<br />clauses are executed in sequence till success. 
<br />-- on failure the following clause is executed. 
<br />-- if all clauses fail a called paragraph also fails
<br />verbs are executed in sequence. 
<br />-- if a verb fails the clause fails.
<br />-- if the verb is a paragraph name then that paragraph is called.

input format:
start :-
[[ 1 ]] !output-filename! body .
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
[[ 3 ]] "[[" !clauseName! "]]" getVerbs tail.
;
getVerbs :-
[[ 1 ]] "/*" doComment tail. 
[[ 2 ]] "@endend" pushback .
[[ 3 ]] ";" endClause .
[[ 4 ]] !verbName! tail.
;
endClause :-
[[ 1 ]] code: endcode: .
;
endParagraph :-
[[ 1 ]] code: endcode:


