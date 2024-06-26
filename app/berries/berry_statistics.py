""" Manage the statistics data """
from statistics import mean, median, variance
from .berry_data_fetcher import BerryDataFetcher

class BerryStatistics:
    """ Class responsible for calculating statistics about berries. """

    def __init__(self, berry_data_fetcher: BerryDataFetcher):
        self.berry_data_fetcher = berry_data_fetcher
        self.growth_times = self.get_berry_growth_times()

    @property
    def berries_names(self) -> list:
        """ Get the names of all berries.

        Returns:
            list: A list of all berries names.
        """
        names = [item['name'] for item in self.berry_data_fetcher.all_data]
        return names

    @property
    def min_growth_time(self) -> int:
        """ Returns the minimum growth time of the berries. """
        return min(self.growth_times)

    @property
    def max_growth_time(self):
        """ Returns the maximum growth time of the berries. """
        return max(self.growth_times)


    def get_berry_growth_times(self) -> list:
        """ Returns the growth times of the berries.

        Returns:
            list: The growth times of the berries.
        """
        growth_times = []

        for berry in self.berry_data_fetcher.all_data:
            berry_data = self.berry_data_fetcher.fetch_data(berry['url'])
            growth_time = berry_data['growth_time']
            growth_times.append(growth_time)

        return growth_times

    def __calculate_frequency(self, numbers: list) -> dict:
        """ Calculates the frequency of each number in a list.

        Args:
            numbers (list): The list of numbers.

        Returns:
            dict: The frequency of each number.
        """

        frequency = {}

        for time in numbers:
            if time in frequency:
                frequency[time] += 1
            else:
                frequency[time] = 1

        return frequency

    def get_stats(self) -> dict:
        """Calculates and returns the statistics of the berries.

        Returns:
            dict: The statistics of the berries.
        """
        median_growth_time = median(self.growth_times)
        variance_growth_time = round(variance(self.growth_times), 2)
        mean_growth_time = round(mean(self.growth_times), 2)
        frequency_growth_time = self.__calculate_frequency(
            self.growth_times)

        return {
            "berries_names": self.berries_names,
            "min_growth_time": self.min_growth_time,
            "median_growth_time": median_growth_time,
            "max_growth_time": self.max_growth_time,
            "variance_growth_time": variance_growth_time,
            "mean_growth_time": mean_growth_time,
            "frequency_growth_time": frequency_growth_time
        }
