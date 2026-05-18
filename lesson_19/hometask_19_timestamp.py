
import logging
from datetime import datetime

#Logger
logging.basicConfig(
    filename="hb_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

KEY = "TSTFEED0300|7E3E|0400"


def extract_timestamp(line):

    start_index = line.find("Timestamp ")

    time_str = line[start_index + 10:start_index + 18]
    return datetime.strptime(time_str, "%H:%M:%S")


def filter_log(file_path):

    filtered_log = []

    with open(file_path, "r") as f:
        for line in f:
            if KEY in line:
                filtered_log.append(line)

    return filtered_log


def analyze_heartbeat(lines):

    timestamps = []


    for line in lines:
        ts = extract_timestamp(line)
        if ts:
            timestamps.append(ts)


    for i in range(1, len(timestamps)):
        current = timestamps[i]
        previous = timestamps[i - 1]

        difference = abs((current - previous).total_seconds())

        if 31 < difference < 33:
            logging.warning(f"WARNING: Heartbeat {difference} sec at {current.time()}")
        elif difference >= 33:
            logging.error(f"ERROR: Heartbeat {difference} sec at {current.time()}")



if __name__ == "__main__":
    log_file = "hblog.txt"

    filtered = filter_log(log_file)
    analyze_heartbeat(filtered)
