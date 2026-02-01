
from flowweave import FlowWeaveTask, FlowWeaveTaskRunner, Result

class Test(FlowWeaveTaskRunner):
    def __init__(self):
        self.name = str() # set by FlowWeave
        self.global_op = str() # set by FlowWeave
        self.default_op = int() # set by FlowWeave

    def __call__(self):
        self.message(f"called {self.name} - {self.global_op}, {self.default_op}")
        return Result.SUCCESS

class Task(FlowWeaveTask):
    runner = Test
