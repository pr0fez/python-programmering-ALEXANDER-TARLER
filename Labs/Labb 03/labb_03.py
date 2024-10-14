import matplotlib.pyplot as plt
import numpy as np
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


def plot_a_line(x_values, y_values, data, formula, line_label, classification_index):
    x_values = np.array(x_values)
    y_values = np.array(y_values)
    classifications = np.array([row[classification_index] for row in data])
  
    plt.scatter(x_values[classifications == 1], y_values[classifications == 1], color='blue', label='Ovanför')
    plt.scatter(x_values[classifications == 0], y_values[classifications == 0], color='red', label='Nedanför')

    min_x, max_x = x_values.min(), x_values.max()
    plt.plot([min_x, max_x], [formula(min_x), formula(max_x)], color='black', label=line_label)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Klassificering av punkter med linjen {line_label}')
    plt.legend()
    plt.show()

def compare_classifications(data):
    comparisons = {
        "y_eq_x vs f": 0,
        "y_eq_x vs g": 0,
        "y_eq_x vs h": 0,
        "f vs g": 0,
        "f vs h": 0,
        "g vs h": 0,
    }
    total_points = len(data)
    
    for row in data:
        label_y_eq_x, label_f, label_g, label_h = row[2], row[3], row[4], row[5]
        

        if label_y_eq_x != label_f:
            comparisons["y_eq_x vs f"] += 1
        if label_y_eq_x != label_g:
            comparisons["y_eq_x vs g"] += 1
        if label_y_eq_x != label_h:
            comparisons["y_eq_x vs h"] += 1
        if label_f != label_g:
            comparisons["f vs g"] += 1
        if label_f != label_h:
            comparisons["f vs h"] += 1
        if label_g != label_h:
            comparisons["g vs h"] += 1


    print("Skillnader i klassificeringar:")
    for key, value in comparisons.items():
        percentage_difference = (value / total_points) * 100
        print(f"{key}: {value} punkter skiljer sig ({percentage_difference:.2f}%)")


compare_classifications(data)


# y = x 
plot_a_line(x_values, y_values, data, lambda x: x, 'y = x', 2)

# f(x) = -0.489x 
plot_a_line(x_values, y_values, data, lambda x: -0.489 * x, 'f(x) = -0.489x', 3)

# g(x) = -2x + 0.16 
plot_a_line(x_values, y_values, data, lambda x: -2 * x + 0.16, 'g(x) = -2x + 0.16', 4)

# h(x) = 800x - 120 
plot_a_line(x_values, y_values, data, lambda x: 800 * x - 120, 'h(x) = 800x - 120', 5)

