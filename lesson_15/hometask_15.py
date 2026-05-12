
from pathlib import Path
import csv

base_path = Path(r"C:\Users\Olena.Fehetsyn\PycharmProjects\PythonProject\aqa-python\lesson_15\csv_report")

csv_files = [
    base_path / "random.csv",
    base_path / "random-michaels.csv"
    ]
output_file = base_path / "result_fehetsyn.csv"


def remove_duplicates(csv_file, output_file):
    rows = []
    header = None
    for file in csv_files:
        with open(file, "r") as f:
            reader = csv.reader(f)
            file_header = next(reader)

            if header is None:
                header = file_header

            for row in reader:
             rows.append(tuple(row))

    unique_rows = set(rows)



    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(unique_rows)

if __name__ == "__main__":
    remove_duplicates(csv_files, output_file)
print("completed successfully")
