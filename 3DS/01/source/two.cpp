#include <stdlib.h>
#include <3ds.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "utils.h"

using namespace std;

int two()
{
	auto input = map_function(readlines("romfs:/input.txt"), int_cast);

	int cur = input[0] + input[1] + input[2];
	int increases = 0;

	for (uint i = 1; i < input.size() - 2; i++)
	{
		int measurement = input[i] + input[i + 1] + input[i + 2];
		if (cur < measurement) increases++;
		cur = measurement;
	}

	return increases;
}
