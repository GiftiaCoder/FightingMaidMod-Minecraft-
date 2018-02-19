#include "ObjModel.h"
#include "Exception.h"

#include <algorithm>
#include <string>
#include <sstream>

// CObjModel
CObjModel::CObjModel() {}

CObjModel::~CObjModel() {}

void CObjModel::load(std::istream &in) {
	initModule();
	if (in.peek() == EOF) {
		throw EXCEPTION_FILE_CANT_ACCESS(NULL_STR);
	}

	const int BUFF_SIZE = 4 * 1024;
	char *pBuff = new char[BUFF_SIZE];
	
	while (! in.eof()) {
		in.getline(pBuff, BUFF_SIZE);
		
		std::stringstream line(pBuff);
		loadLine(line);
	}
	delete pBuff;
}

void CObjModel::render() {

	for (FaceList::iterator it = fList.begin(); it != fList.end(); ++it) {
		FaceInfo &info = *it;
		
		glBegin(GL_POLYGON);
		//int j = 0;
		for (FaceInfo::iterator i = info.begin(); i != info.end(); ++i) {
			stVertexInfo &inf = *i;

			//glTexCoord2fv((GLfloat *) &vtList[inf.vtIdx]);
			glNormal3fv((GLfloat *) &vnList[inf.vnIdx]);
			glVertex3fv((GLfloat *) &vList[inf.vIdx]);
		}
		glEnd();
	}
}

void CObjModel::loadLine(std::stringstream &in) {
	std::string head;
	in >> head;

	std::transform(head.begin(), head.end(), head.begin(), ::tolower);

	FunctionMap::const_iterator findIt = funcMap.find(head);
	if (findIt != funcMap.end()) {
		LoadFunction func = findIt->second;
		(this->*func)(in);
	}
}

void CObjModel::loadV(std::stringstream &line) {
	loadCrdToList(line, vList);
}

void CObjModel::loadVt(std::stringstream &line) {
	loadCrdToList(line, vtList);
}

void CObjModel::loadVn(std::stringstream &line) {
	loadCrdToList(line, vnList);
}

void CObjModel::loadF(std::stringstream &line) {
	std::string data;
	
	FaceInfo faceInfo;
	while (! line.eof()) {
		line >> data;
		faceInfo.push_back(stVertexInfo(data));
	}
	fList.push_back(faceInfo);
}

void CObjModel::loadCrdToList(std::stringstream &line, CrdList &list) {
	list.push_back(stCoord3D(line));
}

FunctionMap CObjModel::funcMap;

// stVertexInfo
stVertexInfo::stVertexInfo(std::string &data) {
	for (int i = 0; i < data.length(); ++ i) {
		char ch = data[i];
		if (ch == '/') {
			data[i] = ' ';
		}
	}
	std::stringstream buf(data);
	
	buf >> vIdx;
	buf >> vtIdx;
	buf >> vnIdx;

	-- vIdx;
	-- vtIdx;
	-- vnIdx;
}

// stCoord3D
stCoord3D::stCoord3D(std::stringstream &in) {
	in >> x;
	in >> y;
	in >> z;
	x /= 100;
	y /= -100;
	z /= 100;
}
