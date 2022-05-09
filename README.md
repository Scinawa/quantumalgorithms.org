

[![quantumalgorithms.org](https://quantumalgorithms.org/images/mainlogo.png)](https://quantumalgorithms.org)

# README

[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](http://unitary.fund)

> Program is an embodiment of an algorithm. Algorithms works on information, programs works on data. - Donald Knuth.



This is the repository for [QuantumAlgorithms.org](https://quantumalgorithms.org). 

This webiste is meant to be a set of lecture notes for students in quantum algorithms and quantum machine learning. 
It will be updated regularly with new research material. The scope is to bridge the gap between introductory material in quantum computing and research-grade papers, standardize notation, and be an overfiew on the state of useful algorithms for quantum machine learning and information processing.



## How to contribute:

The book is written in bookdown, an R-based extension of markdown (even if you don't need to know R at all, it's simply markdown with some latex). 
Download RStudio and make sure you can compile a book with bookdown on your computer. Once you have it, you can work on the book and submit a PR. 


Feel free to submit a PR with improvements in 

- proofreading
- checking and expanding steps in calculations,
- pointing out sections are ambigious or hard to understand, or that can be explained better,
- create and solve new exercise.

For major contributions (like new chapters or new content), [drop us a line](mailto://scinawa@luongo.pro)!

## How to write an algorithm

The book has some algorithms that are rendered as latex algorithms with a package for writing pseudocode. 
These algorithms are rendered as pdfs, and successively these files are rendered as png via a python script. 
The text of the pseudocode of the algorithm is in the folder /algpseudocode/
When writing new algorithms, please use the template that you find there. 
You can obtain a .png, which can be included in the .Rmd files with a small caption. 
There are countless examples of algorithms included in the book, so you can copy that.



## Style guide, tips&tricks. 

- Use \ket{} and \bra{} instead of |x\rangle
- \begin{equation} and \end{equation} should be used throughout the whole book, as math books have all equation numbered. 
- Always put a citation with [@citationname] to theorems you are citing from papers. 
- Labels for equation equations in bookdown are documented in the bookdown documentation https://bookdown.org/yihui/bookdown/markdown-extensions-by-bookdown.html ( tldr; the way to number equation is the following: (\#eq:raylight) )
- Take the references from google scholar. Select that paper you want, go to cite, and use the biblatex paper. Be sure to include always the year of the document, becuase otherwise you will get an error when trying to compile the pdf version of the document. 
- Every time you compile, (and before doing the pull request) be sure to compile also the pdf version of the document. This becuase there are cases where the generation of the book in htlm succeed, but the pdf is failing. 
- We use runtime not run-time or run time.
- no space between  a dollar sign for equations $ and the first character of the formula (otherwise you get an error)
- currently, it's not possible to put latex in the names of the theorems,lemma, definitions. (do we know how to do it?) For example in the definition of the parametereization of the function $\mu$, I had to use the greek letter μ...
- itemize made with - should start and end with a newline
- always use thm, lem, cor, in references: \@ref(thm:qla). 
- Use the bash comand `grep "\`{lemma" * to have the list of all lemmas (or theorems) so after we can check if they are used correctly with \@ref() and there are no wrong \ref{}. 
- If you need a fast way for translating citation from latex \cite{ciao} to markdown [@ciao], you can use \\cite{(.*?)} -----> [@$1]
