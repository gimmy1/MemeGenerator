import os
import uuid

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    allowed_extensions = [".txt"]
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        try:
            with open(path, "r", encoding="utf-8-sig") as infile:
                text_quotes = []
                for line in infile.readlines():
                    body, author = cls.split_text(line, clean="\n")
                    if body and author:
                        text_quotes.append(QuoteModel(body, author))
        except:
            raise Exception("Cannot parse text file")
        else:
            return text_quotes
    
    @staticmethod
    def split_text(text: str, clean="") -> List[str]:
        try:
            body, author = text.strip(clean).split(" - ")
        except ValueError:
            print("not enough values to unpack")
            body, author = "", ""
        finally:
            return body, author
        

            
