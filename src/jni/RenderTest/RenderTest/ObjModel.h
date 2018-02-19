#pragma once

#include "Model.h"

#include <string>
#include <map>
#include <vector>

#include <Windows.h>

#include <gl\GL.h>
#include <gl\GLU.h>

#pragma comment(lib, "opengl32.lib")

class CObjModel;

typedef void (CObjModel::*LoadFunction)(std::stringstream &in);
typedef std::map<std::string, LoadFunction> FunctionMap;

struct stVertexInfo {
	GLuint vIdx;
	GLuint vtIdx;
	GLuint vnIdx;

	stVertexInfo(std::string &data);
};
struct stCoord3D {
	GLfloat x, y, z;

	stCoord3D(std::stringstream &in);
};
typedef std::vector<stVertexInfo> FaceInfo;
typedef std::vector<FaceInfo> FaceList;
//typedef std::vector<GLuint> VertexIndexList;
//typedef std::vector<VertexIndexList> FlatList;
typedef std::vector<stCoord3D> CrdList;

class CObjModel :
	public CModel
{
public:
	CObjModel();

	virtual ~CObjModel();

public:
	virtual void load(std::istream &in) override;

	virtual void render() override;

private:
	void loadLine(std::stringstream &line);

	void loadV(std::stringstream &line);

	void loadVt(std::stringstream &line);

	void loadVn(std::stringstream &line);

	void loadF(std::stringstream &line);

private:
	CrdList vList;
	CrdList vtList;
	CrdList vnList;
	FaceList fList;

private:
	static void loadCrdToList(std::stringstream &line, CrdList &list);

private:
	static FunctionMap funcMap;

public:
	void initModule() {
		CObjModel::funcMap["v"] = &CObjModel::loadV;
		CObjModel::funcMap["vt"] = &CObjModel::loadVt;
		CObjModel::funcMap["vn"] = &CObjModel::loadVn;
		CObjModel::funcMap["f"] = &CObjModel::loadF;
	}
};

