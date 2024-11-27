
from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.cachehierarchies.ruby.mesi_two_level_cache_hierarchy import (
    MESITwoLevelCacheHierarchy,
)
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA
from gem5.simulate.simulator import Simulator
from workloads.array_sum_workload import NaiveArraySumWorkload

processor = SimpleProcessor(cpu_type=CPUTypes.TIMING,num_cores=1,isa=ISA.X86)
memory = SingleChannelDDR4_2400("1GiB")
cache = MESITwoLevelCacheHierarchy(l1i_size="32KiB", l1i_assoc=8, l1d_size="32KiB", l1d_assoc=8, l2_size="512KiB", l2_assoc=16, num_l2_banks=1)

board = SimpleBoard(processor=processor,memory=memory,cache_hierarchy=cache,clk_freq="3GHz")
workload = NaiveArraySumWorkload(16384, 4)

board.set_workload(workload)
simulator = Simulator(board=board)
simulator.run()
