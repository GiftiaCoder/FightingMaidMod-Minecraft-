#include "Model.h"

#include "GLUtil.h"
#include <math.h>

Model::Model(FormatFileReader &rd) : m_BoneGroup(rd), m_VerttexGroup(rd), m_MeshGroup(rd)
{
	// do nothing
}

void Model::Update(void *anima, float time)
{
	m_BoneGroup.Update(anima, time);
	m_VerttexGroup.Update(m_BoneGroup);
}

void Model::Render(float rotationPointX, float rotationPointY, float rotationPointZ, float rotateAngleX, float rotateAngleY, float rotateAngleZ)
{
#define PI (3.1415926)

	glPushMatrix();
	glTranslatef(rotationPointX, rotationPointY, rotationPointZ);
	if (rotateAngleY) glRotatef(rotateAngleY * (180.0F / (float)PI), 0.0F, 1.0F, 0.0F);
	if (rotateAngleX) glRotatef(rotateAngleX * (180.0F / (float)PI), 1.0F, 0.0F, 0.0F);
	if (rotateAngleZ) glRotatef(rotateAngleZ * (180.0F / (float)PI), 0.0F, 0.0F, 1.0F);

	glShadeModel(GL_SMOOTH);

	m_MeshGroup.Render(m_VerttexGroup);

	//glShadeModel(GL_FLAT);

	glPopMatrix();

#undef PI
}
