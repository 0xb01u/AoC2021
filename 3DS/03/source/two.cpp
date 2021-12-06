#include <stdlib.h>
#include <3ds.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include "utils.h"

using namespace std;

int two()
{
	auto diagnosis = readlines("romfs:/input.txt");

	int bitlen = diagnosis[0].length();
	set<string> candidates(diagnosis.begin(), diagnosis.end());

	int oxygen = 0;
	for (int i = 0; i < bitlen; i++)
	{
		int bit = 0;
		for (auto line : candidates)
		{
			bit += line[i] == '1' ? 1 : -1;
		}
		int mcb = bit < 0 ? 0 : 1;
		oxygen <<= 1;
		oxygen |= mcb;

		set<string> candidates_cpy(candidates);
		for (auto candidate : candidates_cpy)
		{
			if (candidate[i] != mcb + '0')
			{
				candidates.erase(candidate);
			}
		}
	}

	int CO2 = 0;
	candidates = set<string>(diagnosis.begin(), diagnosis.end());

	for (int i = 0; i < bitlen; i++)
	{
		int bit = 0;
		for (auto line : candidates)
		{
			bit += line[i] == '1' ? 1 : -1;
		}
		int lcb = bit < 0 ? 1 : 0;
		CO2 <<= 1;
		CO2 |= lcb;

		set<string> candidates_cpy(candidates);
		for (auto candidate : candidates_cpy)
		{
			if (candidate[i] != lcb + '0')
			{
				candidates.erase(candidate);

				if (candidates.size() == 1)
				{
					for (int j = i + 1; j < bitlen; j++)
					{
						CO2 <<= 1;
						CO2 |= ((*candidates.begin())[j] - '0');
					}

					return oxygen * CO2;
				}
			}
		}
	}

	return -1;
}
