#include <algorithm>
#include <functional>
#include <random>

class Generator {
public:
 Generator(unsigned long seed);
 void operator()(std::vector<double>& v);
private:
 std::function<double(double)> randomGenerator;
 std::normal_distribution<double> distribution;
 std::mt19937 uniformGenerator;
};