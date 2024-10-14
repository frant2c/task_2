from src.figures.base_figure import BaseFigure


class Engine2D:
    def __init__(self, pen_color="black"):
        self.canvas: list[BaseFigure] = []
        self.__pen_color = pen_color

    def add_figure(self, figure: BaseFigure):
        figure.set_color(self.__pen_color)
        self.canvas.append(figure)

    def switch_color_in_use_to(self, color):
        self.__pen_color = color

    @property
    def color(self):
        return self.__pen_color

    def draw(self):
        for figure in self.canvas:
            figure.draw()
        self.canvas.clear()
