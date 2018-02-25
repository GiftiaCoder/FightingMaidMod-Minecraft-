#pragma once

#include <vector>

inline float TransformVertex(const float versrc[3], const float matrix[4])
{
	return versrc[0] * matrix[0] + versrc[1] * matrix[1] + versrc[2] * matrix[2] + matrix[3];
}

void TransformVertex(float verdst[3], const float versrc[3], float matrix[4][4])
{
	for (size_t i = 0; i < 3; ++i)
	{
		verdst[i] = TransformVertex(versrc, matrix[i]);
	}
}
