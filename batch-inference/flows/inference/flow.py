from metaflow import step
from obproject import ProjectFlow


class BatchInferenceFlow(ProjectFlow):
    """
    A minimal batch inference flow for testing CI/CD deployment.
    """

    @step
    def start(self):
        print("Starting batch inference...")
        self.data = [1, 2, 3, 4, 5]
        self.next(self.process)

    @step
    def process(self):
        print(f"Processing {len(self.data)} items")
        self.results = [x * 2 for x in self.data]
        self.next(self.end)

    @step
    def end(self):
        print(f"Inference complete. Results: {self.results}")


if __name__ == "__main__":
    BatchInferenceFlow()
