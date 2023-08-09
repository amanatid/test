"""Read Arxiv Papers."""
import hashlib
import logging
import os
from typing import List, Optional, Tuple

from llama_index import download_loader
from llama_index.readers.base import BaseReader
from llama_index.readers.schema.base import Document
from fpdf import FPDF
#################
from llama_index import SimpleDirectoryReader
#################
from deta import Deta

class ArxivReader_mod(BaseReader):
    """Arxiv Reader.

    Gets a search query, return a list of Documents of the top corresponding scientific papers on Arxiv.
    """

    def __init__(
            self,
    ):
        """Initialize with parameters."""
        super().__init__()
