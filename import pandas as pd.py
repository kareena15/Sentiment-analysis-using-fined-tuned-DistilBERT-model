import pandas as pd
data = {'Name': ['kareena', 'shagun', 'divyanshi', 'zoya'],
       'Age': [22, 23, 22, 21],
       'City': ['noida', 'haridawar', 'kanpur', 'kanpur'],
       'Salary': [50000, 60000, 70000, 55000]
}  
df = pd.DataFrame(data)
print("Original DataFrame:\n",df)

df['Age'] = df['Age'] + 1
df['Department'] = ['IT', 'Sales', 'HR', 'Finance']
print("Updated DataFrame:\n",df)

fil_df = df[df['Salary'] > 55000]
print("Filtered DataFrame:\n",fil_df)

sort_df = df.sort_values(by='Salary', ascending=False)
print("Sorted DataFrame:\n",sort_df)

avg_salary = df['Salary'].mean()
print("Average Salary:", avg_salary)