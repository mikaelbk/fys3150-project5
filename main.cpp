#include <iostream>
#include <string>
#include <armadillo>
#include <cmath>
#include <random> 

using namespace std;
using namespace arma;

int main(int argc, char const *argv[])
{
	// RNG
	std::random_device rd;
	std::mt19937_64 gen(rd());
	std::uniform_real_distribution<int> randAgent(0.0,1.0);

	// "Initial conditions"
	double input = atof(argv[1]);
	int N = 500;
	int tpmcc = int(pow(10,7));
	int mcc = int(pow(10,3));
	double m0 = 2.0;

	int k;
	int l;

	// other declerations
	mat agents(N,mcc);
	agents.col(0) = m0*ones<vec>(N);

	for (int i = 0; i < mcc; ++i)
	{
		cout << "mcc#\t" << i << endl;
		for (int j = 0; j < tpmcc; ++j)
		{
			k = int(N*randAgent(gen));
			l = int(N*randAgent(gen));
		}
	}

	return 0;
}