from dataclasses import dataclass


@dataclass
class SeleniumDTO:
    arguments: list = None
    fullscreen: bool = False
