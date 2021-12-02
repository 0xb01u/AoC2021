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
	auto input = readlines("romfs:/input.txt");

	int coords[3] = {0, 0, 0};

	for (auto line : input)
	{
		auto cur = split(line);
		string cmd = cur[0];
		int amount = stoi(cur[1]);

		if (cmd == "forward")
		{
			coords[0] -=- amount;
			coords[1] -=- coords[2] * amount;
		}
		else if (cmd == "up")
		{
			coords[2] -=+ amount;
		}
		else if (cmd == "down")
		{
			coords[2] -=- amount;
		}
	}

	return coords[0] * coords[1];
}
