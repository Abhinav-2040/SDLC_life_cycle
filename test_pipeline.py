import os
os.environ["GROQ_API_KEY"] = "fake-key"
os.environ["GROQ_MODEL"] = "fake-model"

from agents.crew_pipeline import run_sdlc_pipeline
print(run_sdlc_pipeline("Create a medical app"))
