import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months= ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

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
    while 1:
        city=input("\n pick a city (chicago, new york city, washington)\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("you picked wrong city\n")
            continue
    
           

    # TO DO: get user input for month (all, january, february, ... , june)
    while 1:
        month= input("pick a month\n").lower()
        if month in months:
            break
        else:
            print("you picked wrong month\n")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
        day= input("pick a day\n").lower()
        if day in days:
            break
        else:
            print("you picked wrong day\n")
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =  df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        is_month= df['month']==month
        df = df[is_month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
       
        is_day =  df['day_of_week']==day.title()
        df = df[is_day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('Most Comman Month:',popular_month)

    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print('Most Comman Day of Week:',popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Comman Start Hour:',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most Comman Start Station:',start_station)

    # TO DO: display most commonly used end station
    end_station= df['End Station'].value_counts().idxmax()
    print('Most Comman End Station:',end_station)
    


    # TO DO: display most frequent combination of start station and end station trip
    start_end_combo = df.groupby(['Start Station','End Station'])['Trip Duration'].count().idxmax()
    print('Most Comman  Combination of Start Station and End Station Trip:', start_end_combo)  
    
    # most frequent combination of start station and end station trip as  count
    start_end_combo_count=df.groupby(['Start Station','End Station'])['Trip Duration'].count().max()
    print('Most Comman  Combination of Start Station and End Station Trip as count:', start_end_combo_count) 
                                 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total Trip Duration is :',total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Trip Duration is :',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count=df['User Type'].count()
    print('User count is : ',user_count)

    if city != 'washington':
    # TO DO: Display counts of gender
        gender_count= df.groupby(['Gender'])['Gender'].count()
        print('User count grouped by gender is : ',gender_count)
                             
                             


    # TO DO: Display earliest, most recent, and most common year of birth
    
        early= df['Birth Year'].min()
        recent= df['Birth Year'].max()
        common= df['Birth Year'].mode()
         
        print('earliest : ',early)
        print('recent : ',recent)
        print( 'common : ', common)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_loc=0
    while True:
        
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        
        if view_data == 'no':
            break
        
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        
                             
                             
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
