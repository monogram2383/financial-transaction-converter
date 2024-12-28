from abc import ABC, abstractmethod


class PipelineAbstract(ABC):

    @staticmethod
    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError
