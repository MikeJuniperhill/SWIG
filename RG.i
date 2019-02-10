%module RG
%{
#include "RG.h"
%}

// get support for STL C++ vector class
// using vector involves the use of template directive.
// note: 'DoubleVector' is the name for data structure to be used in python program
%include "std_vector.i"
%template(DoubleVector) std::vector<double>;

%include "RG.h"