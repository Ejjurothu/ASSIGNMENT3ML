import matplotlib.pyplot as plt

# Define the programming languages and their popularity
langs = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create a pie chart of the popularity of programming languages
plt.pie(popularity, labels=langs, autopct='%1.1f%%')

# Add title
plt.title('Popularity of Programming Languages')

# Display the chart
plt.show()
