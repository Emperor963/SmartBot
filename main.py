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

#Edited to a better code for showing the axes with origin at (0,0)
@bot.command()
async def plot(ctx, *, eqn):
    fn = Expression(eqn, ['x'])
    if 'x' not in fn:  # check 'x' is used in eqn
        print("Error: Equation must have a variable named x")
    ax = plt.axes()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    x = np.linspace(-10, 10, 100)
    plt.plot(x, fn(x))
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    await ctx.send(file=discord.File(img, "graph.png"))
    plt.clf()
    
    
@bot.command()
async def latexfind(ctx, *, eqn):
    fn = Expression(eqn, ['x'])
    await ctx.send(fn)


bot.run("Add token ID here")

