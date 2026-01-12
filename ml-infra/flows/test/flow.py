from metaflow import step
from obproject import ProjectFlow

# Import shared module from repo root to trigger packaging
import shared_utils

class DataFlow(ProjectFlow):
    @step
    def start(self):
        from shared_utils import get_version
        print(f"Processing data with shared_utils version: {get_version()}")
        self.next(self.end)

    @step
    def end(self):
        print("Done")

if __name__ == '__main__':
    DataFlow()