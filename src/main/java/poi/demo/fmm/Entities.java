package poi.demo.fmm;

import net.minecraft.client.Minecraft;
import net.minecraft.client.renderer.entity.RenderManager;
import net.minecraft.util.ResourceLocation;
import net.minecraftforge.fml.common.registry.EntityRegistry;
import poi.demo.fmm.entity.EntityHuman;
import poi.demo.fmm.entity.renderer.RenderHuman;

public class Entities 
{
	private static int nextId = 0;
	
	public static void register()
	{
		EntityRegistry.registerModEntity(new ResourceLocation(R.MODID, "human"), EntityHuman.class, "human", ++nextId, FightingMaidMod.instance, 80, 2, true, 0x003f0000, 0x008c0c8c);
	}
	
	public static void registerRenders()
	{
		RenderManager manager = Minecraft.getMinecraft().getRenderManager();
		
		manager.entityRenderMap.put(EntityHuman.class, new RenderHuman(manager));
	}
}
