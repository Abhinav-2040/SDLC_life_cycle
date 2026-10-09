import os
from unittest.mock import patch
os.environ["GROQ_API_KEY"] = "fake-key"
os.environ["GROQ_MODEL"] = "fake-model"

import app

print("App loaded.")
