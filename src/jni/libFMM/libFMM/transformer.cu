
#include "transformer.h"

#include <cuda_runtime.h>
#include <device_functions.h>
#include <device_launch_parameters.h>

__global__ void multiply_matrix(const float m1[4][4], const float m2[4][4], float m[4][4])
{
	__shared__ float assist[4][4][4];
	assist[threadIdx.x][threadIdx.y][threadIdx.z] = m1[threadIdx.z][threadIdx.y] * m2[threadIdx.x][threadIdx.z];

	__syncthreads();
	if (threadIdx.z < 2) assist[threadIdx.x][threadIdx.y][threadIdx.z] += assist[threadIdx.x][threadIdx.y][threadIdx.z + 2];
	__syncthreads();
	if (threadIdx.z < 1) m[threadIdx.x][threadIdx.y] = assist[threadIdx.x][threadIdx.y][0] + assist[threadIdx.x][threadIdx.y][1];
}

void MultiplyMatrix(const float m1[4][4], const float m2[4][4], float m[4][4])
{
	const static dim3 blockSize(4, 4, 4);
	multiply_matrix<<<1, blockSize>>>(m1, m2, m);
}

__global__ void calculate_transform_matrix(float offx, float offy, float offz, float rotx, float roty, float rotz, float matrix[4][4])
{
	
}

__device__ void transform_coordinate(float *dstcrd, const float *srccrd, float matrix[4][4])
{
	__shared__ float assist_matrix[4][4];
	assist_matrix[threadIdx.y][threadIdx.x] = threadIdx.y != 3 ? matrix[threadIdx.y][threadIdx.x] * srccrd[threadIdx.y] : matrix[threadIdx.y][threadIdx.x];
	__syncthreads();
	if (threadIdx.y < 2) assist_matrix[threadIdx.y][threadIdx.x] += assist_matrix[threadIdx.y + 2][threadIdx.x];
	__syncthreads();
	if (threadIdx.y < 1) dstcrd[threadIdx.x] = assist_matrix[0][threadIdx.x] + assist_matrix[1][threadIdx.x];
}

__global__  void transform_coordinate(float (*dstcrd)[3], const float (*srccrd)[3], float matrix[4][4], unsigned int crdnum)
{
	unsigned int crdidx = blockIdx.x;
	while (crdidx < crdnum)
	{
		transform_coordinate(dstcrd[crdidx], srccrd[crdidx], matrix);
		crdidx += gridDim.x;
	}
}

void TransformCoordinate(float (*dstCrd)[3], const float (*srcCrd)[3], float matrix[4][4], unsigned int crdNum)
{
	const static dim3 blockSize(3, 4);
	transform_coordinate << <1, blockSize >> > (dstCrd, srcCrd, matrix, crdNum);
}
