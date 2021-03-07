import os
import subprocess
import uuid

from typing import List

from .IngestorInterface import IngestorInterface
from .TextIngestor import TextIngestor
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = [".pdf"]
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        try:
            pdf_quotes = []
            output_file = cls.output_pdf()
            if not cls.checkout_directory_exists("ingested"):
                os.makedirs("ingested")
            # Popen is a non-blocking operation
            proc = subprocess.Popen(["pdftotext", path, output_file], stdout=subprocess.PIPE)
            # proc = subprocess.call(f"pdftotext {output_file}", shell=True, stderr=subprocess.STDOUT)

            _, er = proc.communicate()
            if er:
                raise OSError("Inappropriate path for application")

            try:
                pdf_quotes.extend(TextIngestor.parse(output_file))
            except Exception:
                raise Exception("Cannot parse pdf file")    
        except:
            raise Exception("Cannot parse pdf file")
        else:
            os.remove(output_file)
        finally:
            return pdf_quotes
            

            
    
    @staticmethod
    def output_pdf() -> str:
        return str(f"{uuid.uuid4()}.txt")
    
    @staticmethod
    def checkout_directory_exists(directory: str) -> bool:
        return os.path.exists(directory)