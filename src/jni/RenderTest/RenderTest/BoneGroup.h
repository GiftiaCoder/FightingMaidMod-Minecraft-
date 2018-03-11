#pragma once

#include "FormatFileReader.h"

#include <vector>
#include <unordered_map>

class Bone
{
public:
	void Load(FormatFileReader &rd);
	void Transform(float(&s)[3], float(&d)[3]);

public:
	float* GetMatrix();
	std::string &GetName();

private:
	std::string name;
	float matrix[16];
};

class BoneGroup : public std::unordered_map<std::string, Bone *>
{
public:
	BoneGroup(FormatFileReader &rd);
	~BoneGroup();

	void Update(void *anima, float time);

	void Transforma(float(&s)[3], float(&d)[3], int idx);

private:
	int m_BoneNum;
	Bone *m_BoneList;
};

