#include <stdlib.h>
#include <3ds.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include "utils.h"

using namespace std;

int one()
{
	// Optimized solution using the median as the optimal position.
	auto positions = map_function(split(readlines("romfs:/input.txt")[0], ','), int_cast);

	sort(positions.begin(), positions.end());
	int median = positions[positions.size() / 2];

	int min_fuel = 0;
	for (auto pos : positions)
	{
		min_fuel -=- abs(pos - median);
	}

	return min_fuel;
}
