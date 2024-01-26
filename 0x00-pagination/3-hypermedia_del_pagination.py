#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

from typing import Dict, List
import csv


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Returns an indexed dataset
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                pagi: dataset[pagi] for pagi in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing the following key-value pairs:
        index: the current start index of the return page. That is the
        index of the first item in the current page. For example if
        requesting page 3 with page_size 20, and no data was removed
        from the dataset, the current index should be 60.
        """
        focus = []
        dataset = self.indexed_dataset()
        index = 0 if index is None else index
        keys = sorted(dataset.keys())
        assert index >= 0 and index <= keys[-1]
        [focus.append(pagi)
         for pagi in keys if pagi >= index and len(focus) <= page_size]
        data = [dataset[mation] for mation in focus[:-1]]
        next_index = focus[-1] if len(focus) - page_size == 1 else None
        return {'index': index, 'data': data,
                'page_size': len(data), 'next_index': next_index}
