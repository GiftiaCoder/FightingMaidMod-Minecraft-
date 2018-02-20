#pragma once

#include "Vertex.h"

struct Mesh
{
	typedef vec3<Vertex *> Triangle;
	std::vector<Triangle> triangleList;
};

