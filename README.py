# Data-Extraction-and-Text-Analysis
"""This project is about extracting relevant textual data from website links and analyzing it across various parameters"""


import pandas as pd
import numpy as np
import os
import nltk
import string
import re
import nltk
from newspaper import Article
from pathlib import Path
from newspaper import Config
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords


