import pandas

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
            df = pandas.read_csv(path)
            
            for _, row in df.iterrows():
                csv_model.append(QuoteModel(row["body"], row["author"]))
        except:
            raise Exception("Unsupported filetype")
        else:
            return csv_model

            
            