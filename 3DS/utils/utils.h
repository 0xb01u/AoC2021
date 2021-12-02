#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

vector<string> readlines(string path);

template <class T1, class T2>
vector<T2> map_function(vector<T1> list, T2 (*func)(T1))
{
	vector<T2> res;

	for (T1 e : list)
	{
		res.push_back(func(e));
	}

	return res;
}

int int_cast(string n);
double float_cast(string n);
vector<string> split(string str, char del = ' ', int *len = nullptr);
