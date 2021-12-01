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
	auto input = map_function(readlines("romfs:/input.txt"), int_cast);

	int cur = input[0];
	int increases = 0;
	vector<int> first_out(input.begin() + 1, input.end());
	for (auto measurement : first_out)
	{
		if (cur < measurement) increases++;
		cur = measurement;
	}

	return increases;
}
