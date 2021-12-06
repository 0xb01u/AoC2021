#include <stdlib.h>
#include <3ds.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "utils.h"

using namespace std;

int one()
{
	auto diagnosis = readlines("romfs:/input.txt");

	int bitlen = diagnosis[0].length();

	int gamma_rate = 0;
	for (int i = 0; i < bitlen; i++)
	{
		int bit = 0;
		for (auto line : diagnosis)
		{
			bit += line[i] == '1' ? 1 : -1;
		}
		gamma_rate <<= 1;
		gamma_rate |= bit < 0 ? 0 : 1;
	}

	int epsilon_rate = (~gamma_rate) & ((1 << bitlen) - 1);
	return gamma_rate * epsilon_rate;
}
