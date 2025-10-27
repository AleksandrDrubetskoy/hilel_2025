from datetime import datetime


def analyze_heartbeat_log(input_file='hblog.txt', output_file='hb_test.log'):
    key = "TSTFEED0300|7E3E|0400"
    timestamps = []

    # read the log and select lines with the required key
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            if key in line:
                # Find the index Timestamp
                ts_index = line.find("Timestamp ")
                if ts_index != -1:
                    # Extract 8 characters after "Timestamp" → format HH:MM:SS
                    ts_str = line[ts_index + len("Timestamp "):ts_index + len("Timestamp ") + 8]
                    try:
                        time_obj = datetime.strptime(ts_str, "%H:%M:%S")
                        timestamps.append((ts_str, line.strip()))
                    except ValueError:
                        continue

    # Analyzing the time difference between adjacent records
    with open(output_file, 'w', encoding='utf-8') as log_out:
        for i in range(1, len(timestamps)):
            prev_time = datetime.strptime(timestamps[i - 1][0], "%H:%M:%S")
            curr_time = datetime.strptime(timestamps[i][0], "%H:%M:%S")

            # Difference between adjacent marks
            delta = abs((curr_time - prev_time).total_seconds())

            if 31 < delta < 33:
                log_out.write(f"[WARNING] Heartbeat delay {delta:.1f} sec at {timestamps[i][0]} → {timestamps[i][1]}\n")
            elif delta >= 33:
                log_out.write(f"[ERROR] Heartbeat delay {delta:.1f} sec at {timestamps[i][0]} → {timestamps[i][1]}\n")

    print(f"Analysis complete. The results are recorded in {output_file}")


# Launching a function
if __name__ == "__main__":
    analyze_heartbeat_log()