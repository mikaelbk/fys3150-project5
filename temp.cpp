#include <cmath>
#include <iomanip>
#include <iostream>
#include <string>
#include <armadillo>

using namespace std;
using namespace arma;

int main(int argc, char const *argv[])
{
	mat matrix(10,10);
	matrix.print();
	return 0;
}