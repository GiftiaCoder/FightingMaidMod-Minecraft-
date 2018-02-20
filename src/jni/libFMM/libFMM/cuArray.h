#pragma once

#include "CudaRuntime.h"

template<typename T>
class cuArray
{
private:
	size_t nm, sz;
	T *cb, *hb;

public:
	cuArray(size_t num = 1, bool is_host = true) : 
		cb(CudaRuntime::Malloc<T>(num)), 
		hb(is_host ? CudaRuntime::MallocHost<T>(num) : nullptr), 
		nm(num), 
		sz(num * sizeof(T))
	{
		// TODO
	}

	~cuArray()
	{
		CudaRuntime::Free(cb);
		CudaRuntime::Free(hb);
	}

	inline void get()
	{
		CudaRuntime::Memcpy(hb, cb, sz, CudaRuntime::MemcpyDirection::DEV2HOST);
	}

	inline void set()
	{
		CudaRuntime::Memcpy(cb, hb, sz, CudaRuntime::MemcpyDirection::HOST2DEV);
	}

	inline T& operator[](size_t idx)
	{
		return hb[idx];
	}

	inline T *operator()()
	{
		return cb;
	}

	inline size_t num()
	{
		return nm;
	}

	inline size_t size()
	{
		return sz;
	}

	inline T *cuda_buff()
	{
		return cb;
	}

	inline T *host_buff()
	{
		return hb;
	}
};

