import typing
from .block import Block
from .wall import Wall
from .liquid import Liquid


class Tile:

    def __init__(self, block: typing.Optional[Block], wall: typing.Optional[Wall], liquid: typing.Optional[Liquid]):
        self.block: typing.Optional[Block] = block
        self.wall: typing.Optional[Wall] = wall
        self.liquid: typing.Optional[Liquid] = liquid

    def __repr__(self):
        return f"<Tile {'B' if self.block else '_'}{'W' if self.wall else '_'}{'L' if self.liquid else '_'}>"
