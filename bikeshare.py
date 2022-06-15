import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

  
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cityname = input("please enter the city name")
        cityname = cityname.lower()
        cityname = str(cityname.strip(' '))
        if cityname in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("please enter a valid city name")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:    
        month = input("if you want to filter the data for a specific month (first 6 month) type month name , else type all ")
        month = month.lower()
        month= str(month.strip(' '))
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("please enter a valid input")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("if you want filter the data for a specific day type the day name, else type all")
        day = day.lower()
        day= str(day.strip(' '))
        if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            break
        else:
            print("Please enter a valid input")

    print('-'*40)
    return cityname, month, day

def load_data(cityname, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[cityname])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        
        df = df[df['day_of_week'] == day.title()]
     
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("most common month is ", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print(" most common day of week  is ", df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ", df['hour'].mode()[0])
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most common start station is ", df['Start Station'].mode()[0], "\n")


    # TO DO: display most commonly used end station
     
    print("most common end station is ", df['End Station'].mode()[0], "\n")
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("most common combination of start station and end station trip is: ", df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time is", df['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time
    print("total mean time is", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")

    # TO DO: Display counts of gender
    # Display earliest, most recent, and most common year of birth
    
    if 'Gender' in df :
        gen = df.groupby(['Gender'])['Gender'].count()
        print(gen)
        mryob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        eyob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        mcyob = df['Birth Year'].mode()[0]
        print("earliest birth year is ", eyob, "\n")
        print("most recent birth year is ", mryob, "\n")
        print("most common birth year is ", mcyob, "\n")
        
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    z = 1
    while True:
        raw = input('\ndo you want to access raw data? type yes or no.\n')
        if raw.lower() == 'yes':
            print(df[z:z+5])
            z = z+5
        else:
            break


def main():
    while True:
        cityname, month, day = get_filters()
        df = load_data(cityname, month, day)
      
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
