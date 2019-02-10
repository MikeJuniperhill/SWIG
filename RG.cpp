#include "RG.h"

Generator::Generator(unsigned long seed) {
  // construct lambda method for processing standard normal random number
  randomGenerator = [this](double x)-> double {
   x = distribution(uniformGenerator);
   return x;
  };
  uniformGenerator.seed(seed);
}

// fill client-given vector with random 
// variates from standard normal distribtuion
void Generator::operator()(std::vector<double>& v) {
  std::transform(v.begin(), v.end(), v.begin(), randomGenerator);
}