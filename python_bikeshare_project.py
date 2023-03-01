import time
import pandas as pd
import numpy as np

#this program lets you interact with bikeshare data from different cities

CITY_DATA = { 'chicago': '._chicago.csv',
              'new york city': '._new_york_city.csv',
              'washington': '._washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    city = ''
    month = ''
    day = ''
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

    #get user input for which city
    while city not in CITY_DATA:
        city = input('Which city would you like to get data for? (Chicago, New York City, Washington or all): \n').lower()
        #check if input is a valid city
        if city not in CITY_DATA:
            print('Not a valid city, try again\n')


    #get user input for month
    while True:
        month = input('What month would you like to filter by?:(1-6 or all)')
        try:
            if int(month) in range(1, 7):
                break
            else:
                print('Please enter a valid month\n')
                continue
        except ValueError:
            if month == 'all':
                break
            else:
                print('Please enter a valid month\n')
                continue


    #get user input for day of week
    while day not in days:
            day = input('Which day would you like to get data for? (Sunday-Saturday or all): \n').lower()
            #check if day is valid
            if day not in days:
                print('Not a valid day, try again\n')



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv('._chicago.csv')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
