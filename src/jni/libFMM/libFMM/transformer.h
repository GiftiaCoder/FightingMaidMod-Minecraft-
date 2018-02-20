#pragma once

void MultiplyMatrix(const float m1[4][4], const float m2[4][4], float m[4][4]);

void TransformCoordinate(float(*dstCrd)[3], const float(*srcCrd)[3], float matrix[4][4], unsigned int crdNum);
