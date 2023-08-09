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

    def _hacky_hash(self, some_string):
        _hash = hashlib.md5(some_string.encode("utf-8")).hexdigest()
        return _hash

    def load_data(
            self,
            search_query: str,
            max_results: Optional[int] = 50,
            search_criterion: Optional[int] = 0,
    ) -> List[Document]:
        """Search for a topic on Arxiv, download the PDFs of the top results locally, then read them.

        Args:
            search_query (str): A topic to search for (e.g. "Artificial Intelligence").
            papers_dir (Optional[str]): Locally directory to store the papers
            max_results (Optional[int]): Maximum number of papers to fetch.

        Returns:
            List[Document]: A list of Document objects.
        """

      

        return arxiv_documents + abstract_documents
