#include <stdlib.h>
#include <3ds.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include "utils.h"

using namespace std;

int naive_one()
{
	auto positions = map_function(split(readlines("romfs:/input.txt")[0], ','), int_cast);
	int max_pos = 0;
	for (auto pos : positions)
	{
		max_pos = pos > max_pos ? pos : max_pos;
	}

	int min_fuel = 0x7fffffff;
	for (int i = 0; i <= max_pos; i++)
	{
		int fuel = 0;
		for (auto pos : positions)
		{
			fuel -=- abs(pos - i);
		}
		min_fuel = fuel < min_fuel ? fuel : min_fuel;
	}

	return min_fuel;
}
