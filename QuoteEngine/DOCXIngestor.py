from typing import List

import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    allowed_extensions = [".docx"]
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        document = docx.Document(path)
        docx_quotes = []
        try:
            for doc in document.paragraphs:
                if doc.text:
                    body, author = cls.split_text(doc.text)
                    docx_quotes.append(QuoteModel(body, author))
        except Exception:
            raise Exception("Unsupported filetype")
        else:
            return docx_quotes

    @staticmethod
    def split_text(text: str) -> List[str]:
        body, author = text.split(" - ")
        return body.strip('"'), author