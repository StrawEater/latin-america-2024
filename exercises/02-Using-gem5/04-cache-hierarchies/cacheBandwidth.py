import argparse

from gem5.components.boards.test_board import TestBoard
from gem5.components.memory.multi_channel import DualChannelDDR4_2400
from gem5.components.memory.dram_interfaces.ddr4 import DDR4_2400_8x8
from gem5.components.processors.linear_generator import LinearGenerator
from gem5.components.processors.random_generator import RandomGenerator
from gem5.components.cachehierarchies.classic.private_l1_private_l2_cache_hierarchy import PrivateL1PrivateL2CacheHierarchy
from gem5.simulate.simulator import Simulator
from three_level import PrivateL1PrivateL2SharedL3CacheHierarchy

parser = argparse.ArgumentParser()
parser.add_argument("rate", type=str, help="El rate del Generador")

args = parser.parse_args()
generator = RandomGenerator(rate=args.rate, rd_perc=100, num_cores=1, max_addr=16384)
#generator = RandomGenerator(rate=args.rate, rd_perc=100, num_cores=1, max_addr=1_000_000_000)
#generator = RandomGenerator(rate=args.rate, rd_perc=100, num_cores=1, max_addr=32768)


memory = DualChannelDDR4_2400(size="1GiB")

cache = PrivateL1PrivateL2SharedL3CacheHierarchy(l1d_size="32KiB",
                                                 l1i_size="32KiB",
                                                 l2_size="256KiB",
                                                 l3_size="2MiB",)

testBoard = TestBoard(cache_hierarchy=cache,
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




