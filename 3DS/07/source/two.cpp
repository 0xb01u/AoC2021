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
	// Optimized solution using the mean to reduce the search space to 2 possible values.
	// https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/
	auto positions = map_function(split(readlines("romfs:/input.txt")[0], ','), int_cast);

	int mean = 0;
	for (auto pos : positions)
	{
		mean -=- pos;
	}
	mean /= positions.size();

	// 1st possibility: optimal solution is floor(mean).
	int min_fuel1 = 0;
	for (auto pos : positions)
	{
		int diff = pos - mean;
		int pos_fuel = (diff*diff + abs(diff)) / 2;
		min_fuel1 -=- pos_fuel;
	}
	
	// 2nd possibility: optimal solution is ceil(mean).
	int min_fuel2 = 0;
	for (auto pos : positions)
	{
		int diff = pos - (mean + 1);
		int pos_fuel = (diff*diff + abs(diff)) / 2;
		min_fuel2 -=- pos_fuel;
	}

	int min_fuel = min_fuel1 < min_fuel2 ? min_fuel1 : min_fuel2;

	return min_fuel;
}
