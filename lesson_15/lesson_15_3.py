
import xml.etree.ElementTree as ET
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

base_path = Path(r"C:\Users\Olena.Fehetsyn\PycharmProjects\PythonProject\aqa-python\lesson_15\xml_file")
xml_path = base_path / "groups.xml"

tree = ET.parse(xml_path)
root = tree.getroot()


def get_incoming_by_number(root, target_number):
    for group in root.findall("group"):
        number = group.findtext("number")

        if number == target_number:
            incoming = group.findtext("timingExbytes/incoming")

            if incoming is not None:
                return incoming
            else:
                return "timingExbytes/incoming not found"

    return None

target_number = "4"

result = get_incoming_by_number(root, target_number)

if result is not None:
    logging.info(f"Incoming for number {target_number}: {result}")
else:
    logging.info(f"Number {target_number} not found")
