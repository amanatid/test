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

