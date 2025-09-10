import matplotlib.pyplot as plt

# Take user input for marks
marks = list(map(int, input("Enter marks separated by spaces: ").split()))

# Define bins for the intervals (0–10, 10–20, ..., 90–100)
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create histogram
plt.hist(marks, bins=bins, edgecolor="black")

# Labels and title
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.title("Histogram of Student Marks")

# Show plot
plt.show()

~                                                                                                                                                       
~                                                                                                                                                       
~                                                                                                                                                       
~                                                                                                                                                       
~   
