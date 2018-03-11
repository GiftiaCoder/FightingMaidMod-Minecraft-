#include "MeshGroup.h"

#include "GLUtil.h"

void MeshGroup::Mesh::Load(FormatFileReader &rd)
{
	rd.Read(&m_TriangleNum);
	m_TriangleList = new TriangleIdx[m_TriangleNum];
	rd.Read(m_TriangleList, m_TriangleNum);
}

void MeshGroup::Mesh::Render(VertexGroup::VertexRealtime *vrt)
{
	for (int i = 0; i < m_TriangleNum; ++i)
	{
		TriangleIdx &ti = m_TriangleList[i];
		glNormal3fv(vrt[ti.v[0]].normal.v);
		glVertex3fv(vrt[ti.v[0]].coord.v);
		glNormal3fv(vrt[ti.v[1]].normal.v);
		glVertex3fv(vrt[ti.v[1]].coord.v);
		glNormal3fv(vrt[ti.v[2]].normal.v);
		glVertex3fv(vrt[ti.v[2]].coord.v);
	}
}

MeshGroup::MeshGroup(FormatFileReader &rd)
{
	std::string head;
	rd.ReadStr(head);
	std::cout << __FUNCSIG__ << std::endl;
	std::cout << head << std::endl;
	rd.Read(&m_MeshNum);
	std::cout << "mesh num: " << m_MeshNum << std::endl;
	m_MeshList = new Mesh[m_MeshNum];
	for (int i = 0; i < m_MeshNum; ++i)
	{
		m_MeshList[i].Load(rd);
	}
}

MeshGroup::~MeshGroup()
{
	delete[] m_MeshList;
}

void MeshGroup::Render(VertexGroup &vg)
{
	VertexGroup::VertexRealtime *vertexRealtime = vg.GetVertexData();

	glBindTexture(GL_TEXTURE_2D, 0);
	glBegin(GL_TRIANGLES);
	for (int i = 0; i < m_MeshNum; ++i)
	{
		m_MeshList[i].Render(vertexRealtime);
	}
	glEnd();
}
