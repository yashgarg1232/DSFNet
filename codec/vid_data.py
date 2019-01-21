from codec.custom_exception import DatasetNotSelected, DatasetNotFound, InvalidDataset
import os


class VidData:

    # PATH
    _prefix_path = "/Volumes/Yash 750 Ex/2017 - STAR/Results-New/"
    _suffix_path = "/3P/Features"
    _main_path = ""

    _dataset = ""
    _valid_datasets = ["Weizmann", "KTH", "UCF"]

    def is_dataset_valid(self, dataset):
        if dataset == "" or not dataset:
            raise DatasetNotSelected

        if dataset not in self._valid_datasets:
            raise InvalidDataset

    def __init__(self, dataset=""):
        self.is_dataset_valid(dataset)

        self._dataset = dataset
        self._main_path = os.path.join(self._prefix_path, self._dataset, self._suffix_path)

        if not os.exists(self._main_path):
            raise DatasetNotFound
