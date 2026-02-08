import csv
from datetime import datetime
import sys

from matplotlib import pyplot as plt
filename = 'sitka_weather_2018_simple.csv'

def get_weather_data(column_index):
    """ Helper function to get weather data from the CSV data based on the chosen column index. """
    
    dates, values = [], []
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                try:
                    temp = int(row[column_index])
                except ValueError:
                    print(f"Missing data for {current_date}")
                

                    dates.append(current_date)
                    values.append(temp)
        return dates, values
    except FileNotFoundError:
        print(f"File {filename} not found .Please check the file in the correct directory.")
        return None, None
def plot_data(dates, values, title, color):
        """Handle the Mathplotlib plotting of the data."""
        plt.style.use('seaborn-v0_8') #'seaborn' depending on version
        fig, ax = plt.subplots()
        ax.plot(dates, values, c=color) 

      # Format plot.
        plt.title(title, fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()    
         
def main_menu():
    """ Main program loop and menu logic"""
    print("Welcome to the Sitka Weather Data Visualization!")
    print("Please select the data you want to visualize:Enter'1' for High Temperatures, "
           "'2' for Low Temperatures, '3' for Precipitation, or '4' to Exit.")
    while True:
        print("\nMenu:")
        print("1 High Temperatures (Red)")
        print("2 Low Temperatures (Blue)")
        print("3 Precipitation (Green)")
        print("4 Exit")

        choice = input("Enter your choice: ")
        if choice=='1':
            dates, highs = get_weather_data(5)  # High temperatures are in column index 5
            
            plot_data(dates, highs, "Daily High Temperatures - 2018", 'red'"")
        elif choice == '2':
            dates, lows = get_weather_data(6)  # Low temperatures are in column index 6
            
            plot_data(dates, lows, "Daily Low Temperatures - 2018", 'blue' "")
                      
        elif choice == '3':
            dates, precipitation = get_weather_data(7)  # Precipitation is in column index 7
            
            plot_data(dates, precipitation, "Daily Precipitation - 2018", 'green', "Precipitation (inches)")
        elif choice == '4':
            print(" Thank you for using the Sitka Weather Data Visualization program. Goodbye!")
            sys.exit()
            
        else:           
    
            print("Invalid choice. Please enter a number 1, 2, 3, or 4.")

            

            
if __name__ == "__main__":
       main_menu()


    
   