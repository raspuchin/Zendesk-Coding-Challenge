class subcomponent():
    def __init__(self, screenwidth=100):
        self.screenwidth = screenwidth


    def set_display_str(self, disp: str) -> None:
        disp_broken_down = []
        i = 0
        n = len(disp)
        while i + self.screenwidth <= n:
            disp_broken_down.append(disp[i:i + self.screenwidth])
            i += self.screenwidth
        disp_broken_down.append(disp[i:n])
        disp = '\n'.join(disp_broken_down)
        self.value = disp


    def get_display(self) -> str:
        if hasattr(self, 'value'):
            return self.value

        return 'NA' + ' ' * (self.screenwidth - 2)