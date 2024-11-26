import argparse

from gem5.components.boards.test_board import TestBoard
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.memory.simple import SingleChannelSimpleMemory
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.memory.multi_channel import ChanneledMemory
from gem5.components.memory.dram_interfaces.lpddr5 import LPDDR5_6400_1x16_BG_BL32
from gem5.components.processors.linear_generator import LinearGenerator
from gem5.components.processors.random_generator import RandomGenerator
from gem5.simulate.simulator import Simulator

parser = argparse.ArgumentParser()
parser.add_argument("rate", type=str, help="El rate del Generador")
parser.add_argument("readRatio", type=int, help="El porcentaje de Lectura del Generador")

args = parser.parse_args()

generator = LinearGenerator(rate=args.rate, rd_perc=args.readRatio, num_cores=1)

memory = SingleChannelSimpleMemory(bandwidth="32GiB/s",
                                   latency="20ns",
                                   latency_var="0s",
                                   size="1GiB")

testBoard = TestBoard(cache_hierarchy=NoCache(),
                      memory=memory,
                      generator=generator,
                      clk_freq="3GHz")

simulator = Simulator(board=testBoard)
simulator.run()

statsSim = simulator.get_simstats()
seconds = statsSim.simTicks.value / statsSim.simFreq.value

total_bytes = (
    statsSim.board.processor.cores[0].generator.bytesRead.value
    + statsSim.board.processor.cores[0].generator.bytesWritten.value
)
latency = (
    statsSim.board.processor.cores[0].generator.totalReadLatency.value
    / statsSim.board.processor.cores[0].generator.totalReads.value
)
print(f"Total bandwidth: {total_bytes / seconds / 2**30:0.2f} GiB/s")
print(f"Average latency: {latency / statsSim.simFreq.value * 1e9:0.2f} ns")






