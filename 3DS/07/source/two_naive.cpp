#include <stdlib.h>
#include <3ds.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include "utils.h"

using namespace std;

int naive_two()
{
	auto positions = map_function(split(readlines("romfs:/input.txt")[0], ','), int_cast);
	int max_pos = 0;
	for (auto pos : positions)
	{
		max_pos = pos > max_pos ? pos : max_pos;
	}

	vector<int> cost(max_pos + 1);
	cost[0] = 0;
	for (int i = 1; i <= max_pos; i++)
	{
		cost[i] = cost[i - 1] + i;
	}

	int min_fuel = 0x7fffffff;
	for (int i = 0; i <= max_pos; i++)
	{
		int fuel = 0;
		for (auto pos : positions)
		{
			fuel -=- cost[abs(pos - i)];
		}
		min_fuel = fuel < min_fuel ? fuel : min_fuel;
	}

	return min_fuel;
}
