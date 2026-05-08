
from pathlib import Path
import csv

base_path = Path(r"C:\Users\Olena.Fehetsyn\PycharmProjects\PythonProject\aqa-python\lesson_15\csv_report")

file1 = base_path / "random.csv"
file2 = base_path / "random-michaels.csv"

rows = []
header = None

for file in [file1, file2]:
    with open(file, "r") as f:
        reader = csv.reader(f)
        file_header = next(reader)

        if header is None:
            header = file_header

        for row in reader:
            rows.append(tuple(row))

unique_rows = set(rows)

output_file = base_path / "result_fehetsyn.csv"

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(unique_rows)

print("completed successfully")
