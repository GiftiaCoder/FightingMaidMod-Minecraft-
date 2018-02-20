#pragma once

class CudaRuntime
{
public:
	static void *Malloc(size_t size);
	static void *MallocHost(size_t size);
	static void Free(void *ptr);

public:
	template<typename T>
	static T *Malloc(size_t num)
	{
		return (T *)Malloc(sizeof(T) * num);
	}

	template<typename T>
	static T *MallocHost(size_t num)
	{
		return (T *)MallocHost(sizeof(T) * num);
	}

public:
	enum MemcpyDirection
	{
		DEV2HOST = 0, HOST2DEV, DEV2DEV, HOST2HOST
	};
	static void Memcpy(void *dst, const void *src, size_t size, MemcpyDirection direction);

public:
	static const char *GetLastError();
};

