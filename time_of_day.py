# Name: Baaba
# Partners name: Diego
# Rating: 5
# Time taken: 1 hour
# Comment: overall cool

# implementing the what_time_of_day function and the return value will be based on the time parameter
def what_time_of_day(time):
    if  time <= 0 or time >= 2400:
        return "INVALID"
    elif time <= 1200:
        return "Morning"
    elif 1200 <= time <= 1759:
        return "Afternoon"
    elif 1800 <= time <= 2059:
        return "Evening"
    else:
        return "Late Night"

def main():
    pass

if __name__ == '__main__':
    main()
