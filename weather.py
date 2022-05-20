import csv
from datetime import datetime
from time import strftime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # strptime what type do they expect as an argument what type do they return
    # strftime

    iso_string_nt = iso_string[:-15]

    iso_object1 = datetime.strptime(iso_string_nt, "%Y-%m-%d")

    format = iso_object1.strftime("%A %d %B %Y")
    return(format)


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    tf_float = float(temp_in_farenheit)
    calculator = (tf_float - 32) * 5/9
    return round(calculator, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    wd_float = [float(x) for x in weather_data]
    mean = (sum(wd_float))/len(weather_data)
    return(float(mean))


def load_data_from_csv(csv_f):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    list_of_lists = []

    with open(csv_f) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            list_of_lists.append(row)

        list_of_lists.pop(0)
        for i in list_of_lists:
            for j in i:
                i[1] = int(i[1])
                i[2] = int(i[2])

        # using this to get rid of empty rows that are creating empty lists
        final_list = ([x for x in list_of_lists if x])

    return final_list


def find_min(a_list):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if a_list == []:
        return()
    else:
        mv_float = [float(x) for x in a_list]
        min_value = min(mv_float)
        for i in reversed(range(len(mv_float))):
            if mv_float[i] == min_value:
                return(min_value, i)


def find_max(a_list):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if a_list == []:
        return()
    else:
        mv_float = [float(x) for x in a_list]
        max_value = max(mv_float)
        for i in reversed(range(len(mv_float))):
            if mv_float[i] == max_value:
                return(max_value, i)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


weather_data = load_data_from_csv("tests\data\example_one.csv")


# changing dates to human readable ones
dates = []
for x in weather_data:
    dates.append(convert_date(x[0]))

# temperature convertions min temps during the days
min_temps = []
for x in weather_data:
    min_temps.append(convert_f_to_c(x[1]))

# temperature convertions max temps during the days
max_temps = []
for x in weather_data:
    max_temps.append(convert_f_to_c(x[2]))


# finding min and max temps

min_and_max_temps = min_temps + max_temps

min = find_min(min_and_max_temps)
# print(min)

max = find_max(min_and_max_temps)
# print(max)

max_mean = calculate_mean(max_temps)
print(max_mean)

min_mean = calculate_mean(min_temps)
print(min_mean)


print(
    f"5 day Overview \n The lowest temperature will be{min[0]},and will occur on {dates,{min[1]}}. \n ")


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
