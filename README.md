
# Directory Watchdog

This is a Python application that monitors file system events (such as creation, modification, deletion, and movement) in a selected directory. The application uses `tkinter` for the GUI and `watchdog` to observe file system changes. The events are displayed in a scrollable text widget in the GUI.

## Features
- **Monitor a directory:** Choose any directory to monitor for file changes.
- **Real-time updates:** Displays events such as file creation, modification, deletion, and movement.
- **Scrollable output:** All events are shown in a scrollable text area.
- **Cross-platform:** Compatible with major operating systems (Windows, macOS, Linux).

## Requirements
- Python 3.x
- `tkinter` (usually comes pre-installed with Python)
- `watchdog` library

## Installation

To get started, you need to install the `watchdog` library:

```bash
pip install watchdog
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/pralinkhaira/directory-watchdog.git
   cd directory-watchdog
   ```

2. Run the `directory_watchdog.py` file:
   ```bash
   python directory_watchdog.py
   ```

3. In the GUI, click the **"Select Directory"** button and choose the directory you want to monitor. 
4. The application will start showing the events in the scrollable text area. 

## Features of the Application

- **Select Directory:** Select the directory you want to monitor.
- **Events Displayed:** Creation, modification, deletion, and movement of files.
- **Stop Monitoring:** Close the application to stop monitoring the directory.

## Screenshot

![image](https://github.com/user-attachments/assets/d57bde8f-ac55-4e91-9e50-634a2453a1d7)
![image](https://github.com/user-attachments/assets/120417b2-1e7f-4a58-b62e-c8f688f96121)


## Example

When you create, modify, delete, or move a file in the monitored directory, the corresponding event will be shown in the GUI output.

Example output:

```
Monitoring directory: /path/to/directory
Created: /path/to/directory/new_file.txt
Modified: /path/to/directory/modified_file.txt
Deleted: /path/to/directory/old_file.txt
Moved: from /path/to/directory/old_location.txt to /path/to/directory/new_location.txt
```

## Update v2 by Marcus (October 1, 2025)

### New Features Added:
- **Error Handling:** Improved robustness with comprehensive error handling for directory selection and monitoring
- **Status Indicator:** Visual status display showing current monitoring state (Monitoring/Not Monitoring/Error)
- **Clear Output Button:** Added ability to clear the monitoring history with one click
- **Timestamps:** All events now include timestamps for better tracking
- **File Extension Filter:** New filter functionality to monitor specific file types
  - Example: Enter `.txt,.pdf` to only monitor text and PDF files
  - Leave empty to monitor all files

### GUI Improvements:
- Added button frame for better organization
- Status label showing current monitoring state
- File extension filter input field
- Clear output button alongside directory selection

### Example Output with New Features:
```
[2025-10-01 14:30:22] Monitoring directory: C:/Users/Documents
[2025-10-01 14:30:45] Created: C:/Users/Documents/new_file.txt
[2025-10-01 14:31:01] Modified: C:/Users/Documents/existing_file.pdf
Status: Monitoring
```

### Coming Soon:
- Pause/Resume monitoring functionality
- Save logs to file option
- Dark/Light theme toggle
- System tray minimization
- Last monitored directory memory

## Contributing

Feel free to fork this project and submit pull requests. Any contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
