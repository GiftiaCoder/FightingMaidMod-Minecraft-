#pragma once

#include "FormatFileReader.h"

#include <vector>
#include <unordered_map>

class BoneGroup : public std::unordered_map<std::string, BoneGroup::Bone *>
{
private:
	class Bone
	{
	public:
		void Load(FormatFileReader &rd);

	public:
		float **GetMatrix();
		std::string &GetName();

	private:
		std::string name;
		float matrix[4][4];
	};

public:
	BoneGroup(FormatFileReader &rd);
	~BoneGroup();

private:
	int m_BoneNum;
	Bone *m_BoneList;
};

