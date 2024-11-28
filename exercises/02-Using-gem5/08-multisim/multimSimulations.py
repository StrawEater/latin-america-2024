from m5.objects import RiscvO3CPU
from gem5.components.processors.base_cpu_core import BaseCPUCore
from gem5.components.processors.base_cpu_processor import BaseCPUProcessor
from gem5.isas import ISA
from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import obtain_resource
from gem5.isas import ISA
from gem5.simulate.simulator import Simulator
import gem5.utils.multisim as multisim

class BigO3(RiscvO3CPU):
    def __init__(self):
        super().__init__()
        self.fetchWidth = 8
        self.decodeWidth = 8
        self.renameWidth = 8
        self.issueWidth = 8
        self.wbWidth = 8
        self.commitWidth = 8
        self.numROBEntries = 256
        self.numPhysIntRegs = 512
        self.numPhysFloatRegs = 512

class LittleO3(RiscvO3CPU):
    def __init__(self):
        super().__init__()
        self.fetchWidth = 2
        self.decodeWidth = 2
        self.renameWidth = 2
        self.issueWidth = 2
        self.wbWidth = 2
        self.commitWidth = 2
        self.numROBEntries = 30
        self.numPhysIntRegs = 40
        self.numPhysFloatRegs = 40

class BigCore(BaseCPUCore):
    def __init__(self):
        super().__init__(BigO3(), ISA.RISCV)

class LittleCore(BaseCPUCore):
    def __init__(self):
        super().__init__(LittleO3(), ISA.RISCV)

class BigProcessor(BaseCPUProcessor):
    def __init__(self):
        super().__init__([BigCore()])

    @classmethod
    def get_name(self):
        return "BIG-PROCESSOR"

class LittleProcessor(BaseCPUProcessor):
    def __init__(self):
        super().__init__([LittleCore()])

    @classmethod
    def get_name(self):
        return "little-processor"

multisim.set_num_processes(2)
for typeProcessor in [LittleProcessor, BigProcessor]:
    for benchmark in obtain_resource("riscv-getting-started-benchmark-suite"):
        processor = typeProcessor()
        memory = SingleChannelDDR4_2400("1GiB")
        cache = PrivateL1CacheHierarchy(l1d_size="32KiB", l1i_size="32KiB")
        board = SimpleBoard(processor=processor,memory=memory,cache_hierarchy=cache,clk_freq="3GHz")

        board.set_workload(benchmark)
        simulator = Simulator(board=board, id=f"{typeProcessor.get_name()}-{benchmark.get_id()}")
        multisim.add_simulator(simulator)

