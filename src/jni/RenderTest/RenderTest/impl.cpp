
#include "poi_demo_fmm_entity_renderer_ModelHuman.h"
#include "poi_demo_fmm_entity_renderer_ModelHuman_CustomModelRenderer.h"

#include <iostream>
#include <fstream>

#include <Windows.h>
#include <gl\GL.h>
#include <gl\GLU.h>

#include <vector>
#include <string>

#include <math.h>

#pragma comment(lib, "opengl32.lib")

void *jlong2ptr(jlong l)
{
	union
	{
		jlong l;
		void *p;
	}u = { 0 };
	u.l = l;
	return u.p;
}

jlong ptr2jlong(void *p)
{
	union
	{
		jlong l;
		void *p;
	}u = { 0 };
	u.p = p;
	return u.l;
}

template<typename T, size_t s>
struct Vector
{
	T v[s];

	T& operator[] (size_t i)
	{
		return v[i];
	}

	std::iostream &operator >> (std::iostream &in)
	{
		for (size_t i = 0; i < s; ++i)
		{
			in >> v[i];
		}
	}
};

class FileFormatReader
{
public:
	FileFormatReader(const char *path) : in(path, std::ios::binary) {}

public:
	template<typename T>
	void Read(T *v)
	{
		in.read((char *)v, sizeof(*v));
	}

protected:
	std::ifstream in;
};

class Model : public FileFormatReader
{
private:
	std::vector<Vector<float, 3>> vertexs;
	std::vector<Vector<float, 3>> normals;
	std::vector<Vector<int16_t, 3>> meshs;

public:

	Model(const char *path) : FileFormatReader(path)
	{
		uint32_t vertexNum, meshNum;
		in >> vertexNum;
		std::cout << "vertex num: " << vertexNum << std::endl;
		for (uint32_t i = 0; i < vertexNum; ++i)
		{
			Vector<float, 3> v, n;
			in >> v[0];
			in >> v[2];
			in >> v[1];
			v[0] *= 1;
			v[1] *= -1;
			v[2] *= 1;
			vertexs.push_back(v);
			in >> n[0];
			in >> n[2];
			in >> n[1];
			n[0] *= 1;
			n[1] *= -1;
			n[2] *= 1;
			normals.push_back(n);
		}
		in >> meshNum;
		std::cout << "mesh num: " << meshNum << std::endl;
		for (uint32_t i = 0; i < meshNum; ++i)
		{
			uint32_t trgNum;
			in >> trgNum;
			std::cout << "trg num: " << trgNum << std::endl;
			for (uint32_t j = 0; j < trgNum; ++j)
			{
				Vector<int16_t, 3> t;
				for (int k = 0; k < 3; ++k)
				{
					in >> t[k];
				}
				meshs.push_back(t);
			}
		}
		std::cout << "vertex size: " << vertexs.size() << std::endl;
		std::cout << "normal size: " << normals.size() << std::endl;
	}

	void doRender()
	{
		//std::cout << meshs.size() << std::endl;
		//std::cout << vertexs.size() << std::endl;
		//std::cout << normals.size() << std::endl;
		glBindTexture(GL_TEXTURE_2D, 0);
		glEnable(GL_SMOOTH);
		glShadeModel(GL_SMOOTH);
		for (size_t trg = 0; trg < meshs.size(); ++trg)
		{
			glBegin(GL_TRIANGLES);
			Vector<int16_t, 3> &m = meshs[trg];
			glNormal3fv(normals[m[0]].v);
			glVertex3fv(vertexs[m[0]].v);
			glNormal3fv(normals[m[1]].v);
			glVertex3fv(vertexs[m[1]].v);
			glNormal3fv(normals[m[2]].v);
			glVertex3fv(vertexs[m[2]].v);
			glEnd();
		}
	}
};

#define PI (3.1415926)

JNIEXPORT void JNICALL Java_poi_demo_fmm_entity_renderer_ModelHuman_00024CustomModelRenderer_renderCustomModel
(JNIEnv *env, jclass, jfloat rotationPointX, jfloat rotationPointY, jfloat rotationPointZ, jfloat rotateAngleX, jfloat rotateAngleY, jfloat rotateAngleZ, jlong modelId)
{
	glPushMatrix();
	glTranslatef(rotationPointX, rotationPointY, rotationPointZ);
	if (rotateAngleY) glRotatef(rotateAngleY * (180.0F / (float)PI), 0.0F, 1.0F, 0.0F);
	if (rotateAngleX) glRotatef(rotateAngleX * (180.0F / (float)PI), 1.0F, 0.0F, 0.0F);
	if (rotateAngleZ) glRotatef(rotateAngleZ * (180.0F / (float)PI), 0.0F, 0.0F, 1.0F);

	((Model *)jlong2ptr(modelId))->doRender();

	glPopMatrix();
}

JNIEXPORT jlong JNICALL Java_poi_demo_fmm_entity_renderer_ModelHuman_00024CustomModelRenderer_loadCustomModel
(JNIEnv *env, jclass, jstring path)
{
	const char *model_path = env->GetStringUTFChars(path, false);
	Model *m = new Model(model_path);
	//CObjModel *model = new CObjModel();
	std::ifstream in(model_path, std::ios::binary);
	//model->load(in);
	env->ReleaseStringUTFChars(path, model_path);
	//std::cout << "model addr: " << m << std::endl;
	//return ptr2jlong(model);
	return ptr2jlong(m);
}
