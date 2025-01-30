import time
import tkinter as tk
from tkinter import filedialog, scrolledtext
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DirectoryMonitorHandler(FileSystemEventHandler):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    # Append events to the text widget in the GUI
    def display_event(self, message):
        self.text_widget.insert(tk.END, message + "\n")
        self.text_widget.see(tk.END)

    def on_created(self, event):
        self.display_event(f"Created: {event.src_path}")

    def on_modified(self, event):
        self.display_event(f"Modified: {event.src_path}")

    def on_deleted(self, event):
        self.display_event(f"Deleted: {event.src_path}")

    def on_moved(self, event):
        self.display_event(f"Moved: from {event.src_path} to {event.dest_path}")

class DirectoryMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Monitor")
        
        # Select Directory Button
        self.select_button = tk.Button(root, text="Select Directory", command=self.select_directory)
        self.select_button.pack(pady=10)
        
        # Output Text Area
        self.output_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.output_area.pack(padx=10, pady=10)
        
        self.directory_to_monitor = None
        self.observer = None

    def select_directory(self):
        # Open file dialog to select directory
        directory = filedialog.askdirectory()
        if directory:
            self.directory_to_monitor = directory
            self.start_monitoring()

    def start_monitoring(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()

        # Set up the observer and event handler
        self.output_area.insert(tk.END, f"Monitoring directory: {self.directory_to_monitor}\n")
        event_handler = DirectoryMonitorHandler(self.output_area)
        self.observer = Observer()
        self.observer.schedule(event_handler, self.directory_to_monitor, recursive=True)
        
        # Start monitoring
        self.observer.start()
        self.root.after(100, self.monitor_directory)

    def monitor_directory(self):
        try:
            time.sleep(0.1)
        except Exception:
            pass

    def stop_monitoring(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.stop_monitoring)
        self.root.mainloop()

if __name__ == "__main__":
    app = DirectoryMonitorApp(tk.Tk())
    app.run()
