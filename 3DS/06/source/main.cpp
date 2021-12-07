#include <stdlib.h>
#include <3ds.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stdint.h>

using namespace std;

uint64_t solve(int days);
#define one() solve(80)
#define two() solve(256)

int main()
{
	gfxInitDefault();
	consoleInit(GFX_TOP, NULL);

	cout << " === ADVENT OF CODE 2021 === " << endl;
	cout << "Day 6:" << endl << endl;

	Result rc = romfsInit();
	if (rc)
	{
		cerr << "Error initializing ROMfs. Error code: 0x" << hex << rc << "." << endl;
	}
	else
	{
		uint64_t _1 = one();
		uint64_t _2 = two();

		cout << "Part one: " << _1 << endl;
		if (_1 != 359999)
		{
			cout << " >>> PART 1 ERROR <<< " << endl;
		}

		cout << "Part two: " << _2 << endl;
		if (_2 != 1631647919273)
		{
			cout << " >>> PART 2 ERROR <<< " << endl;
		}
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
