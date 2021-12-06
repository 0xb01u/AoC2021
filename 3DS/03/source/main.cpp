#include <stdlib.h>
#include <3ds.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int one();
int two();

int main()
{
	gfxInitDefault();
	consoleInit(GFX_TOP, NULL);

	cout << " === ADVENT OF CODE 2021 === " << endl;
	cout << "Day 3:" << endl << endl;

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
		if (_1 != 3959450)
		{
			cout << " >>> PART 1 ERROR <<< " << endl;
		}

		cout << "Part two: " << _2 << endl;
		if (_2 != 7440311)
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
