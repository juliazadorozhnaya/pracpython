from . import solve, fig
import gettext
import os

gettext.install("solve", "po")


a, b = map(float, input(_("Input a b: ")).split())
print(fig(solve(a, b)))