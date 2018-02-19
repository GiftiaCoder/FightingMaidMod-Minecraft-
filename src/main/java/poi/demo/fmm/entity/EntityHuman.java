package poi.demo.fmm.entity;

import net.minecraft.entity.EntityLiving;
import net.minecraft.entity.ai.EntityAILookIdle;
import net.minecraft.entity.ai.EntityAISwimming;
import net.minecraft.entity.ai.EntityAIWanderAvoidWater;
import net.minecraft.entity.ai.EntityAIWatchClosest;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.world.World;

public class EntityHuman extends EntityLiving
{
	public EntityHuman(World worldIn) 
	{
		super(worldIn);
        setSize(0.8F, 1.6F);
	}

	protected void initEntityAI()
	{
		//this.tasks.addTask(0, new EntityAISwimming(this));
		//this.tasks.addTask(7, new EntityAIWatchClosest(this, EntityPlayer.class, 6.0F));
		//this.tasks.addTask(8, new EntityAILookIdle(this));
	}
}
