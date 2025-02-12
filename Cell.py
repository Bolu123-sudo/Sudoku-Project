import pygame

class Cell:
    ## fill in digits with images when style is decided
    digits = {}


    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.sketched = 0
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched = value

    def select(self):
        self.selected = True

    def draw(self):
        if self.value == 0:
            return
        width = self.screen.get_width()
        length = self.screen.get_height()
        cell_w = width / 9
        cell_l = length / 9
        top_left = (self.col*cell_w, self.row*cell_l)
        self.screen.blit(self.digits[self.value], self.digits[self.value].get_rect(topleft=top_left))
        if self.selected:
            color = "red"
        else:
            color = "black"
        pygame.draw.line(self.screen, color=color, start_pos=top_left, end_pos=(top_left[0]+cell_w, top_left[1]))
        pygame.draw.line(self.screen, color=color, start_pos=top_left, end_pos=(top_left[0], top_left[1]+cell_l))
        pygame.draw.line(self.screen, color=color, start_pos=(top_left[0], top_left[1] + cell_l), end_pos=(top_left[0]+cell_w, top_left[1] + cell_l))
        pygame.draw.line(self.screen, color=color, start_pos=(top_left[0]+cell_w,top_left[1]), end_pos=(top_left[0]+cell_w, top_left[1] + cell_l))
