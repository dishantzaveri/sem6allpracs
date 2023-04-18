from pyspark import SparkContext

# Create a SparkContext object
sc = SparkContext("local", "Cube of Numbers")

# Create an RDD with the range of numbers 1 to 10
nums = sc.parallelize(range(1, 11))

# Map each number to its cube
cubes = nums.map(lambda x: x**3)

# Filter the cubes greater than 10
result = cubes.filter(lambda x: x > 10)

# Print the result
print(result.collect())

# Stop the SparkContext
sc.stop()