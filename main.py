import pandas as pd
import numpy as np

diab_data = pd.read_csv('diabetes.csv')

# First, let's check what types of data we are dealing with using the print statement below (uncommennt as needed)
print(diab_data.dtypes)

# Next, let's find the amount of columns in the DataFrame
print(len(diab_data.columns)) #(there are 9)

#Then, let's find the amount of rows
print(len(diab_data)) #(there are 768)

# Let's check how clean the data is by checking for null values

# While we could use a function like this, it is much easier to user different methods...
"""def is_null(diab_data):
    n_values = False
    for i in diab_data.values:
        for j in range(0, len(i)):
            #checking for null elements
            if(i[j] == None):
                n_values = True
    if(n_values):
        print("There are null values")
    else:
        print("There are no null values")
"""
# While there seems to be no null values, theres likely still missing data
# We can access this data by using the statement below
print(diab_data.describe())

# There are a few things that are odd with this data, such as the minimum value for all the columns is zero
# However, a person would be dead if any of these values were zero, so we know this could not be the case...

# There are also some outliers including the maximum and minimum when compared to the mean for seemingly every column...

# Next, we will want to reaplce all the zeroes with 'Nan' which means not a number, this should hopefully make our data more accurate
diab_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diab_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

# Now let's check to see if there are any null values in the data
print(diab_data.isnull().sum())

# Alternatively, there is another way to display these values
print(diab_data.info())

# Now let's check where each null value is coming from
print(diab_data[diab_data.isnull().any(axis=1)])

# Let's now check the datatypes in this DataFrame
print(diab_data.dtypes)

# Notice how the Outcome column is distinct in the fact that it has an object value...
print(diab_data['Outcome'].unique())

# It looks like we have values of both the number 0 and the letter O
# We would want to replace this using the following code...
diab_data['Outcome'] = diab_data['Outcome'].replace('O', '0')

# Now we just jave to check to make sure everything looks good!
print(diab_data['Outcome'].unique())

# Finally, let's change the string '0' to int 0
diab_data['Outcome'] = diab_data['Outcome'].astype('int')
print(diab_data.dtypes)