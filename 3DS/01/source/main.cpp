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
	cout << "Day 1:" << endl << endl;

	Result rc = romfsInit();
	if (rc)
	{
		cerr << "Error initializing ROMfs. Error code: 0x" << hex << rc << "." << endl;
	}
	else
	{
		cout << "Part one: " << one() << endl;
		cout << "Part two: " << two() << endl;
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
