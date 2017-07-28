# BASIIS
BNF actuator scripts (for) intelligent information Systems
keys:
<<<<<<< HEAD
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
=======
<br />"{"name"}" get input token and save to name
<br />?name="value" - if input is this value
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
>>>>>>> origin/master

input format:
start :-
[[ 1 ]] {output-filename} body .
;
body :-
[[ 1 ]] {b1} ?b1="/star" doComment tail. .
[[ 2 ]] ?b1="@endend" finalSave .
[[ 3 ]] paragraphs tail.
;
paragraphs :-
[[ 1 ]] {p1} ?p1="/star" doComment tail. 
[[ 2 ]] ?p1="@endend" pushback .
[[ 3 ]] {ParagraphName} {p2} ?p2=":-" 
   doClauses  endParagraph tail.
;
doClauses :-
[[ 1 ]] {c1} ?c1="/star" doComment tail. 
[[ 2 ]] ?c1="@endend" pushback .
[[ 3 ]] doClause tail.
;
doClause :-
[[ 1 ]] {dc1} ?dc1="/star" doComment tail. 
[[ 2 ]] ?dc1="@endend" pushback .
[[ 3 ]] ?dc1="[[" {clauseName} {dc2} ?dc2="]]" getVerbs tail.
;
getVerbs :-
[[ 1 ]] {gv1} ?gv1="/*" doComment tail. 
[[ 2 ]] ?gv1="@endend" pushback .
[[ 3 ]] ?gv1=";" endClause .
[[ 4 ]] {verbName} doverb tail.
;
endClause :-
[[ 1 ]] code: endcode: .
;
endParagraph :-
[[ 1 ]] code: endcode:


