import discord
from discord.ext import commands
from milestone_manager import MilestoneManager
from dispute_resolution import DisputeResolution
from escrow import Escrow
import config

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize modules
milestone_manager = MilestoneManager()
dispute_resolution = DisputeResolution()
escrow = Escrow()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='create_milestone')
async def create_milestone(ctx, *, description):
    """Creates a new milestone."""
    try:
        milestone_manager.create_milestone(description)
        await ctx.send(f'Milestone created: {description}')
    except Exception as e:
        await ctx.send(f'Error creating milestone: {str(e)}')

@bot.command(name='submit_milestones')
async def submit_milestones(ctx):
    """Submits the milestone checklist."""
    try:
        milestone_manager.submit_milestones()
        await ctx.send('Milestones submitted successfully.')
    except Exception as e:
        await ctx.send(f'Error submitting milestones: {str(e)}')

@bot.command(name='complete_milestone')
async def complete_milestone(ctx, *, description):
    """Marks a milestone as completed."""
    try:
        milestone_manager.complete_milestone(description)
        await ctx.send(f'Milestone completed: {description}')
    except Exception as e:
        await ctx.send(f'Error completing milestone: {str(e)}')

@bot.command(name='verify_milestone')
async def verify_milestone(ctx, *, description):
    """Verifies the completion of a milestone."""
    try:
        milestone_manager.verify_milestone(description)
        await ctx.send(f'Milestone verified: {description}')
    except Exception as e:
        await ctx.send(f'Error verifying milestone: {str(e)}')

@bot.command(name='raise_dispute')
async def raise_dispute(ctx, milestone, *, reason):
    """Raises a dispute for a milestone."""
    try:
        dispute_resolution.raise_dispute(milestone, reason)
        await ctx.send(f'Dispute raised for milestone: {milestone} - Reason: {reason}')
    except Exception as e:
        await ctx.send(f'Error raising dispute: {str(e)}')

@bot.command(name='release_escrow')
async def release_escrow(ctx):
    """Releases escrow funds upon milestone completion."""
    try:
        escrow.release_funds()
        await ctx.send('Escrow funds released.')
    except Exception as e:
        await ctx.send(f'Error releasing escrow funds: {str(e)}')

if __name__ == '__main__':
    bot.run(config.BOT_TOKEN)
