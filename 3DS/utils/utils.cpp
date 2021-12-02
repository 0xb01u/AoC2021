#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <string.h>
#include "utils.h"

using namespace std;

vector<string> readlines(string path)
{
	vector<string> res;

	ifstream input(path);
	
	for (string line; getline(input, line);)
	{
		if (line[line.length() - 1] == '\r') line.pop_back();
		if (line != "") res.push_back(line);
	}

	input.close();

	return res;
}

int int_cast(string n)
{
	return stoi(n);
}

double float_cast(string n)
{
	return stof(n);
}

vector<string> split(string str, char del, int *len)
{
	vector<string> res;

	//  Get amount of substrings:
	int n_substr = 1;
	for (unsigned int i = 0; i < str.length(); i++)
	{
		if (str[i] == del) n_substr++;
	}

	// Create substrings.
	int cur_substr = 0;
	int last_start_index = 0;
	unsigned int i;
	for (i = 0; i <= str.length(); i++)
	{
		if (i == str.length() || str[i] == del)
		{
			res.push_back(str.substr(last_start_index, i - last_start_index));
			last_start_index = i + 1;
			cur_substr++;
		}
	}

	if (len != nullptr)
	{
		*len = n_substr;
	}

	return res;
}
