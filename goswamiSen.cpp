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

void writeArraysToFile(mat, string[], int, int);
void matrixTransactions(int, int, int, double, mat&);

int main(int argc, char const *argv[])
{
	// "Initial conditions"
	int N = 500;
	int transactions = int(pow(10,7));
	int mcc = 100;
	double saving = atof(argv[1]);
	double m0 = atof(argv[2]);
	double a = 0;
	string filename = argv[3];

	// other declerations
	mat agents(N,mcc);
	mat agentsAvg(N,mcc);
	agents.col(0) = m0*ones<vec>(N);

	matrixTransactions(N, mcc, transactions, saving, agents);

	// write to file
	//string filename = to_string(saving) + "l_" + to_string(m0) + "m";
	agents.save(filename,csv_ascii);

	return 0;
}

void matrixTransactions(int N, int mcc, int transactions, double saving, mat& agents){
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
		while (j < transactions){
			int k = (int)(N*rand(gen));
			int l = (int)(N*rand(gen));
			if(k == l){continue;}
			if(rand(gen) < 2*pow(fabs((agents(k)-agents(l))/double(m0)),-alpha)*(pow((c(k,l)+1)/(maxTransactions+1),gamma)) ){
				;
			}
			double eps = rand(gen);
			double dm = (1-saving)*(eps*agents(l,i)-(1-eps)*agents(k,i));
			agents(k,i) += dm;
			agents(l,i) -= dm;
			j++;
		}
		if(i%(int(mcc/20.0)) == 0){cout<<"="<<std::flush;}
	} cout << endl;
}