#include "VertexGroup.h"

#include <iostream>

void VertexGroup::Vec3::Zero()
{
	v[0] = 0;
	v[1] = 0;
	v[2] = 0;
}

VertexGroup::Vec3 &VertexGroup::Vec3::Plus(Vec3 &vec, float wei)
{
	v[0] += vec.v[0] * wei;
	v[1] += vec.v[1] * wei;
	v[2] += vec.v[2] * wei;
	return *this;
}

VertexGroup::VertexGroup(FormatFileReader &rd)
{
	std::string head;
	rd.ReadStr(head);
	std::cout << __FUNCSIG__ << std::endl;
	std::cout << head << std::endl;
	rd.Read(&m_VertexNum);
	std::cout << "vertex num: " << m_VertexNum << std::endl;
	m_VertexStaticList = new VertexStatic[m_VertexNum];
	m_VertexRealtimeList = new VertexRealtime[m_VertexNum];

	rd.Read(m_VertexStaticList, m_VertexNum);
	for (int i = 0; i < m_VertexNum; ++i)
	{
		m_VertexRealtimeList[i] = *(VertexRealtime *)(m_VertexStaticList + i);
	}
}

VertexGroup::~VertexGroup()
{
	delete[] m_VertexStaticList;
	delete[] m_VertexRealtimeList;
}

void VertexGroup::Update(BoneGroup &group)
{
	for (int i = 0; i < m_VertexNum; ++i)
	{
		UpdateRealtimeVertex(m_VertexRealtimeList[i], m_VertexStaticList[i], group);
	}
}

int VertexGroup::GetVertexNum()
{
	return m_VertexNum;
}

VertexGroup::VertexRealtime *VertexGroup::GetVertexData()
{
	return m_VertexRealtimeList;
}

void VertexGroup::UpdateRealtimeVertex(VertexRealtime &r, VertexStatic &s, BoneGroup &bg)
{
	r.coord.Zero();
	r.normal.Zero();
	Vec3 coord, normal;
	for (int i = 0; i < 4; ++i)
	{
		bg.Transforma(s.coord.v, coord.v, s.bones[i]);
		r.coord.Plus(coord, s.weight[i]);

		bg.Transforma(s.normal.v, normal.v, s.bones[i]);
		r.normal.Plus(normal, s.weight[i]);
	}
}
