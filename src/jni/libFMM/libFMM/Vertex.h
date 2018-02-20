#pragma once

#include "vec.h"
#include "Bone.h"

struct Vertex
{
	vec3<float> crd;
	vec3<float> nrl;
	vec3<float> uv;
	
	Bone *bone[4];
	float weight[4];
};

