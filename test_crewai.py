try:
    from crewai.llms.base_llm import BaseLLM
    print("BaseLLM imported successfully")
except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"Other error: {e}")
