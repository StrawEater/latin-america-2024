import argparse

from gem5.components.boards.test_board import TestBoard
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.memory.simple import SingleChannelSimpleMemory
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.memory.multi_channel import ChanneledMemory
from gem5.components.memory.dram_interfaces.lpddr5 import LPDDR5_6400_1x16_BG_BL32
from gem5.components.processors.linear_generator import LinearGenerator
from gem5.components.processors.random_generator import RandomGenerator
from gem5.components.processors.abstract_generator import AbstractGenerator

from gem5.simulate.simulator import Simulator
import math

class HybridGenerator(AbstractGenerator):
    def __init__(
            self,
            cores: int = 2,
            duration: str = "1ms",
            rate: str = "1GB/s",
            block_size: int = 8,
            min_addr: int = 0,
            max_addr: int = 131072,
            rd_perc: int = 100,
            data_limit: int = 0
            ):
        super().__init__(cores)

def get_cant_linear_cores(num_cores: int):
    if (num_cores & (num_cores - 1) == 0):
        return num_cores/2
    else:
        return 2** int(math.log(num_cores,2))


