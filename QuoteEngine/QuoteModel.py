from dataclasses import dataclass

@dataclass
class QuoteModel:
    """ A Quotemodel class """
    body: str
    author: str

    def __repr__(self):
        return f"QuoteModel: '{self.body}' - {self.author}"