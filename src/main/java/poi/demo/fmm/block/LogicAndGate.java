package poi.demo.fmm.block;

import net.minecraft.block.Block;
import net.minecraft.block.BlockHorizontal;
import net.minecraft.block.material.Material;
import net.minecraft.block.state.IBlockState;
import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.util.EnumFacing;
import net.minecraft.util.math.BlockPos;
import net.minecraft.world.World;
import poi.demo.fmm.R;

public class LogicAndGate extends BlockHorizontal
{
	public LogicAndGate() 
	{
		super(Material.ROCK);
		
		R.EnumModBlocks.LOGIC_AND_GATE.initName(this);
		
		setCreativeTab(CreativeTabs.REDSTONE);
	}
	
	@Override
	public void neighborChanged(IBlockState state, World worldIn, BlockPos pos, Block blockIn, BlockPos fromPos) 
	{
		if (! worldIn.isRemote)
		{
			EnumFacing facing = this.getBedDirection(state, worldIn, fromPos);
			System.out.println(facing);
		}
	}
}
