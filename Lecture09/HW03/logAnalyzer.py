def analyze_log_file(log_file_path: str) -> dict:
    with open(log_file_path, 'r') as a:
        pass
        


log_file_path = 'server_log.txt'  # Replace with the path to your log file
result = analyze_log_file(log_file_path)

# Print the analysis result
print("Log File Analysis Result:")
print(f"Requests by IP: {result['requests_by_ip']}")
print(f"Most Requested Resource: {result['most_requested_resource']}")
print(f"Total 404 Errors: {result['total_404_errors']}")
print(f"Total Bytes Transferred: {result['total_bytes']}")
