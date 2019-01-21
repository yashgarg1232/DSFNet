class DatasetNotSelected(Exception):
    def __init__(self):
        super().__init__("Data set not selected")


class InvalidDataset(Exception):
    def __init__(self):
        super().__init__("Invalid dataset provided.")


class DatasetNotFound(Exception):
    def __init__(self):
        super().__init__("Data set not found.")
