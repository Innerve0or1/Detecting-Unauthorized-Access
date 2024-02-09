import win32evtlog

def print_event_logs():
    server = None  # None for local machine, or specify a remote server name
    log_types = ["Application", "System"]  # Specify the event log types you want to retrieve
    
    for log_type in log_types:
        print(f"=== {log_type} Event Log ===")
        hand = win32evtlog.OpenEventLog(server, log_type)
        total_records = win32evtlog.GetNumberOfEventLogRecords(hand)
        print(f"Total records: {total_records}")

        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(hand, flags, 0)

        if events:
            for event in events:
                event_id = event.EventID
                event_source = event.SourceName
                event_time = event.TimeGenerated.Format()
                event_message = event.StringInserts

                print(f"Event ID: {event_id}")
                print(f"Source: {event_source}")
                print(f"Time Generated: {event_time}")
                print(f"Message: {event_message}")
                print("-" * 30)
        else:
            print("No events found.")
        win32evtlog.CloseEventLog(hand)
        print()

if __name__ == "__main__":
    print_event_logs()
