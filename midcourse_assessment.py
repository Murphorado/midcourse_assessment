import matplotlib.pyplot as plt
import numpy as np

# Pre-defined functions for statistical calculations
def mean(data):
    average = sum(data) / len(data)
    return average

def stdev(data):
    sd = (sum((y - mean(data)) ** 2 for y in data) / (len(data) - 1)) ** 0.5
    return sd

def sterr(data):
    ste = stdev(data) / (len(data)) ** 0.5
    return ste

def gradient(data1, data2):
    numerator = sum((x - mean(data1)) * (y - mean(data2)) for x, y in zip(data1, data2))
    denominator = sum((x - mean(data1)) ** 2 for x in data1)
    m = numerator / denominator
    return m

def intercept(data1, data2):
    c = mean(data2) - mean(data1) * gradient(data1, data2)
    return c

def main():
    # Loading the file into the Python translator...
    fname = input('Enter the file path:')
    try:
        with open(fname) as fhand:
            next(fhand)  # Skip the first line
            columns_list = []

            for line in fhand:
                data = line.strip().split('\t')
                try:
                    float_data = list(map(float, data))
                    columns_list.append(float_data)
                except ValueError:
                    pass

            # Calculate statistics
            mean_m_bodytemp = mean(columns_list[0])
            std_m_bodytemp = stdev(columns_list[0])
            ste_m_bodytemp = sterr(columns_list[0])

            mean_f_bodytemp = mean(columns_list[1])
            std_f_bodytemp = stdev(columns_list[1])
            ste_f_bodytemp = sterr(columns_list[1])

            mean_f_heartrate = mean(columns_list[2])
            std_f_heartrate = stdev(columns_list[2])
            ste_f_heartrate = sterr(columns_list[2])

            gradient_females = gradient(columns_list[1], columns_list[2])
            intercept_females = intercept(columns_list[1], columns_list[2])

            # Print statistics
            print('Mean male body temperature (degrees F):', mean_m_bodytemp)
            print('Standard deviation for male body temperature (+/- degrees F):', std_m_bodytemp)
            print('Standard error for male body temperature (+/- degrees F):', ste_m_bodytemp)

            print('Mean female body temperature (degrees F):', mean_f_bodytemp)
            print('Standard deviation for female body temperature (+/- degrees F):', std_f_bodytemp)
            print('Standard error for female body temperature (+/- degrees F):', ste_f_bodytemp)

            print('Mean female heart rate (bpm):', mean_f_heartrate)
            print('Standard deviation for female heart rate (+/- bpm):', std_f_heartrate)
            print('Standard error for female heart rate (+/- bpm):', ste_f_heartrate)

            print('Gradient of the line of best fit between body temperature (x axis) and heart rate (y axis) in females:', gradient_females)
            print('Intercept of the line of best fit between body temperature (x axis) and heart rate (y axis) in females:', intercept_females)

            # Plotting the linear regression
            plt.scatter(columns_list[1], columns_list[2], label='Data')  # Scatter plot
            plt.plot(columns_list[1], gradient_females * np.array(columns_list[1]) + intercept_females, color='red', label='Linear Regression')  # Regression line
            plt.xlabel('Female Body Temperature (°F)')
            plt.ylabel('Female Heart Rate (bpm)')
            plt.title('Linear Regression: Female Body Temperature vs. Heart Rate')
            plt.legend()
            plt.grid(True)
            plt.show()

    except FileNotFoundError:
        print('File not found or incorrect path:', fname)
    except PermissionError:
        print('You do not have permission to access this file:', fname)
    except Exception as e:
        print('An error occurred:', e)

if __name__ == '__main__':
    main()
