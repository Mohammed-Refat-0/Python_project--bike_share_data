# Python Project 
## Statistics program for Bike-Share provider
### introduction
In this project, I used data provided by Motivate, a bike-share system provider for many major cities in the United States, to write a Python program to uncover bike-share usage patterns. I will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.
### Statistics Computed by the program
#1 Popular times of travel (i.e., occurs most often in the start time)\
most common month\
most common day of week\
most common hour of day

#2 Popular stations and trip\
most common start station\
most common end station\
most common trip from start to end (i.e., most frequent combination of start station and end station)\

#3 Trip duration\
total travel time\
average travel time

#4 User info\
counts of each user type\
counts of each gender (only available for NYC and Chicago)\
earliest, most recent, most common year of birth (only available for NYC and Chicago)\
### Data source and files
Datasets:\
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core of six (6) columns:\
Start Time (e.g., 2017-01-01 00:07:57)\
End Time (e.g., 2017-01-01 00:20:53)\
Trip Duration (in seconds - e.g., 776)\
Start Station (e.g., Broadway & Barry Ave)\
End Station (e.g., Sedgwick St & North Ave)\
User Type (Subscriber or Customer)\
The Chicago and New York City files also have the following two columns:\
Gender\
Birth Year

Files:\
[bikeshare.py](https://github.com/Mohammed-Refat-0/bike_share_data_project/blob/main/bikeshare.py): python program\
[chicago.zip](https://github.com/Mohammed-Refat-0/bike_share_data_project/blob/main/chicago.zip): zip folder containing the .csv Chicago dataset\
[new_york_city.zip](https://github.com/Mohammed-Refat-0/bike_share_data_project/blob/main/new_york_city.zip): zip folder containing the .csv New York dataset\
[washington.zip](https://github.com/Mohammed-Refat-0/bike_share_data_project/blob/main/washington.zip): zip folder containing the .csv Washington dataset\
### Dependencies
Python 3
### How to run
clone this repository in your local machine, install the dependencies, unzip the datasets into the same folder of the bikeshare.py program, and run bikeshare.py to get the results
