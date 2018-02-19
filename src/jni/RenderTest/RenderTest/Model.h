#pragma once

#include <iostream>

class CModel
{
public:
	CModel();

	virtual ~CModel();

public:
	virtual void load(std::string &path);

	virtual void load(std::istream &in) = 0;

	virtual void render() = 0;
};

