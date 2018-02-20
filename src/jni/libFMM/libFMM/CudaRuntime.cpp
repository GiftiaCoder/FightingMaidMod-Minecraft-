#include "CudaRuntime.h"

#include <cuda_runtime.h>
#include <cuda_runtime_api.h>

void *CudaRuntime::Malloc(size_t size)
{
	void *ptr = nullptr;
	::cudaMalloc(&ptr, size);
	return ptr;
}

void *CudaRuntime::MallocHost(size_t size)
{
	void *ptr = nullptr;
	::cudaMallocHost(&ptr, size);
	return ptr;
}

void CudaRuntime::Free(void *ptr)
{
	if (ptr)
	{
		::cudaFree(ptr);
	}
}

void CudaRuntime::Memcpy(void *dst, const void *src, size_t size, MemcpyDirection direction)
{
	const static cudaMemcpyKind KIND_LIST[] = 
	{
		cudaMemcpyDeviceToHost, cudaMemcpyHostToDevice, cudaMemcpyDeviceToDevice, cudaMemcpyHostToHost
	};
	cudaMemcpy(dst, src, size, KIND_LIST[direction]);
}

const char *CudaRuntime::GetLastError()
{
	return cudaGetErrorString(cudaGetLastError());
}
