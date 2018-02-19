package poi.demo.fmm;

import net.minecraft.block.Block;
import net.minecraft.block.state.IBlockState;
import net.minecraft.client.Minecraft;
import net.minecraft.client.renderer.block.model.ModelResourceLocation;
import net.minecraft.client.renderer.block.statemap.IStateMapper;
import net.minecraft.client.renderer.block.statemap.StateMapperBase;
import net.minecraft.item.Item;
import net.minecraft.item.ItemBlock;
import net.minecraftforge.fml.common.registry.GameRegistry;
import net.minecraftforge.registries.GameData;

public class Blocks 
{
	public static final IStateMapper STATE_MAPPER = new StateMapperBase() 
	{	
		@Override
		protected ModelResourceLocation getModelResourceLocation(IBlockState state) 
		{
			return new ModelResourceLocation(state.getBlock().getRegistryName(), "inventory");
		}
	};
	
	public static void register()
	{
		// TODO
	}
	
	public static void registerRender()
	{
		// TODO
	}
	
	private static void register(Block block)
	{
		GameData.register_impl(block);
		GameData.register_impl(createItemBlock(block));
	}
	
	private static void registerRender(Block block)
	{
		Minecraft.getMinecraft().getBlockRendererDispatcher().getBlockModelShapes().registerBlockWithStateMapper(block, STATE_MAPPER);
		Minecraft.getMinecraft().getRenderItem().getItemModelMesher().register(Item.getItemFromBlock(block), 0, new ModelResourceLocation(block.getRegistryName(), "inventory"));
	}
	
	private static Item createItemBlock(Block block)
	{
		return new ItemBlock(block).setRegistryName(block.getRegistryName());
	}
}
