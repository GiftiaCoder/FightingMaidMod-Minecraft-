#include "BoneGroup.h"

void Bone::Load(FormatFileReader &rd)
{
	rd.ReadStr(name);
	rd.Read(matrix, sizeof(matrix) / sizeof(*matrix));
	for (int i = 0; i < 16; ++i)
	{
		std::cout << matrix[i] << "\t";
	}
	std::cout << std::endl;
}

void Bone::Transform(float (&s)[3], float(&d)[3])
{
	d[0] = (s[0] * matrix[0]) + (s[1] * matrix[4]) + (s[2] * matrix[8]) + matrix[12];
	d[1] = (s[0] * matrix[1]) + (s[1] * matrix[5]) + (s[2] * matrix[9]) + matrix[13];
	d[2] = (s[0] * matrix[2]) + (s[1] * matrix[6]) + (s[2] * matrix[10]) + matrix[14];
}

float *Bone::GetMatrix()
{
	return matrix;
}

std::string &Bone::GetName()
{
	return name;
}

BoneGroup::BoneGroup(FormatFileReader &rd)
{
	std::string head;
	rd.ReadStr(head);
	std::cout << __FUNCSIG__ << std::endl;
	std::cout << head << std::endl;
	rd.Read(&m_BoneNum);
	std::cout << "bone num: " << m_BoneNum << std::endl;
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

void BoneGroup::Update(void *anima, float time)
{
	// TODO
}

void BoneGroup::Transforma(float (&s)[3], float(&d)[3], int idx)
{
	m_BoneList[idx].Transform(s, d);
}
