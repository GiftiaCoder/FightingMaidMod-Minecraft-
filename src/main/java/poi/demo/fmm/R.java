package poi.demo.fmm;

import net.minecraft.block.Block;

public interface R 
{
	public static final String MODID = "fightingmaidmod";
	public static final String NAME = "Fighting Maid Mod";
	public static final String VERSION = "1.0";
	
	public static enum EnumModBlocks
	{
		LOGIC_AND_GATE("logic_and_gate");
		
		private String unlocalizedName;
		private String registryName;
		
		private EnumModBlocks(String name)
		{
			unlocalizedName = name;
			registryName = name;
		}
		
		public void initName(Block block)
		{
			block.setUnlocalizedName(unlocalizedName);
			block.setRegistryName(registryName);
		}
	}
}
