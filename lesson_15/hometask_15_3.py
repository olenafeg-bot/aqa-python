import xmltodict
import logging
from pathlib import Path

# логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

xml_path = Path(__file__).parent / "xml_file" / "groups.xml"

with open(xml_path, "r") as f:
    data = xmltodict.parse(f.read())

def get_incoming_by_number(data, target_number):
    groups = data.get("groups", {}).get("group", [])

    if isinstance(groups, dict):
        groups = [groups]

    for group in groups:
        number = group.get("number")

        if number == target_number:
            timing = group.get("timingExbytes")

            if timing:
                return timing.get("incoming")
            else:
                return "timingExbytes not found"

    return None


target_number = "4"

result = get_incoming_by_number(data, target_number)

if result is None:
    logging.info(f"Number {target_number} not found")
elif result == "timingExbytes not found":
    logging.info(f"Number {target_number} found, but no incoming value")
else:
    logging.info(f"Incoming for number {target_number}: {result}")
