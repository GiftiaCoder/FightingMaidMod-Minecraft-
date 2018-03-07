#pragma once

#include <iostream>
#include <fstream>

#include <string>

class FormatFileReader
{
public:
	FormatFileReader(std::ifstream &is);

public:
	void ReadStr(std::string &out);

	template<typename T>
	void Read(T *t)
	{
		in.read((char *)t, sizeof(T));
	}

	template<typename T>
	void Read(T *t, int s)
	{
		in.read((char *)t, sizeof(T) * s);
	}

private:
	std::ifstream &in;
};

