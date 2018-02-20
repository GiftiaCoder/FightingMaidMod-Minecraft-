#pragma once

#include "Bone.h"
#include "Vertex.h"

#include <map>

class Model
{
public:
	void Render();

private:
	std::map<std::string, Bone *> boneMap;

	std::vector<Bone *> rootBoneList;
	std::vector<Vertex> vertexList;

private:
	void UpdateTransformMatrixs();
	void UpdateVertexs();
};

