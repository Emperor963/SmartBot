from discord.ext import commands
import numexpr
import numpy as np
import matplotlib.pyplot as plt
import Equation
from Equation import Expression
from io import BytesIO
import discord
from math import *
import sympy
from sympy import *
from sympy.plotting import *
from sympy.parsing.sympy_parser import *

bot = commands.Bot(command_prefix="!")

@bot.command()
async def math(ctx, *, arg):
    x = numexpr.evaluate(arg)
    await ctx.send(x)

@bot.command()
async def plot(ctx,type, *, eqn):
    if type == 'explicit':
        x = symbols('x')
        eqn = eqn.replace("^", "**")
        transformations = standard_transformations + (implicit_multiplication,)
        eqn2 = parse_expr(eqn, transformations=transformations, evaluate=False)
        plt1 = sympy.plot(eqn2, (x, -10, 10), show=False)
        img = BytesIO()
        plt1.save(img)
        img.seek(0)
        await ctx.send(file=discord.File(img, "graph.png"))
    if type == 'parametric':
        u = symbols('u')
        x_eq, y_eq = eqn.split(", ")
        eqn = eqn.replace("^", "**")
        plt2 = plot_parametric(x_eq, y_eq, (u, -10, 10,100), show=False)
        img = BytesIO()
        plt2.save(img)
        img.seek(0)
        await ctx.send(file=discord.File(img, "graph.png"))
    if type == '3d':
        x, y = symbols('x y')
        eqn = eqn.replace("^", "**")
        plt3 = plot3d(eqn, (x, -10, 10), (y, -10, 10), show=false)
        img = BytesIO()
        plt3.save(img)
        img.seek(0)
        await ctx.send(file=discord.File(img, "graph.png"))




@bot.command()
async def latexfind(ctx, *, eqn):
    fn = Expression(eqn, ['x'])
    await ctx.send(fn)







bot.run("Add Token ID here")

