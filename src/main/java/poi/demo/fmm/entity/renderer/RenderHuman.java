package poi.demo.fmm.entity.renderer;

import java.io.File;

import net.minecraft.client.renderer.entity.RenderLivingBase;
import net.minecraft.client.renderer.entity.RenderManager;
import net.minecraft.entity.EntityLiving;
import net.minecraft.util.ResourceLocation;

public class RenderHuman extends RenderLivingBase<EntityLiving>
{	
	private static final ResourceLocation TEXTURE = new ResourceLocation("minecraft", "textures/entity/minecart.png");
	
	public RenderHuman(RenderManager renderManagerIn) 
	{
		super(renderManagerIn, new ModelHuman(), 0.6f);
	}

	@Override
	protected ResourceLocation getEntityTexture(EntityLiving entity)
	{
		return TEXTURE;
		//return null;
	}
	
	@Override
	public void doRender(EntityLiving entity, double x, double y, double z, float entityYaw, float partialTicks) 
	{
		super.doRender(entity, x, y, z, entityYaw, partialTicks);
	}
}
