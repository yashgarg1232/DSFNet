from codec.custom_exception import DatasetNotSelected, DatasetNotFound, InvalidDataset
import numpy as np
import os


class VidData:

    # PATH
    _prefix_path = "/Volumes/Yash 750 Ex/2017 - STAR/Results-New"
    _suffix_path = "3P/Features"
    _main_path = ""

    _dataset = ""
    _valid_datasets = ["Weizmann", "KTH", "UCF"]

    _files = []
    _num_files = None

    def __init__(self, dataset="", verbose=0):

        self.is_dataset_valid(dataset)

        self._dataset = dataset
        self._main_path = os.path.join(self._prefix_path, self._dataset, self._suffix_path)

        if not os.path.exists(self._main_path):
            raise DatasetNotFound

        if verbose:
            print("Loading List of available files.")

        self.load_file_list()

    def is_dataset_valid(self, dataset, verbose=0):
        if dataset == "" or not dataset:
            raise DatasetNotSelected

        if verbose:
            print("Dataset selected.")

        if dataset not in self._valid_datasets:
            raise InvalidDataset

        if verbose:
            print("Valid dataset selected.")

    def load_file_list(self):
        self._files = os.listdir(self._main_path)
        self._num_files = int(len(self._files)/2)

    def load_data(self, file_index):
        descriptor_file_index, feature_file_index = self.parse_file_index(file_index)

        descriptor_file_path = os.path.join(self._main_path, self._files[descriptor_file_index])
        feature_file_path = os.path.join(self._main_path, self._files[feature_file_index])
        print(descriptor_file_path)
        print(feature_file_path)

        features = np.loadtxt(feature_file_path, delimiter=',')
        print(features.shape)

        decscriptors = np.loadtxt(descriptor_file_path, delimiter=',')
        print(decscriptors.shape)

    def parse_file_index(self, file_index):
        """
        :param file_index: Infex of the file to read
        :return: returns descriptor and feature index files.
        """
        if self._dataset == self._valid_datasets[0] or self._dataset == self._valid_datasets[1]:
            return ((file_index * 2) - 2), ((file_index * 2) - 1)
        else:
            return (file_index - 1), ((file_index + self._num_files) - 2)
