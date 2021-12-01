#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "utils.h"

using namespace std;

vector<string> readlines(string path)
{
	vector<string> res;

	ifstream input(path);
	
	for (string line; getline(input, line);)
	{
		if (line != "") res.push_back(line);
	}

	input.close();

	return res;
}

int int_cast(string a)
{
	return stoi(a);
}

double float_cast(string a)
{
	return stof(a);
}
