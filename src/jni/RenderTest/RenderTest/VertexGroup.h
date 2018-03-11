#pragma once

#include "BoneGroup.h"

#include "FormatFileReader.h"

class VertexGroup
{
public:
	struct Vec3
	{
		float v[3];

		void Zero();
		Vec3 &Plus(Vec3 &vec, float wei);
	};

	struct VertexRealtime
	{
		Vec3 coord;
		Vec3 normal;
		float uv[2];
	};

private:
	struct VertexStatic
	{
		Vec3 coord;
		Vec3 normal;
		float uv[2];

		int bones[4];
		float weight[4];
	};

public:
	VertexGroup(FormatFileReader &rd);
	~VertexGroup();

	void Update(BoneGroup &group);

	int GetVertexNum();
	VertexRealtime *GetVertexData();

private:
	static void UpdateRealtimeVertex(VertexRealtime &r, VertexStatic &s, BoneGroup &bg);

private:
	int m_VertexNum;
	VertexStatic *m_VertexStaticList;
	VertexRealtime *m_VertexRealtimeList;
};

