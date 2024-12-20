import argparse

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.cachehierarchies.classic.private_l1_shared_l2_cache_hierarchy import PrivateL1SharedL2CacheHierarchy
from gem5.components.cachehierarchies.ruby.mesi_two_level_cache_hierarchy import (
    MESITwoLevelCacheHierarchy,
)
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA
from gem5.simulate.simulator import Simulator
from gem5.resources.resource import BinaryResource
from gem5.simulate.exit_event import ExitEvent
import m5.stats

parser = argparse.ArgumentParser()
parser.add_argument("ISA", type=str, help="La ISA a testear")
args = parser.parse_args()


#Esto devuelve una funcion
def workbegin_handler():
    print("WORK BEGIN HANDLER")
    m5.stats.dump()
    m5.stats.reset()
    yield False

def workexit_handler():
    print("WORK EXIT HANDLER")
    m5.stats.dump()
    m5.stats.reset()
    yield False

isa = ""
if (args.ISA == "x86"):
    isa = ISA.X86
elif (args.ISA == "r"):
    isa = ISA.RISCV

processor = SimpleProcessor(cpu_type=CPUTypes.TIMING,num_cores=1,isa=isa)
memory = SingleChannelDDR4_2400()
cache = PrivateL1SharedL2CacheHierarchy(l1d_size="64KiB", l1i_size="64KiB", l2_size="1MB")
board = SimpleBoard(processor=processor,memory=memory,cache_hierarchy=cache,clk_freq="3GHz")

binary = None
if (args.ISA == "x86"):
    binary = BinaryResource(local_path="/workspaces/latin-america-2024/exercises/02-Using-gem5/06-custom-benchamarks/matrix-multiply/matrix-multiply")
elif (args.ISA == "r"):
    binary = BinaryResource(local_path="/workspaces/latin-america-2024/exercises/02-Using-gem5/06-custom-benchamarks/matrix-multiply/matrix-multiply-riscv")

board.set_se_binary_workload(binary)
simulator = Simulator(board=board,
                      on_exit_event={
                          ExitEvent.WORKBEGIN:workbegin_handler(),
                          ExitEvent.WORKEND: workexit_handler()
                      })
simulator.run()
