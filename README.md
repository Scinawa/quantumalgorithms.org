# Welcome to the repository for quantumalgorithms.org

[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](http://unitary.fund)


This is the repository for [QuantumAlgorithms.org](https://quantumalgorithms.org). 

This webiste is meant to be a set of lecture notes for students in quantum algorithms and quantum machine learning. 
It will be updated regularly with new research material. The scope is to bridge the gap between introductory material in quantum computing and research-grade papers, standardize notation, and be an overfiew on the state of useful algorithms for quantum machine learning and information processing.


The book is written in bookdown, an R-based extension of markdown (even if you don't need to know R at all, it's simply markdown with some latex). 


## What to do

The current issues that we have, for which we  are roughly organized as follows:

- minor issues: 
  - proofreading
  - checking and expanding steps in calculations,
  - making sure things are written in good and clearn english
  - pointing out paragraphs that are not mathematically clear, or that could be expanded)
- major contributions (like new chapters)
- create and solve new exercise
- address the TODOs that are inserted in the comments of the .Rmd files. 

Please refer to the file tipsandtricks.md for small but useful tips on Rmarkdown. 

In any case, if you want to contribute, [drop me a line](mailto://scinawa@luongo.pro)!

## How to render an algorithm for the book

The book has some algorithms that are rendered as latex algorithms with a package for writing pseudocode. 
These algorithms are rendered as pdfs, and successively these files are rendered as png via a python script. 
The text of the pseudocode of the algorithm is in the folder /algpseudocode/
When writing new algorithms, please use the template that you find there. 
You can obtain a .png, which can be included in the .Rmd files with a small caption. 
There are countless examples of algorithms included in the book, so you can copy that.



## Guidelines for writings

- Use \ket{} and \bra{} instead of |x\rangle
- \begin{equation} and \end{equation} in bookdown are not really working 100% of the time (check?), but they should be used throughout the whole book, as math book have all equation numbered. 
- Labels for equation equations are documented in the bookdown documentation https://bookdown.org/yihui/bookdown/markdown-extensions-by-bookdown.html
- Take the references from google scholar. Select that paper you want, go to cite, and use the biblatex paper. Be sure to include always the year of the document, becuase otherwise you will get an error when trying to compile the pdf version of the document. 
- Every time you compile, (and before doing the pull request) be sure to compile also the pdf version of the document. This becuase there are cases where the generation of the book in htlm succeed, but the pdf is failing for some reasons. 
- Use \~ before the citation.
- We use runtime not run-time or run time.

