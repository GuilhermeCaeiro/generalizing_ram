# Generalizing RAM (G-RAM)

The Generalizing RAM Weightless model is a neural node (artificial neuron) that tries to add generalization capabilities to the Probabilistic Logic Node (PLN) through the use of a "spreading" phase, where stored values are propagated to nearby addresses (according to the Hamming Distace between them). A brief explanation on how the G-RAM and the PLN models work is given by [1] and [2].

The code present in this repository is an attempt of an implementation of the standard G-RAM, that uses a "matrix" instead of a hash map or something like that to represent the memory. For that reason, the G-RAM present here is very inefficient.

A simple usage test can be found in the file "test.py".

## References

[1] T. B. Ludermir, A. Carvalho, A. P. Braga and M. C. P. Souto, “Weightless Neural Models: A Review of Current and Past Works”, Neural Computing Surveys 2, pp. 41-60, 1999.

[2] I. Aleksander, M. De Gregorio, F. M. G. França, P. M. V. Lima and H. Morton, “A brief introduction to Weightless Neural Systems”, In ESANN, pp. 299-305, 2009.
