
#include "cuArray.h"

#include "transformer.h"

#include <iostream>

int main()
{
	cuArray<float[4][4]> m1(1), m2(1), m(1);
	for (int x = 0, i = 0; x < 4; ++x)
	{
		for (int y = 0; y < 4; ++y, ++i)
		{
			m1[0][x][y] = i;
			m2[0][x][y] = i;
		}
	}
	m1.set();
	m2.set();

	MultiplyMatrix(m1.cuda_buff()[0], m2.cuda_buff()[0], m.cuda_buff()[0]);

	m.get();
	for (int x = 0; x < 4; ++x)
	{
		for (int y = 0; y < 4; ++y)
		{
			std::cout << m[0][x][y] << ", ";
		}
		std::cout << std::endl;
	}

	system("pause");
	return 0;
}
