from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Interface for ingestors"""

    @classmethod
    def can_ingest(cls, path: Path) -> bool:
        """Check if filetype can be ingested
        :param path: Path to file
        :return: Can file be ingested? True/False
        """
        for ext in cls.allowed_extensions:
            if path.endswith(ext):
                return True
        return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file with quotes
        :param path: Path to file
        :return: List of quotes
        """
        pass
    
    @staticmethod
    @abstractmethod
    def split_text(text: str, clean="") -> List[str]:
        return text.strip(clean).split(" - ")