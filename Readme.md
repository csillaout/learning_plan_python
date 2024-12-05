=======================================

LEARNING PLAN

=======================================

- Python Basics
- Intermediate Python
- Object Oriented Python
- Advanced Python
- Review
- Project

=======================================

RESOURCES

=======================================

Python: Official Documentation & Python3 Fundamentals - Pluralsight
Python: Beginner Guides and Documentation
Pytest: Testing in Python 3
fastAPI: FastAPI Fundamentals - Pluralsight and fastAPI Official Documentation
GitLab: GitLab Fundamentals
ChatGPT for revising, generating data and creating exersices and examples

=======================================
WEEK 1

1. Python Basics

Understand the Fundamentals of Python Programming

- Install Python on computer
- Create first Python file in VSCode
- Use a print statement to output "Hello World" to the console
- Run file using the command python3 FILE_NAME
- Learn about variables, data types, and basic Python syntax

Learn About Python Data Structures

- Understand the basics of Python's3 of the the built-in data types: lists, tuples, and, dictionaries
- Work with conditional statements and loops
- Do exercises involving manipulating data structures

Learn About Functions and Modules

- Understand function definition and calling
- Exercise involving writing and using a custom function
- Learn About Python modules and libraries
- Find at least one Python module and/or library and write a function that utilizes it
- Understand **init**.py and **main**

Exercises 🔨

- Rock, Paper, Scissors
- Guess the Word

2. Intermediate Python

Advanced Data Structures

- Learn about sets and frozensets
- Work with nested data structures (a list of lists, a list of dictionaries, etc.)
- Find and manipulate an advanced dataset

File Handling and Exceptions

- Learn how to read and write files
- Work with exception handling to catch and handle errors
- Exercise involving file handling and exception handling

Unit Testing in Python

- Install the pytests unit testing library
- Use a TDD approach to create some functions by writing the tests before creating the functions.

Exercises 🔨

- Word Frequency Analyzer: Create a word frequency analyzer that reads a text file, process its contents, and generate a report of the frequency of each word in the file. Be sure to utilize exception handling and write unit tests.
- Movie Recommendation System: Create a movie recommendation system that will suggest movies to users based on their preferences and previously watched movies. The program should read a file containing a list of previously watched movies and their genres and recommends movies based on the values in the file. Be sure to utilize exception handling and write unit tests.

WEEK 2

3. Object Oriented Python

Classes and Objects

- Create a simple class with attributes and methods.
- Create an object of the class and access its attributes and methods.

Inheritance

- Create a subclass that inherits from a superclass.
- Override a method in the subclass.

Polymorphism

- Create a program that uses polymorphism through method overriding and/or method overloading.
- Use the isinstance() function to check the type of an object.

Encapsulation

- Create a class with private attributes and methods.
- Use getter and setter methods to access and modify private attributes.

Exercises 🔨

- Inventory Management System: Create an online store inventory that allows users to add, update, and view products in an store's inventory. Users should also be able to perform operations such as checking stock availability, calculating total inventory value, and generating inventory reports.

4. Advanced Python

Regular Expressions

- Understand the basics of regular expressions
- Learn how to use the re module to search for and manipulate strings

Web Scraping

- Understand the basics of web scraping
- Learn how to use the requests and BeautifulSoup libraries to scrape websites
- Utilize the requests and/or BeautifulSoup libraries to create a program that uses web scraping

Data Visualization

- Learn about data visualization libraries like Matplotlib and Seaborn
- Understand the basics of creating plots and charts
- Create a program that creates a data visualization using Matplotlib and/or Seaborn

WEEK 3 & 4

5.  Project

RECIPE FINDER 🍔

- Overview:
  Create a web app to browse and search recipes by ingredients or cuisine type.
- Steps:
  Data Source: Use a free recipe API like Spoonacular to get recipe data.
- Backend:
  Build endpoints to:
  List recipes based on an ingredient search.
  Fetch details about a specific recipe (e.g., instructions, ingredients, nutrition).
  Add a filter for dietary preferences like vegetarian, vegan, or gluten-free.
- Frontend:
  Create a simple UI where users can:
  Input ingredients or select cuisine types.
  Browse recipe results.
  View detailed recipe information.
- Enhancements:
  Add functionality to save favorite recipes.
  Display nutritional information for each recipe and calculate calorie intake

General Steps for All Projects:

- Backend (FastAPI):
  Create endpoints to fetch data from the source API or static dataset.
  Use data processing or caching to optimize responses.
  Document the API using FastAPI's built-in Swagger UI.
- Frontend (UI):
  Use HTML, CSS, and JavaScript to create the interface.
  Integrate a library like Bootstrap for responsive design.
  Fetch data using the FastAPI endpoints with fetch or axios.
- Deployment:
  Deploy the app using Render.
  Use NGINX or Gunicorn to serve the application.
