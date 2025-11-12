from metaflow import FlowSpec, step
from obproject import ProjectFlow

class DataFlow(ProjectFlow):
    @step
    def start(self):
        print("Processing data")
        self.next(self.end)

    @step
    def end(self):
        print("Done")

if __name__ == '__main__':
    DataFlow()