from discord.ext import commands
import numexpr
import numpy as np
import matplotlib.pyplot as plt
import Equation
from Equation import Expression
from io import BytesIO
import discord
from math import *

bot = commands.Bot(command_prefix="!")

@bot.command()
async def math(ctx, *, arg):
    x = numexpr.evaluate(arg)
    await ctx.send(x)

@bot.command()
async def plot(ctx, *, eqn):
    fn = Expression(eqn, ['x'])
    if 'x' not in fn:  # check 'x' is used in eqn
        print("Error: Equation must have a variable named x")
    x = np.linspace(-10, 10, 100)
    plt.plot(x, fn(x))
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    await ctx.send(file=discord.File(img, "graph.png"))


bot.run("ODM5NTA2MTUwNjA4MzM4OTc0.YJKpBw.XbrE-_ix8AL5_1DdBI18zbxS-_8")

