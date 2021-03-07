import csv

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    # class attribute
    allowed_extensions = [".csv"]
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        try:
            csv_model = []
            with open(path, "r") as infile:
                reader = csv.DictReader(infile)
                for elem in reader:
                    csv_model.append(QuoteModel(elem.get("body"), elem.get("author")))
        except:
            raise Exception("Unsupported filetype")
        else:
            return csv_model

            
            