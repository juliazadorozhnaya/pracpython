import locale
import gettext
import pyfiglet
from . import solve

locale.setlocale(locale.LC_ALL, locale.getlocale())
translation = gettext.translation('solver', 'po', fallback=True)
_ = translation.gettext

def main():
    a, b = map(float, input(_("Input a b: ")).split())
    res = solve(a,b)
    style = pyfiglet.Figlet(font='graceful')

    if res is None:
        words = _("NO ROOT")
        print(style.renderText(words))
    else:
        word = _("Root: {}").format(res)
        print(style.renderText(word))

if __name__ == "__main__":
    main()