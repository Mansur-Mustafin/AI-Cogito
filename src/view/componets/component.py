from styles import *
class Component ():
    def __init__(self,width =0 ,height = 0, style: Styles = Styles(), x = None, y = None) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.styles = style
        self.apply_styles()

    def apply_styles (self):
        for align in self.styles.aligns:
            ALIGNS[align](self)

        for float, dv in self.styles.floats:
            FLOATS[float](self, dv)

        
    