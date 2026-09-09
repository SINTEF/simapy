"""Progress Management Module.

Manages multiple tqdm progress bars for concurrent SIMA analysis runs.
Each task gets its own progress bar with proper positioning and cleanup.

Example:
    >>> pm = ProgressManager()
    >>> pm.create_progress_bar("Task 1")
    >>> pm.update_progress("Task 1", 50.0)
    >>> pm.close_all()
"""
from tqdm import tqdm

class ProgressManager:
    """Manages multiple progress bars for concurrent task tracking."""
    
    def __init__(self):
        """Initialize with empty progress bar dictionary."""
        self.progress_bars = {}
    
    def create_progress_bar(self, name: str):
        """Create a new progress bar for a task.
        
        Args:
            name (str): Unique identifier for the task
            
        Returns:
            tqdm: The created progress bar object
        """
        self.progress_bars[name] = tqdm(total=100, desc=name, unit="%", position=len(self.progress_bars))
        return self.progress_bars[name]
    
    def update_progress(self, name: str, progress: float):
        """Update progress for a specific task.
        
        Args:
            name (str): Task name to update
            progress (float): New progress value (0.0 to 100.0)
        """
        if name in self.progress_bars:
            pbar = self.progress_bars[name]
            # Calculate the difference to update by
            current = pbar.n
            diff = progress - current
            if diff > 0:
                pbar.update(diff)
    
    def close_progress_bar(self, name: str):
        """Close and cleanup a specific progress bar.
        
        Args:
            name (str): Name of the progress bar to close
        """
        if name in self.progress_bars:
            self.progress_bars[name].close()
            del self.progress_bars[name]
    
    def close_all(self):
        """Close all progress bars and clear the dictionary."""
        for pbar in self.progress_bars.values():
            pbar.close()
        self.progress_bars.clear()