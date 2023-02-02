import os

from colorama import Fore

class UI:

	def __init__(self) -> None:
		self.red: str = Fore.RED
		self.reset: str = Fore.RESET
		self.prefix: str = f"[{self.red}ryuk{self.reset}]"

	def clear(self) -> None:
		os.system("cls || clear")