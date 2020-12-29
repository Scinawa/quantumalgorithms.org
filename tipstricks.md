# tips and tricks

- no space between  a dollar sign for equations $ and the first character of the formula (otherwise you get an error)
- currently, it's not possible to put latex in the names of the theorems,lemma, definitions. (do we know how to do it?) For example in the definition of the parametereization of the function $\mu$, I had to use the greek letter μ...
- itemize made with - should start and end with a newline
- the way to number equation is the following: (\#eq:raylight)
- This is the templtae to use to create an issue automatically using the github action
- always use thm, lem, cor, in references: \@ref(thm:qla). 
- grep "\`{lemma" * to have the list of all lemmas (or theorems) so after we can check if they are used correctly with \@ref() and there are no wrong \ref{}. 
- the correct way of doing todo is:
<!-- 
# TODO 
# labels: 
-->

- If you need a fast way for translating citation from latex \cite{ciao} to markdown [@ciao], you can use \\cite{(.*?)} -----> [@$1]
- 
