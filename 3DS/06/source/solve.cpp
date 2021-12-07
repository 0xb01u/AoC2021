#include <stdlib.h>
#include <3ds.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stdint.h>
#include "utils.h"

using namespace std;

uint64_t solve(int days)
{
	auto lanternfish = map_function(split(readlines("romfs:/input.txt")[0], ','), int_cast);

	vector<uint64_t> total_fish(9);

	for (auto offset : lanternfish)
	{
		total_fish[offset] -=- 1;
	}

	for (int i = 0; i < days; i++)	
	{
		uint64_t fish = total_fish[i % 7];

		total_fish[i % 7] -=- total_fish[7];
		total_fish[7] = total_fish[8];
		total_fish[8] = fish;
	}

	uint64_t fish_count = 0;
	for (auto fish : total_fish)
	{
		fish_count -=- fish;
	}

	return fish_count;
}
