def naive_bayes_classifier():
    dataset = [
        ['young', 'High', 'No', 'Fair', 'No'],
        ['young', 'High', 'No', 'Good', 'No'],
        ['Middle_aged', 'High', 'No', 'Fair', 'Yes'],
        ['old', 'Medium', 'No', 'Fair', 'Yes'],
        ['old', 'Low', 'Yes', 'Fair', 'Yes'],
        ['old', 'Low', 'Yes', 'Good', 'No'],
        ['Middle_aged', 'Low', 'Yes', 'Good', 'Yes'],
        ['young', 'Medium', 'No', 'Fair', 'No'],
        ['young', 'Low', 'Yes', 'Fair', 'Yes'],
        ['old', 'Medium', 'Yes', 'Fair', 'Yes'],
        ['young', 'Medium', 'Yes', 'Good', 'Yes'],
        ['Middle_aged', 'Medium', 'No', 'Good', 'Yes'],
        ['Middle_aged', 'High', 'Yes', 'Fair', 'Yes'],
        ['old', 'Medium', 'No', 'Good', 'No']
    ]

    # Total number of records
    n = len(dataset)

    # Calculate the prior probabilities for 'Yes' and 'No'
    count_yes = sum(1 for record in dataset if record[4] == 'Yes')
    count_no = n - count_yes

    p_yes = count_yes / n
    p_no = count_no / n

    # Initialize counters for conditional probabilities
    attr_counts = {
        'age': {'Yes': {}, 'No': {}},
        'income': {'Yes': {}, 'No': {}},
        'student': {'Yes': {}, 'No': {}},
        'credit_rating': {'Yes': {}, 'No': {}}
    }

    # Attributes values we are interested in
    attributes = ['age', 'income', 'student', 'credit_rating']
    values = {
        'age': ['young', 'Middle_aged', 'old'],
        'income': ['High', 'Medium', 'Low'],
        'student': ['Yes', 'No'],
        'credit_rating': ['Fair', 'Good']
    }

    # Initialize all counts
    for attr in attributes:
        for value in values[attr]:
            attr_counts[attr]['Yes'][value] = 0
            attr_counts[attr]['No'][value] = 0

    # Count occurrences of attribute values conditioned on 'Yes' or 'No'
    for record in dataset:
        for i, attr in enumerate(attributes):
            if record[4] == 'Yes':
                attr_counts[attr]['Yes'][record[i]] += 1
            else:
                attr_counts[attr]['No'][record[i]] += 1

    # Ask the user for the input to classify
    new_record = {
        'age': 'young',
        'income': 'Medium',
        'student': 'Yes',
        'credit_rating': 'Fair'
    }

    # Calculate the likelihood probabilities
    p_x_given_yes = 1
    p_x_given_no = 1
    for attr in attributes:
        p_x_given_yes *= (attr_counts[attr]['Yes'][new_record[attr]] / count_yes) if count_yes != 0 else 0
        p_x_given_no *= (attr_counts[attr]['No'][new_record[attr]] / count_no) if count_no != 0 else 0

    # Multiply by the prior probabilities
    p_yes_given_x = p_x_given_yes * p_yes
    p_no_given_x = p_x_given_no * p_no

    # Print the results
    print(f"\nProbability of class 'Yes': {p_yes_given_x}")
    print(f"Probability of class 'No': {p_no_given_x}")

    # Predict the class
    if p_yes_given_x > p_no_given_x:
        print("The predicted class is 'Yes' (Buys computer).")
    else:
        print("The predicted class is 'No' (Does not buy computer).")


if __name__ == '__main__':
    naive_bayes_classifier()
