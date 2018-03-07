#include "BoneGroup.h"

void BoneGroup::Bone::Load(FormatFileReader &rd)
{
	rd.ReadStr(name);
	rd.Read((float *)matrix, 16);
}

BoneGroup::BoneGroup(FormatFileReader &rd)
{
	rd.Read(&m_BoneNum);
	m_BoneList = new Bone[m_BoneNum];
	
	for (int i = 0; i < m_BoneNum; ++i)
	{
		m_BoneList[i].Load(rd);
		(*this)[m_BoneList[i].GetName()] = m_BoneList + i;
	}
}

BoneGroup::~BoneGroup()
{
	delete[] m_BoneList;
}
