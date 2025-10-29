import json
import logging
from pathlib import Path

# Setting up logging
logging.basicConfig(
    filename="json__Drubetskoy.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File paths
files = [
    "swagger.json",
    "localizations_en.json",
    "localizations_ru.json",
    "login.json"
]


def validate_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json.load(f)
        print(f"{file_path} — valid JSON")
    except json.JSONDecodeError as e:
        logging.error(f"{file_path} — invalid JSON: {e}")
        print(f"{file_path} — error: {e}")
    except Exception as e:
        logging.error(f"{file_path} — error while reading: {e}")
        print(f"{file_path} — error while reading: {e}")


if __name__ == "__main__":
    for file in files:
        if Path(file).exists():
            validate_json(file)
        else:
            logging.error(f"{file} — file not found")
            print(f"{file} — file not found")

