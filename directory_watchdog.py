import time
import tkinter as tk
from tkinter import filedialog, scrolledtext
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DirectoryMonitorHandler(FileSystemEventHandler):
    def __init__(self, text_widget, filter_entry):
        self.text_widget = text_widget
        self.filter_entry = filter_entry

    def should_process_file(self, path):
        filters = self.filter_entry.get().strip()
        if not filters:
            return True
        return any(path.endswith(ext.strip()) for ext in filters.split(','))

    def display_event(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.text_widget.insert(tk.END, f"[{timestamp}] {message}\n")
        self.text_widget.see(tk.END)

    def on_created(self, event):
        if self.should_process_file(event.src_path):
            self.display_event(f"Created: {event.src_path}")

    def on_modified(self, event):
        if self.should_process_file(event.src_path):
            self.display_event(f"Modified: {event.src_path}")

    def on_deleted(self, event):
        if self.should_process_file(event.src_path):
            self.display_event(f"Deleted: {event.src_path}")

    def on_moved(self, event):
        if self.should_process_file(event.src_path):
            self.display_event(f"Moved: from {event.src_path} to {event.dest_path}")

class DirectoryMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Monitor")

        # Status label
        self.status_label = tk.Label(root, text="Status: Not monitoring", fg="red")
        self.status_label.pack(pady=5)

        # Filter frame
        self.filter_frame = tk.Frame(root)
        self.filter_frame.pack(pady=5)
        tk.Label(self.filter_frame, text="File Extension Filter:").pack(side=tk.LEFT)
        self.filter_entry = tk.Entry(self.filter_frame, width=20)
        self.filter_entry.pack(side=tk.LEFT, padx=5)
        tk.Label(self.filter_frame, text="(e.g., .txt,.pdf)").pack(side=tk.LEFT)

        # Button frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.select_button = tk.Button(self.button_frame, text="Select Directory", command=self.select_directory)
        self.select_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear Output", command=self.clear_output)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Output area
        self.output_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.output_area.pack(padx=10, pady=10)

        self.directory_to_monitor = None
        self.observer = None

    def clear_output(self):
        self.output_area.delete(1.0, tk.END)
        self.output_area.insert(tk.END, "Output cleared.\n")

    def select_directory(self):
        try:
            directory = filedialog.askdirectory()
            if directory:
                self.directory_to_monitor = directory
                self.start_monitoring()
                self.output_area.insert(tk.END, f"Successfully started monitoring: {directory}\n")
        except Exception as e:
            self.output_area.insert(tk.END, f"Error selecting directory: {str(e)}\n")
            self.status_label.config(text="Status: Error", fg="red")

    def start_monitoring(self):
        try:
            if self.observer:
                self.observer.stop()
                self.observer.join()

            self.output_area.insert(tk.END, f"Monitoring directory: {self.directory_to_monitor}\n")
            event_handler = DirectoryMonitorHandler(self.output_area, self.filter_entry)
            self.observer = Observer()
            self.observer.schedule(event_handler, self.directory_to_monitor, recursive=True)

            self.observer.start()
            self.status_label.config(text="Status: Monitoring", fg="green")
            self.root.after(100, self.monitor_directory)
        except Exception as e:
            self.output_area.insert(tk.END, f"Error starting monitoring: {str(e)}\n")
            self.status_label.config(text="Status: Error", fg="red")

    def monitor_directory(self):
        try:
            time.sleep(0.1)
        except Exception:
            pass

    def stop_monitoring(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()
        self.status_label.config(text="Status: Not monitoring", fg="red")

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.stop_monitoring)
        self.root.mainloop()

if __name__ == "__main__":
    app = DirectoryMonitorApp(tk.Tk())
    app.run()
