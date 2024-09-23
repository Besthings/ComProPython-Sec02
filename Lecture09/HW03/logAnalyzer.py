def analyze_log_file(log_file_path: str) -> dict:
    with open(log_file_path, 'r') as a:
        result = {
            'requests_by_ip': {},
            'most_requested_resource': {},
            'total_404_errors': 0,
            'total_bytes': 0
        }

        for i in a:
            parts = i.split()
            ip = parts[0]
            mosts = parts[2]
            error = parts[3]
            try:
                total_byte = int(parts[4])
            except ValueError:
                continue

            if ip in result['requests_by_ip']:
                result['requests_by_ip'][ip] += 1
            else:
                result['requests_by_ip'][ip] = 1

            if mosts in result['most_requested_resource']:
                result['most_requested_resource'][mosts] += 1
            else:
                result['most_requested_resource'][mosts] = 1

            if error == '404':
                result['total_404_errors'] += 1

            result['total_bytes'] += total_byte

        if result['most_requested_resource']:
            most_requested_resource = max(result['most_requested_resource'], key=result['most_requested_resource'].get)
            result['most_requested_resource'] = most_requested_resource
        else:
            result['most_requested_resource'] = None       

        return result


log_file_path = 'server_log.txt'  # Replace with the path to your log file
result = analyze_log_file(log_file_path)

# Print the analysis result
print("Log File Analysis Result:")
print(f"Requests by IP: {result['requests_by_ip']}")
print(f"Most Requested Resource: {result['most_requested_resource']}")
print(f"Total 404 Errors: {result['total_404_errors']}")
print(f"Total Bytes Transferred: {result['total_bytes']}")
