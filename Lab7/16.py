import pandas as pd
import math
import sys

# Load the dataset
f=open(sys.argv[1])
df = pd.read_csv(sys.argv[1], sep="\t")
columns=list(df.columns)
Label_col=columns[len(columns)-1]

# Define the entropy calculation function
def entropy(probs):
    return sum([-prob * math.log(prob, 2) for prob in probs])

# Define the information gain calculation function
def information_gain(data, feature, target):
    # Calculate the entropy of the entire dataset
    total_entropy = entropy(data[target].value_counts(normalize=True))

    # Calculate the weighted entropy for each possible value of the feature
    weighted_entropy = 0
    for value in data[feature].unique():
        subset = data[data[feature] == value]
        weight = len(subset) / len(data)
        subset_entropy = entropy(subset[target].value_counts(normalize=True))
        weighted_entropy += weight * subset_entropy

    # Calculate the information gain
    information_gain = total_entropy - weighted_entropy
    return information_gain

# Define the ID3 algorithm function
def id3(data, original_data, features, target_attribute_name=Label_col):
#Termination conditions:
    # pure attribute
    if len(data[target_attribute_name].unique()) <= 1:
        return data[target_attribute_name].unique()[0]

    # If dataset becomes empty then from that dataset we need to select the maximum occuring values
    elif len(data) == 0:
        return original_data[target_attribute_name].mode()[0]

    # IIf features are over then from that dataset we need to select the maximum occuring values
    elif len(features) == 0:
        return data[target_attribute_name].mode()[0]

#No More termination conditions
    else:
        
        default = data[target_attribute_name].mode()[0]

        # Select the feature that best splits the dataset
        best_feature = max(features, key=lambda feature: information_gain(data, feature, target_attribute_name))

        
        tree = {best_feature: {}}

        #remove the column with highest information gain
        remaining_features = [feature for feature in features if feature != best_feature]

        # Build a subtree for each possible value of the best feature
        for value in data[best_feature].unique():
            subset = data[data[best_feature] == value]
            subtree = id3(subset, data, remaining_features, target_attribute_name)

            # Add the subtree to the tree
            tree[best_feature][value] = subtree

        return tree

#Prediction
def predict(instance, tree):
    attribute = list(tree.keys())[0]
    if instance[attribute] in tree[attribute]:
        result = tree[attribute][instance[attribute]]
        if isinstance(result, dict):
            return predict(instance, result)
        else:
            return result
    else:
        return "No"

# Example usage:


# Build the decision tree
features = list(df.columns[:-1])
tree = id3(df, df, features)
print("Tree",type(tree))

# Print the decision tree
import json
answer = json.dumps(tree, indent=4)
print(answer)
columns=list(df.columns)[-1]

# Load test data
test_data = pd.read_csv(sys.argv[1],sep="\t").to_dict(orient='records')

# Predict test data using decision tree
predictions = []
Correct=0
Incorrect=0
for instance in test_data:
    prediction = predict(instance, tree)
    if(instance[columns] == prediction):
        Correct+=1
    else:
        Incorrect+=1
    predictions.append(prediction)

print("Correct = ", Correct,"\n", "Incorrect = ",Incorrect,"\n")
print("Accuracy = ",100*Correct/(Correct+Incorrect),"%")

# test_instance = {'outlook': 'sunny', 'temperature': 'hot', 'humidity': 'high', 'windy': 'false'}
# print(predict(test_instance, tree))


