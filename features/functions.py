import json

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
