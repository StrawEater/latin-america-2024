import argparse


from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from customCPU import BigProcessor, LittleProcessor


parser = argparse.ArgumentParser()
parser.add_argument("CPU", type=str, help="El cpu a testear")
args = parser.parse_args()

cpuType = ""
if args.CPU == "A":
    cpuType = CPUTypes.ATOMIC
elif args.CPU == "T":
    cpuType = CPUTypes.TIMING
elif args.CPU == "M":
    cpuType = CPUTypes.MINOR
elif args.CPU == "O":
    cpuType = CPUTypes.O3

processor = SimpleProcessor(cpu_type=cpuType, num_cores=1, isa=ISA.RISCV)
memory = SingleChannelDDR4_2400()
cache = PrivateL1CacheHierarchy(l1d_size="128KiB", l1i_size="128KiB")

board = SimpleBoard(processor=processor,memory=memory,cache_hierarchy=cache,clk_freq="3GHz")
board.set_workload(obtain_resource("riscv-matrix-multiply-run"))
simulator = Simulator(board=board)
simulator.run()





