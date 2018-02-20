#include "Model.h"

void Model::Render()
{

}

void Model::UpdateTransformMatrixs()
{
	for (std::vector<Bone *>::iterator i = rootBoneList.begin(); i != rootBoneList.end(); ++i)
	{
		Bone *bone = *i;

	}
}

void Model::UpdateVertexs()
{

}
