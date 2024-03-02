from .styles import *
from .theme import *
from .component import Component
from settings import *
import pygame

buttonStyle = Styles(
    {
        STYLES.BACKGROUND : WHITE_COLOR,
        STYLES.TEXT_COLOR : BLUE_COLOR,
        STYLES.FONT_SIZE: 13,
        STYLES.BORDER : 60
    }
)

quitButtonStyle = Styles(
    {
        STYLES.BACKGROUND : BACKGROUND_COLOR,
        STYLES.TEXT_COLOR : RED_COLOR,
        STYLES.FONT_SIZE: 13,
        STYLES.BORDER : 20
    }
)

buttonComponent = lambda : Component( 250, 50, buttonStyle)

quitButtonStyle = Component( 250, 50, quitButtonStyle)

def draw_button(button,screen, mouse_pos: tuple[int, int], x_pos: int | None, y_pos: int | None ):


    if x_pos is not None:
            button.component.x = x_pos
            button.component.y = y_pos

    button.component.draw(screen)
    component: Component = button.component
    style: Styles = button.component.styles

    # invert colors if mouse is over the button
    button_color = style.textColor if button.is_over(mouse_pos) else style.background
    text_color = style.background if button.is_over(mouse_pos) else style.textColor

    # Draw the button rectangle
    rect = pygame.Rect(component.x, component.y, component.width, component.height)
    pygame.draw.rect(screen, button_color, rect, border_radius=style.border)

    # Draw the text on the button
    if button.text != '':
        try:
            font = pygame.font.Font(FONT_PATH, style.fontSize)
        except Exception as e:
            print(f"Error loading font: {e}")
            font = pygame.font.SysFont('Arial', style.fontSize)

        text_surface = font.render(button.text, True, text_color)
        screen.blit(text_surface, (component.x + (component.width- text_surface.get_width()) / 2,
                                    component.y + (component.height - text_surface.get_height()) / 2))
