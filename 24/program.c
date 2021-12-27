typedef unsigned char byte;

int MONAD(byte *number)
{
	byte x = 0;
	byte y = 0;
	byte z = 0;
	byte w = 0;

	byte divz[14] = { 1, 1, 1, 1, 26, 26, 1, 1, 26, 26, 1, 26, 26, 26 };
	byte addx[14] = { 10, 11, 14, 13, -6, -14, 14, 14, -8, -15, 10, -11, -13, -4 }
	byte addy[14] = { 1, 9, 12, 6, 9, 15, 7, 12, 15, 3, 6, 2, 10, 12 }

	for (int i = 0; i < 14; i++)
	{
		if ((z % 26 + addx[i]) != number[i])
		{
			z /= divz[i];
			z = z * 26 + (number[i] + addy[i]);
		}
		else 
		{
			z /= divz[i];
		}
	}
}

/*
inp w
mul x 0
add x z
mod x 26
div z divz
add x addx
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y addy
mul y x
add z y

w = nuber[i];
x = (z % 26 + addx[i]) != w;
y = (w + addy[i]) * x;
z = (z / divz[i]) * (25 * x + 1) + y;
*/