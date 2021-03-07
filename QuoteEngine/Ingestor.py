from abc import ABC, abstractmethod
from typing import List

from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.DOCXIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface


class Ingestor(IngestorInterface):
    # class attribute
    INGESTORS = (CSVIngestor, TextIngestor, PDFIngestor, DocxIngestor)
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.INGESTORS:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError("Unsupported filetype")