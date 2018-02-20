#pragma once

template<typename T>
union vec2
{
	T v[2];
	struct
	{
		T x, y;
	};
};

template<typename T>
union vec3
{
	T v[3];
	struct
	{
		T x, y, z;
	};
};

template<typename T>
union vec4
{
	T v[4];
	struct
	{
		T x, y, z, w;
	};
};
