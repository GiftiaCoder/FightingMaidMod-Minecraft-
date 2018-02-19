package poi.demo.fmm;

import java.io.File;

import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventHandler;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPostInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;
import net.minecraftforge.fml.relauncher.Side;

@Mod(modid = R.MODID, name = R.NAME, version = R.VERSION)
public class FightingMaidMod 
{
	@Mod.Instance(R.MODID)
	public static FightingMaidMod instance;
	
	@EventHandler
	public void pre(FMLPreInitializationEvent event)
	{
		//System.out.println(new File(".").getAbsolutePath());
	}
	
	@EventHandler
	public void init(FMLInitializationEvent event)
	{
		//Blocks.register();
		Entities.register();
		
		if (event.getSide() == Side.CLIENT)
		{
			//Blocks.registerRender();
			Entities.registerRenders();
		}
	}
	
	@EventHandler
	public void post(FMLPostInitializationEvent event)
	{
		
	}
}
