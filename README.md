# pyspeeder
A repository for testing different approach to runtime optimization of Python programs

Testing different approaches to speeding up Python programs, e.g. Numba, c-optimization and so on

Things to keep in mind:
- When working with numba and functions that work with lists, it is best to work with numpy arrays instead of Python lists
- When working with numba instead of working with initially empty lists to which elements are appended, it is better to create an initial numpy array of defined type and length; this will help numba enhance performance to an even greater extend
- Tosee the impact of this compare example 2 with example 3. Example 3 uses numpy arrays of predefined lengths, while example 2 facilitates the same overall logic with python lists that are initially empty and then are appended to
