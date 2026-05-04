# Task D: Histogram Display
from graphics import *
from tasks_a_b_c import main  # Import the main function from tasks_a_b_c

# Import graphics.py for graphical window and drawing (Source: https://mcsp.wartburg.edu/zelle/python/graphics.py)
class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data
        self.date = date
        self.canvas = None  # Will hold the canvas for drawing
        self.setup_window()

    def setup_window(self):
        """
        Sets up the window for the histogram using graphics.py.
        """
        self.win = GraphWin(f"Histogram - {self.date}", 1500, 700)
        self.win.setBackground("white")

    def draw_histogram(self):
        """
        Draw the histogram with axes, labels, and bars using graphics.py.
        """
        # Title of the histogram
        title_text = f"Histogram of Vehicle Frequency per Hour for {self.date}"
        title = Text(Point(self.win.getWidth() / 2, 30), title_text)
        title.setSize(14)
        title.setTextColor("black")
        title.draw(self.win)

        bar_width = 20  # Width of each bar
        spacing = 2  # Space between bars
        pair_spacing = 15  # Space between different junction bars
        max_vehicle_count = 0  # To track the highest vehicle count

        # Calculate the maximum vehicle count for scaling the bars
        for hour, junctions in self.traffic_data.items():
            for count in junctions.values():
                max_vehicle_count = max(max_vehicle_count, count)

        # Scaling factor to fit the bars within the window
        scaling_factor = 500 / max_vehicle_count
        y_bottom = 600  # Bottom of the Y-axis
        y_top = y_bottom - (max_vehicle_count * scaling_factor) - 50  # Top of the Y-axis
        x_offset = 50  # Left margin of the X-axis

        # Draw X and Y axes
        x_axis = Line(Point(x_offset, y_bottom), Point(1400 - x_offset, y_bottom))
        x_axis.setWidth(2)
        x_axis.draw(self.win)

        y_axis = Line(Point(x_offset, y_bottom), Point(x_offset, y_top))
        y_axis.setWidth(2)
        y_axis.draw(self.win)

        # Draw Y-axis labels (vehicle count)
        for i in range(0, max_vehicle_count + 6, 5):
            y_label = y_bottom - i * scaling_factor
            line = Line(Point(x_offset - 5, y_label), Point(x_offset + 5, y_label))
            line.draw(self.win)

            label = Text(Point(x_offset - 20, y_label), str(i))
            label.setSize(8)
            label.draw(self.win)

        # Draw X-axis labels (hours of the day)
        for hour in range(0, 24):
            x_label = x_offset + hour * (2 * bar_width + pair_spacing) + bar_width
            label = Text(Point(x_label, y_bottom + 10), str(hour))
            label.setSize(8)
            label.draw(self.win)

        # Draw the bars for each hour and junction
        for hour in range(0, 24):
            hour_data = self.traffic_data.get(hour, {})
            junction_a_count = hour_data.get("Elm Avenue/Rabbit Road", 0)
            junction_b_count = hour_data.get("Hanley Highway/Westway", 0)

            junction_a_height = junction_a_count * scaling_factor
            junction_b_height = junction_b_count * scaling_factor

            x1_pair = x_offset + (hour * (2 * bar_width + pair_spacing))

            # Draw the bars for both junctions
            x1_a = x1_pair
            x2_a = x1_a + bar_width
            y1_a = y_bottom
            y2_a = y_bottom - junction_a_height

            x1_b = x2_a + spacing
            x2_b = x1_b + bar_width
            y1_b = y_bottom
            y2_b = y_bottom - junction_b_height

            # Rectangle for junction A
            rect_a = Rectangle(Point(x1_a, y1_a), Point(x2_a, y2_a))
            rect_a.setFill("teal")
            rect_a.draw(self.win)

            # Rectangle for junction B
            rect_b = Rectangle(Point(x1_b, y1_b), Point(x2_b, y2_b))
            rect_b.setFill("coral")
            rect_b.draw(self.win)

            # Text for junction A count
            text_a = Text(Point((x1_a + x2_a) / 2, y2_a - 10), f"{junction_a_count}")
            text_a.setSize(8)
            text_a.draw(self.win)

            # Text for junction B count
            text_b = Text(Point((x1_b + x2_b) / 2, y2_b - 10), f"{junction_b_count}")
            text_b.setSize(8)
            text_b.draw(self.win)

        # Label for X-axis
        x_axis_label = Text(Point(700, 630), "Hours 00:00 to 24:00 ")
        x_axis_label.draw(self.win)

        # Label for Y-axis
        y_axis_label = Text(Point(50, 40), "Vehicle Count")
        y_axis_label.setSize(10)
        y_axis_label.setStyle("bold")
        y_axis_label.setTextColor("black")
        y_axis_label.draw(self.win)

        # Draw the button for loading new data
        self.button = Rectangle(Point(600, 650), Point(750, 680))
        self.button.setFill("mediumseagreen")
        self.button.draw(self.win)

        button_label = Text(self.button.getCenter(), "Load New Data Set")
        button_label.setSize(11)
        button_label.draw(self.win)

    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """
        legend_x = 1200
        legend_y = 40

        # Legend for junction A
        legend_rect_a = Rectangle(Point(legend_x, legend_y), Point(legend_x + 20, legend_y + 20))
        legend_rect_a.setFill("teal")
        legend_rect_a.draw(self.win)
        legend_label_a = Text(Point(legend_x + 120, legend_y + 10), "Elm Avenue/Rabbit Road")
        legend_label_a.setSize(11)
        legend_label_a.draw(self.win)

        # Legend for junction B
        legend_rect_b = Rectangle(Point(legend_x, legend_y + 30), Point(legend_x + 20, legend_y + 50))
        legend_rect_b.setFill("coral")
        legend_rect_b.draw(self.win)
        legend_label_b = Text(Point(legend_x + 120, legend_y + 40), "Hanley Highway/Westway")
        legend_label_b.setSize(11)
        legend_label_b.draw(self.win)

    def run(self):
        """
        Runs the histogram drawing process.
        """
        self.draw_histogram()  # Draw the histogram
        self.add_legend()  # Add the legend

        # Wait for user click to load new data
        while True:
            click = self.win.getMouse()
            if (
                self.button.getP1().getX() <= click.getX() <= self.button.getP2().getX()
                and self.button.getP1().getY() <= click.getY() <= self.button.getP2().getY()
            ):
                print("Load New Data button clicked!")
                self.win.close()
                break

# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        self.traffic_data = {}

    def load_csv_file(self, file_path):
        """
        Loads the CSV file and processes traffic data.
        """
        with open(file_path, "r") as file:
            lines = file.readlines()
            header = lines[0].strip().split(",")
            junction_name_idx = header.index("JunctionName")
            time_of_day_idx = header.index("timeOfDay")

            for line in lines[1:]:
                data = line.strip().split(",")
                junction_name = data[junction_name_idx]
                time_of_day = data[time_of_day_idx]
                hour = int(time_of_day.split(":")[0])

                # Initialize data structure if hour or junction is missing
                if hour not in self.traffic_data:
                    self.traffic_data[hour] = {}

                if junction_name not in self.traffic_data[hour]:
                    self.traffic_data[hour][junction_name] = 0

                # Increment vehicle count
                self.traffic_data[hour][junction_name] += 1

    def process_files(self, file_path):
        """
        Processes the CSV file and extracts the date.
        """
        self.load_csv_file(file_path)
        date_str = file_path.split('traffic_data')[1].split('.')[0]
        return f"{date_str[:2]}/{date_str[2:4]}/{date_str[4:]}"


def handle_user_interaction():
    """
    Handles the loading of datasets and user interaction for file processing.
    """
    while True:
        # Prompt user to load a new dataset or quit
        next_action = input("Do you want to load another data file for a different date? (type 'load' or 'quit'): ").strip().lower()
        if next_action == "quit":
            print("Exiting the program. Goodbye!")
            break
        elif next_action == "load":
            main()  # Invoke traffic_flow_manager's main first
            file_path = input("Enter the path of the CSV file: ").strip()
            processor = MultiCSVProcessor()
            date = processor.process_files(file_path)
            app = HistogramApp(processor.traffic_data, date)
            app.run()  # Run the histogram application
        else:
            print("Invalid input. Please type 'load' or 'quit'.")


if __name__ == "__main__":
    main()  # Run traffic_flow_manager's main initially
    processor = MultiCSVProcessor()
    file_path = input("Enter the path of the CSV file: ").strip()
    date = processor.process_files(file_path)
    app = HistogramApp(processor.traffic_data, date)
    app.run()

    handle_user_interaction()  # Handle user interaction for further file loading
 