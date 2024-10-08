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

# y = x
def classify_datapoint_y_eq_x(x, y):
    return 1 if y > x else 0

# f(x) = -0.489x
def classify_datapoint_f(x, y):
    return 1 if y > -0.489 * x else 0

# g(x) = -2x + 0.16
def classify_datapoint_g(x, y):
    return 1 if y > -2 * x + 0.16 else 0

# h(x) = 800x - 120
def classify_datapoint_h(x, y):
    return 1 if y > 800 * x - 120 else 0


with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        x, y = float(row[0]), float(row[1])

        label_y_eq_x = classify_datapoint_y_eq_x(x, y)
        label_f = classify_datapoint_f(x, y)
        label_g = classify_datapoint_g(x, y)
        label_h = classify_datapoint_h(x, y)
        
        x_values.append(x)
        y_values.append(y)

        data.append([x, y, label_y_eq_x, label_f, label_g, label_h])


min_x = min(x_values)
max_x = max(x_values)


with open(output_file, 'w', newline='') as f_write:
    csv_writer = csv.writer(f_write)
    csv_writer.writerow(['x', 'y', 'label_y_eq_x', 'label_f', 'label_g', 'label_h'])
    for row in data:
        csv_writer.writerow(row)


def plot_a_line(x_values, y_values, data, formula, line_label,  classification_index):

    for i in range(len(data)):
        if data[i][classification_index] == 1:
            plt.scatter(x_values[i], y_values[i], color='blue', label='Ovanför' if i == 0 else "")
        else:
            plt.scatter(x_values[i], y_values[i], color='red', label='Nedanför' if i == 0 else "")

    y_min = formula(min_x)
    y_max = formula(max_x)


    plt.plot([min_x, max_x], [y_min, y_max], color="black", label=line_label)


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Klassificering av punkter med linjen {line_label}')
    plt.legend()
    plt.show()



# y = x 
plot_a_line(x_values, y_values, data, lambda x: x, 'y = x', 2)

# f(x) = -0.489x 
plot_a_line(x_values, y_values, data, lambda x: -0.489 * x, 'f(x) = -0.489x', 3)

# g(x) = -2x + 0.16 
plot_a_line(x_values, y_values, data, lambda x: -2 * x + 0.16, 'g(x) = -2x + 0.16', 4)

# h(x) = 800x - 120 
plot_a_line(x_values, y_values, data, lambda x: 800 * x - 120, 'h(x) = 800x - 120', 5)
