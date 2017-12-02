#include <cmath>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <random>
#include <armadillo>
#include <string>
using namespace std;
using namespace arma;
ofstream ofile;

void matrixTransactions(int, int, double, double, double, mat&, int);

int main(int argc, char const *argv[])
{
	// thrown message with bad usage of program call
	if (argc != 8) {
		cout << "\tError: Invalid number of arguments. Program requires the following call:" << endl;
		cout << "\t" << argv[0] << " N mcc l m0 a g filename" << endl;
		//cout << "\tWhere the arguments are:\n\tL:\tSquare root of the number of lattice points for the LxL lattice\n\tmcc:\tNumber of Montecarlo cycles. If less than 20 then is set to 10^mcc\n\tti:\tstarting temperature of experiment\n\ttf:\tfinal temperature of experiment\n\tnt:\tnumber of measurements between ti and tf" << endl;
		exit(1);
	}
	// "Initial conditions"
	int N = atoi(argv[1]);
	int mcc = atoi(argv[2]);
	double saving = atof(argv[3]);
	double m0 = atof(argv[4]);
	double a = atof(argv[5]);
	double g = atof(argv[6]);
	string filename = argv[7];
	int transactions = int(pow(10,7));

	// other declerations
	mat agents(N,mcc);
	agents.col(0) = m0*ones<vec>(N);

	matrixTransactions(N, mcc, saving, a, g, agents, transactions);

	// write to file
	//string filename = to_string(saving) + "l_" + to_string(m0) + "m";
	agents.save(filename,csv_ascii);

	return 0;
}

void matrixTransactions(int N, int mcc, double saving, double a, double g, mat& agents, int transactions){
	printf("Starting simulation with N=%d, mcc=%d, l=%f, a=%f, g=%f\n",N,mcc,saving,a,g);
	double m0 = agents(0,0);
	mat agentRelations(N,N);
	// RNG
	std::random_device rd;
	std::mt19937_64 gen(rd());
	std::uniform_real_distribution<double> rand(0.0,1.0);

	// progress bar
	cout << "0" << "%             100" << "%" << endl;

	// 'montecarlo loop' 
	for (int i = 1; i < mcc; ++i){
		agents.col(i) = agents.col(i-1);
		// perform transactions
		double j = 0;
		double p;
		while (j < transactions){
			int k = (int)(N*rand(gen));
			int l = (int)(N*rand(gen));
			if(k == l){continue;}
			if(agents(k,i) == agents(l,i)){p = 1.0;}
			else{p = 2*pow(fabs((agents(k,i)-agents(l,i))/m0),-a)*(pow((agentRelations(k,l)+1),g));}
			if(rand(gen) < p ){
				double eps = rand(gen);
				double dm = (1-saving)*(eps*agents(l,i)-(1-eps)*agents(k,i));
				agents(k,i) += dm;
				agents(l,i) -= dm;
				agentRelations(k,l)++;
				agentRelations(l,k)++;
				j++;
			}
		}
		if(i%(int(mcc/20.0)) == 0){cout<<"="<<std::flush;}
	} cout << endl;
}