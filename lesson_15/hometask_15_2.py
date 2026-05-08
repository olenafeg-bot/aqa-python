
from pathlib import Path
import json
from logger import log_event

base_path = Path(r"C:\Users\Olena.Fehetsyn\PycharmProjects\PythonProject\aqa-python\lesson_15\json_files")
file_path1 = base_path / "localizations_en.json"
file_path2 = base_path / "localizations_ru.json"
file_path3 = base_path / "login.json"
file_path4 = base_path / "swagger.json"

for file_path in [file_path1, file_path2, file_path3, file_path4]:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(data)
    except json.JSONDecodeError as e:
        print("Incorrect format JSON:", e)
        log_event(file_path.name, f"Invalid JSON: {e}")








