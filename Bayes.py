def naive_bayes_classifier():
    
    dataset = []

    
    n = int(input("Enter the number of records in the dataset: "))

    
    print("Enter the data in the format 'attr1 attr2 class' (attr1 and attr2 can be 0 or 1, class can be 'a' or 'b'):")

    for i in range(n):
        a1, a2, cls = input(f"Enter data for record {i + 1}: ").split()
        dataset.append([int(a1), int(a2), cls])

    
    count_a = sum(1 for record in dataset if record[2] == 'a')
    count_b = n - count_a  

    p_a = count_a / n
    p_b = count_b / n

    attr1_count0a = attr1_count1a = attr1_count0b = attr1_count1b = 0
    attr2_count0a = attr2_count1a = attr2_count0b = attr2_count1b = 0

    
    for record in dataset:
        a1, a2, cls = record
        if a1 == 0:
            if cls == 'a':
                attr1_count0a += 1
            else:
                attr1_count0b += 1
        elif a1 == 1:
            if cls == 'a':
                attr1_count1a += 1
            else:
                attr1_count1b += 1

        if a2 == 0:
            if cls == 'a':
                attr2_count0a += 1
            else:
                attr2_count0b += 1
        elif a2 == 1:
            if cls == 'a':
                attr2_count1a += 1
            else:
                attr2_count1b += 1

    
    attr1_p_zero_given_a = attr1_count0a / count_a if count_a != 0 else 0
    attr1_p_one_given_a = attr1_count1a / count_a if count_a != 0 else 0
    attr1_p_zero_given_b = attr1_count0b / count_b if count_b != 0 else 0
    attr1_p_one_given_b = attr1_count1b / count_b if count_b != 0 else 0

    attr2_p_zero_given_a = attr2_count0a / count_a if count_a != 0 else 0
    attr2_p_one_given_a = attr2_count1a / count_a if count_a != 0 else 0
    attr2_p_zero_given_b = attr2_count0b / count_b if count_b != 0 else 0
    attr2_p_one_given_b = attr2_count1b / count_b if count_b != 0 else 0

    new_attr1 = int(input("Enter new attr1 for prediction (0 or 1): "))
    new_attr2 = int(input("Enter new attr2 for prediction (0 or 1): "))

    
    if new_attr1 == 0:
        p_class_a = attr1_p_zero_given_a
        p_class_b = attr1_p_zero_given_b
    else:
        p_class_a = attr1_p_one_given_a
        p_class_b = attr1_p_one_given_b

    if new_attr2 == 0:
        p_class_a *= attr2_p_zero_given_a
        p_class_b *= attr2_p_zero_given_b
    else:
        p_class_a *= attr2_p_one_given_a
        p_class_b *= attr2_p_one_given_b

    p_class_a *= p_a
    p_class_b *= p_b

    
    print(f"\nProbability of class 'a': {p_class_a}")
    print(f"Probability of class 'b': {p_class_b}")

    
    if p_class_a > p_class_b:
        print("The predicted class is 'a'.")
    else:
        print("The predicted class is 'b'.")

if __name__ == '__main__':
    naive_bayes_classifier()
