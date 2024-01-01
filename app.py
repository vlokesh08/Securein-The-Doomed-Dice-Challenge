from flask import Flask, render_template

app = Flask(__name__)

def calculate_total_combinations():
    die_a_sides = range(1, 7)
    die_b_sides = range(1, 7)
    count = 0
    for i in die_a_sides:
        for j in die_b_sides:
            count += 1
    return count

def generate_all_combinations():
    die_a_sides = range(1, 7)
    die_b_sides = range(1, 7)
    combinations_list = []
    for i in die_a_sides:
        temp = []
        for j in die_b_sides:
            temp.append([i, j])
        combinations_list.append(temp)
    return combinations_list

def calculate_probabilities(die_a, die_b):
    sums_list = []
    for i in die_a:
        for j in die_b:
            s = i + j
            sums_list.append(s)

    counts = {}
    probabilities = {}
    for i in sums_list:
        counts[i] = counts.get(i, 0) + 1

    for i in range(2, 13):
        count_i = counts.get(i, 0)
        probability_i = count_i / len(sums_list)
        probabilities[i] = {"count": count_i, "probability": str(round(probability_i, 3))}

    return probabilities

def transform_dice(die_a, die_b):
    new_die_a = [i - 3 if i > 4 else i for i in die_a]
    new_die_b = [j + 2 if j % 2 == 0 else j for j in die_b]
    return sorted(new_die_a), sorted(new_die_b)

@app.route('/')
def index():
    total_combinations = calculate_total_combinations()

    die_a_sides = range(1, 7)
    die_b_sides = range(1, 7)

    original_probabilities = calculate_probabilities(die_a_sides, die_b_sides)
    all_combinations = generate_all_combinations()
    new_die_a, new_die_b = transform_dice(list(die_a_sides), list(die_b_sides))
    modified_probabilities = calculate_probabilities(new_die_a, new_die_b)

    return render_template('index.html',
                           total_combinations=total_combinations,
                           all_combinations=all_combinations,
                           original_probabilities=original_probabilities,
                           modified_probabilities=modified_probabilities)

if __name__ == '__main__':
    app.run(debug=True)
