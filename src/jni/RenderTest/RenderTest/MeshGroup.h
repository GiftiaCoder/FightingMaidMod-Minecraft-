#pragma once

#include "BoneGroup.h"
#include "VertexGroup.h"
#include "FormatFileReader.h"

class MeshGroup
{
private:
	struct TriangleIdx
	{
		int v[3];
	};

	class Mesh
	{
	public:
		void Load(FormatFileReader &rd);

		void Render(VertexGroup::VertexRealtime *vrt);

	private:
		int m_TriangleNum;
		TriangleIdx *m_TriangleList;
	};
public:
	MeshGroup(FormatFileReader &rd);
	~MeshGroup();

	void Render(VertexGroup &vg);

private:
	int m_MeshNum;
	Mesh *m_MeshList;
};

