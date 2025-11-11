import tkinter as tk

class DemoViewer:
    height = 0
    width = 0

    @staticmethod
    def main():
        # Create main window
        root = tk.Tk()
        root.title("Ticket")

        # Set window size
        root.geometry("400x400")

        # Save dimensions
        DemoViewer.width = 400
        DemoViewer.height = 400

        # Start Tkinter event loop
        root.mainloop()

    @staticmethod
    def get_height():
        return DemoViewer.height

    @staticmethod
    def get_width():
        return DemoViewer.width


if __name__ == "__main__":
    DemoViewer.main()