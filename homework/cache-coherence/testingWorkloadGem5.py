
from gem5.simulate.simulator import Simulator
from workloads.array_sum_workload import (
    NaiveArraySumWorkload,
    
    )
from components.boards import HWX86Board
from components.cache_hierarchies import HWMESITwoLevelCacheHierarchy
from components.memories import HWDDR4
from components.network import L1L2ClusterTree
from components.processors import HWO3CPU


processor = HWO3CPU(7)
memory = HWDDR4()
cache = HWMESITwoLevelCacheHierarchy(1)

board = HWX86Board(processor=processor,memory=memory,cache_hierarchy=cache,clk_freq="3GHz")
workload = NaiveArraySumWorkload(16384, 7)

board.set_workload(workload)
simulator = Simulator(board=board)
simulator.run()
