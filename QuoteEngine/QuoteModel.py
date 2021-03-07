from dataclasses import dataclass

@dataclass
class QuoteModel:
    """ A Quotemodel class """
    body: str
    author: str