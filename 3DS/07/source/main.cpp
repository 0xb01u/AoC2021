#include <stdlib.h>
#include <3ds.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int one();
int two();
int naive_one();
int naive_two();

int main()
{
	gfxInitDefault();
	consoleInit(GFX_TOP, NULL);

	cout << " === ADVENT OF CODE 2021 === " << endl;
	cout << "Day 7:" << endl << endl;

	Result rc = romfsInit();
	if (rc)
	{
		cerr << "Error initializing ROMfs. Error code: 0x" << hex << rc << "." << endl;
	}
	else
	{
		int _1 = one();
		int _2 = two();

		cout << "Part one: " << _1 << endl;
		if (_1 != 349357)
		{
			cout << " >>> PART 1 ERROR <<< " << endl;
		}

		cout << "Part two: " << _2 << endl;
		if (_2 != 96708205)
		{
			cout << " >>> PART 2 ERROR <<< " << endl;
		}

		#define NAIVE
		#ifdef NAIVE
		cout << endl;

		_1 = naive_one();
		_2 = naive_two();

		cout << "Naive part one: " << _1 << endl;
		if (_1 != 349357)
		{
			cout << " >>> PART 1 ERROR <<< " << endl;
		}

		cout << "Naive part two: " << _2 << endl;
		if (_2 != 96708205)
		{
			cout << " >>> PART 2 ERROR <<< " << endl;
		}
		#endif // NAIVE

		/* Seems like the time measurement doesn't work. What a pity. */
		#ifdef CLOCK_NAIVE
		cout << endl;

		osTimeRef_s begin = osGetTimeRef();
		_1 = naive_one();
		osTimeRef_s middle = osGetTimeRef();
		_2 = naive_two();
		osTimeRef_s end = osGetTimeRef();

		cout << "Naive part one: " << _1;
		printf(" (exec time: %lld ms)\n", middle.value_ms - begin.value_ms);
		if (_1 != 349357)
		{
			cout << " >>> PART 1 ERROR <<< " << endl;
		}

		cout << "Naive part two: " << _2;
		printf(" (exec time: %lld ms)\n", end.value_ms - middle.value_ms);
		if (_2 != 96708205)
		{
			cout << " >>> PART 2 ERROR <<< " << endl;
		}
		#endif // CLOCK_NAIVE
	}

	cout << endl << "Press START to exit." << endl;
	while (aptMainLoop())
	{
		gspWaitForVBlank();
		gfxSwapBuffers();
		hidScanInput();

		u32 kDown = hidKeysDown();

		if (kDown & KEY_START)
			break;
	}

	gfxExit();
	romfsExit();

	return 0;
}
