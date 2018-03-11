#pragma once

#include "BoneGroup.h"
#include "VertexGroup.h"
#include "MeshGroup.h"

#include "FormatFileReader.h"

class Model
{
public:
	Model(FormatFileReader &rd);

	void Update(void *anima, float time);
	void Render(float rotationPointX, float rotationPointY, float rotationPointZ, float rotateAngleX, float rotateAngleY, float rotateAngleZ);

private:
	BoneGroup m_BoneGroup;
	VertexGroup m_VerttexGroup;
	MeshGroup m_MeshGroup;
};

