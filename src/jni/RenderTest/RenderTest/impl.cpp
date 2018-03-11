
#include "Model.h"
#include "FormatFileReader.h"

#include "poi_demo_fmm_entity_renderer_ModelHuman.h"
#include "poi_demo_fmm_entity_renderer_ModelHuman_CustomModelRenderer.h"

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

JNIEXPORT void JNICALL Java_poi_demo_fmm_entity_renderer_ModelHuman_00024CustomModelRenderer_renderCustomModel
(JNIEnv *env, jclass, jfloat rotationPointX, jfloat rotationPointY, jfloat rotationPointZ, jfloat rotateAngleX, jfloat rotateAngleY, jfloat rotateAngleZ, jlong modelId)
{
	((Model *)jlong2ptr(modelId))->Update(nullptr, 0);
	((Model *)jlong2ptr(modelId))->Render(rotationPointX, rotationPointY, rotationPointZ, rotateAngleY, rotateAngleZ, rotateAngleZ);
}

JNIEXPORT jlong JNICALL Java_poi_demo_fmm_entity_renderer_ModelHuman_00024CustomModelRenderer_loadCustomModel
(JNIEnv *env, jclass, jstring path)
{
	const char *model_path = env->GetStringUTFChars(path, false);
	Model *m = new Model(FormatFileReader(model_path));
	env->ReleaseStringUTFChars(path, model_path);
	return ptr2jlong(m);
}
