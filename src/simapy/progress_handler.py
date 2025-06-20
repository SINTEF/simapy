"""
Progress handler for SRE output.

This module provides a tqdm-based progress handler for SRE output.

"""
from tqdm import tqdm

class ProgressHandler:
    def __init__(self, show_output=True):
        self.progress_bar = None
        self.show_output = show_output
    
    def handle_output(self, line: str):
        """
        Process SRE output to execution progress using tqdm.
        
        This handler function monitors the SRE output stream
        and extracts progress information from status messages. When a status message
        is detected, it updates a tqdm progress bar.
        
        Args:
            line (str): A line of text output from the SRE process
            
        Example:
            When SRE outputs a line like: "@STATUS "Total" 800 1000"
            The function will update the tqdm progress bar to 80%
        """
        
        # "@STATUS "Total" 800 1000"
        if line.startswith("@STATUS"):
            # Find the last number
            parts = line.split()
            worked = float(parts[-2])  # Second-to-last value is work completed
            total = float(parts[-1])   # Last value is total work units
            
            # Initialize the progress bar if it doesn't exist yet
            if self.progress_bar is None:
                self.progress_bar = tqdm(total=total, desc="Progress", unit="%")
            
            # Update the progress bar
            self.progress_bar.update(worked - self.progress_bar.n)
            
            # If we've reached the end, close the progress bar
            if worked >= total:
                self.progress_bar.close()
                self.progress_bar = None
        elif self.progress_bar and self.show_output:
            self.progress_bar.write(line)
        elif self.show_output:
            print(line)
