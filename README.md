# BASIIS</br>
BNF actuator scripts (for) intelligent information Systems</br>
keys:</br>
<<<<<<< HEAD</br>
"<"name">" get input token and save to name</br>
"value" - if input is this value</br>
special verbs:</br>
tail. - re-executes the paragraph. </br>
pushback - backups the stream to allow repicking of this token</br>
code: - special marker to envelope stream (IE bypass parsing) till endcode:</br>
</br>
operation:</br>
paragraphs are executed as called</br>
clauses are executed in sequence: </br>
-- on failure the following clause is executed. </br>
-- if all clauses fail the paragraph also fails</br>
verbs are executed in sequence. </br>
-- if a verb fails the clause fails.</br>
-- if the verb is a paragraph name then that paragraph is called (IE executed in place).</br>
=======</br>
<br />"{"name"}" get input token and save to name</br>
<br />?name="value" - if input is this value</br>
<br />special verbs:</br>
<br />tail. - re-executes the paragraph. </br>
<br />pushback - backups the stream to allow repicking of this token</br>
<br />code: - special marker to envelope stream till endcode:</br>
</br>
operation:</br>
<br />paragraphs are executed as called</br>
<br />clauses are executed in sequence till success. </br>
<br />-- on failure the following clause is executed. </br>
<br />-- if all clauses fail a called paragraph also fails</br>
<br />verbs are executed in sequence. </br>
<br />-- if a verb fails the clause fails.</br>
<br />-- if the verb is a paragraph name then that paragraph is called.</br>
>>>>>>> origin/master</br>
</br>
input format:</br>
start :-</br>
[[ 1 ]] {output-filename} body .</br>
;</br>
body :-</br>
[[ 1 ]] {b1} ?b1="/star" doComment tail. .</br>
[[ 2 ]] ?b1="@endend" finalSave .</br>
[[ 3 ]] paragraphs tail.</br>
;</br>
paragraphs :-</br>
[[ 1 ]] {p1} ?p1="/star" doComment tail. </br>
[[ 2 ]] ?p1="@endend" pushback .</br>
[[ 3 ]] {ParagraphName} {p2} ?p2=":-" </br>
   doClauses  endParagraph tail.</br>
;</br>
doClauses :-</br>
[[ 1 ]] {c1} ?c1="/star" doComment tail. </br>
[[ 2 ]] ?c1="@endend" pushback .</br>
[[ 3 ]] doClause tail.</br>
;</br>
doClause :-</br>
[[ 1 ]] {dc1} ?dc1="/star" doComment tail. </br>
[[ 2 ]] ?dc1="@endend" pushback .</br>
[[ 3 ]] ?dc1="[[" {clauseName} {dc2} ?dc2="]]" getVerbs tail.</br>
;</br>
getVerbs :-</br>
[[ 1 ]] {gv1} ?gv1="/*" doComment tail. </br>
[[ 2 ]] ?gv1="@endend" pushback .</br>
[[ 3 ]] ?gv1=";" endClause .</br>
[[ 4 ]] {verbName} doverb tail.</br>
;</br>
endClause :-</br>
[[ 1 ]] code: endcode: .</br>
;</br>
endParagraph :-</br>
[[ 1 ]] code: endcode:</br>
</br>
</br>
