from typing import Optional

import pygame

from .controller import Controller, Command


class GameController(Controller):

    def __init__(self, state, view):
        super().__init__(state, view)

    def handle_event(self) -> Optional[Command]:
        """
        Handles users events while in game such as quitting and key pressing
        :return: a command to be executed or None if the game is yet to end
        :rtype: Optional[Command]
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
                return Command.EXIT

            elif event.type == pygame.KEYDOWN:
                self.__handle_keydown(event.key)
                if self.state.is_win_condition():
                    print("END GAME")
                    return Command.CHANGE_MAIN
                return None

    def __handle_keydown(self, key: any) -> None:
        """
        Handles the key pressing, moves the player depending on the pressed key
        :param key: the key that has been pressed
        :type key: Any
        :return: None
        """
        if key in self.KEY_DIRECTIONS:
            self.state.process_move(self.KEY_DIRECTIONS[key])
