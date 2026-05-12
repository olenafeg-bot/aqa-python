
from pathlib import Path
import json
from logger import log_event

base_path = Path(r"C:\Users\Olena.Fehetsyn\PycharmProjects\PythonProject\aqa-python\lesson_15\json_files")
files = [
    base_path / "localizations_en.json",
    base_path / "localizations_ru.json",
    base_path / "login.json",
    base_path / "swagger.json",
]

def valid_json(files):
    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                print(data)
        except json.JSONDecodeError as e:
            print("Incorrect format JSON:", e)
            log_event(file_path.name, f"Invalid JSON: {e}")

if __name__ == "__main__":
    valid_json(files)






