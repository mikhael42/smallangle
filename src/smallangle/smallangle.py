import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.argument("name")
@click.option("-n", "--number", type=int)
def sin(name, number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


@cmd_group.command()
@click.argument("tan")
@click.option("-n", "--number")
def tan(name, number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()
