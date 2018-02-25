package poi.demo.fmm.entity.renderer;

import java.io.File;

import net.minecraft.client.model.ModelBase;
import net.minecraft.client.model.ModelBiped;
import net.minecraft.client.model.ModelRenderer;
import net.minecraft.client.renderer.GlStateManager;
import net.minecraftforge.fml.relauncher.Side;
import net.minecraftforge.fml.relauncher.SideOnly;

public class ModelHuman extends ModelBiped
{
	static
	{
		System.load(new File("RenderTest.dll").getAbsolutePath());
	}
	
	static class CustomModelRenderer extends ModelRenderer
	{
		private long modelId;
		
		public CustomModelRenderer(ModelBase model, String path) 
		{
			super(model);
			modelId = loadCustomModel(path);
		}
		
		@SideOnly(Side.CLIENT)
	    public void render(float scale)
	    {
			renderWithRotation(scale);
	    }
		
	    @SideOnly(Side.CLIENT)
	    public void renderWithRotation(float scale)
	    {
	        if (!this.isHidden)
	        {
	            if (this.showModel)
	            {
	            	renderCustomModel(rotationPointX * scale, rotationPointY * scale, rotationPointZ * scale, 
	            			rotateAngleX, rotateAngleY, rotateAngleZ, modelId);
	            }
	        }
	    }
	    
	    private native static void renderCustomModel(
	    		float rotationPointX, float rotationPointY, float rotationPointZ, 
	    		float rotateAngleX, float rotateAngleY, float rotateAngleZ, 
	    		long modelId);
	    
	    private native static long loadCustomModel(String path);
	}
	
	public ModelHuman()
	{
		bipedRightLeg = new CustomModelRenderer(this, "spe_body0.model.txt");
		
		bipedHead.showModel = false;
		bipedBody.showModel = false;
		
		bipedHeadwear.showModel = false;
		bipedRightArm.showModel = false;
		bipedLeftArm.showModel = false;
		bipedRightLeg.showModel = true;
		bipedLeftLeg.showModel = false;
	}
}
