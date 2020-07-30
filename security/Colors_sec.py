import colorama

colorama.init()

class COLORS(colorama.ansi.AnsiFore):
    def __init__(self):
        color = colorama.Fore
        self.CYAN = color.CYAN
        self.GREEN = color.GREEN
        self.LIGHTBLACK_EX = color.LIGHTBLACK_EX
        self.MAGENTA = color.MAGENTA
        self.RED = color.RED
        self.RESET = color.RESET
        self.LIGHTMAGENTA_EX = color.LIGHTMAGENTA_EX
        self.LIGHTYELLOW_EX = color.LIGHTYELLOW_EX
 