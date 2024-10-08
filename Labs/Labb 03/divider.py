import matplotlib.pyplot as plt
import csv
import os

# These lines of code are meant to both shorten the pathway to the csv-files as well as make the program executable outside of my original development environment
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, 'unlabelled_data.csv')
output_file = os.path.join(current_dir, 'labelled_data.csv')


x_values = []
y_values = []
data = []



def classify_datapoint(x, y):
    return 1 if y > x else 0


with open(input_file) as csv_file:
        # The delimiter variable is used to separate the values in the csv-file using the commas as a reference
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            x, y = float(row[0]), float(row[1])
            label = classify_datapoint(x, y)
            x_values.append(x)
            y_values.append(y)
            data.append([x, y, label])


with open(output_file, 'w', newline='') as f_write:
    csv_writer = csv.writer(f_write)

    for row in data:
        csv_writer.writerow(row)

for i in range(len(data)):
    if data[i][2] == 1:
        plt.scatter(x_values[i], y_values[i], color='blue', label='Ovanför' if i == 0 else "")
    else:
        plt.scatter(x_values[i], y_values[i], color='red', label='Nedanför' if i == 0 else "")

min_x = min(x_values)
max_x = max(x_values)

plt.plot([min_x, max_x], [min_x, max_x], color='black', label='y = x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Klassificering av punkter med linjen y = x')
plt.legend()
plt.show()

