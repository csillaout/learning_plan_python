=======================================
LEARNING PLAN

- Python Basics
- Intermediate Python
- Object Oriented Python
- Advanced Python
- Review
- Project

=======================================
RESOURCES

Python: Official Documentation & Python3 Fundamentals - Pluralsight
Python: Beginner Guides and Documentation
Pytest: Testing in Python 3
fastAPI: FastAPI Fundamentals - Pluralsight and fastAPI Official Documentation
GitLab: GitLab Fundamentals
ChatGPT for revising, generating data and creating exersices and examples

=======================================
WEEK 1

1. Python Basics

- Understand the Fundamentals of Python Programming
  -- Install Python on computer
  -- Create first Python file in VSCode
  -- Use a print statement to output "Hello World" to the console
  -- Run file using the command python3 FILE_NAME
  -- Learn about variables, data types, and basic Python syntax

- Learn About Python Data Structures
  Understand the basics of Python's3 of the the built-in data types: lists, tuples, and, dictionaries
  Work with conditional statements and loops
  Do exercises involving manipulating data structures

- Learn About Functions and Modules
  Understand function definition and calling
  Exercise involving writing and using a custom function
  Learn About Python modules and libraries
  Find at least one Python module and/or library and write a function that utilizes it
  Understand **init**.py and **main**

- Exercises:
  Rock, Paper, Scissors
  Guess the Word

  2. Intermediate Python
     This section covers the following topics:

Advanced Data Structures
File Handling and Exceptions
Unit Testing in Python
With the above steps completed, you'll be able to create more sophisticated programs and functionality for your users.

Learn about sets and frozensets
Work with nested data structures (a list of lists, a list of dictionaries, etc.)
Find and manipulate an advanced dataset
Can't find a dataset? Ask ChatGPT to create a dataset for you!
File Handling and Exceptions

Learn how to read and write files
Work with exception handling to catch and handle errors
Do an exercise involving file handling and exception handling
E.g. Write a Python program that reads a text file and counts the number of words in it. The program should handle file handling and exception handling to ensure that the file exists and can be accessed without errors.
Unit Testing in Python

Install the pytests unit testing library
Go back to the mini-project you made from the last section and create some tests for functions you you wrote.
Use a TDD approach to create some functions by writing the tests before creating the functions.
E.g. Write tests for a function to return the largest element of an array before writing the function itself.
Build Something! 🔨

Option #1 - Word Frequency Analyzer: Create a word frequency analyzer that reads a text file, process its contents, and generate a report of the frequency of each word in the file. Be sure to utilize exception handling and write unit tests.
Option #2 - Movie Recommendation System: Create a movie recommendation system that will suggest movies to users based on their preferences and previously watched movies. The program should read a file containing a list of previously watched movies and their genres and recommends movies based on the values in the file. Be sure to utilize exception handling and write unit tests.

3. Object Oriented Python
   This section covers the following topics:

Classes and Objects
Inheritance
Polymorphism
Encapsulation
By completing the above steps, you will have a stronger understanding of object oriented programming, which will allow you to structure your projects and reuse code in different ways.

Tasks
Classes and Objects

Create a simple class with attributes and methods.
Create an object of the class and access its attributes and methods.
Write a program that uses a class to model a real-world object.
E.g. Create a Person class with a name, age, and hometown properties. The class should also have a bio method that prints on the persons information.
Inheritance

Create a subclass that inherits from a superclass.
Override a method in the subclass.
Use inheritance to create a hierarchy of classes that models a real-world scenario.
E.g. Create an Animal parent class with multiple animal subclasses that inherit information from the parent class.
Polymorphism

Create a program that uses polymorphism through method overriding and/or method overloading.
Use the isinstance() function to check the type of an object.
Write a program that demonstrates the concept of polymorphism in a real-world scenario.
E.g. Create a shape calculator that calculates the area of different shapes such as rectangles, circles, and triangles each with a area() method.
Encapsulation

Create a class with private attributes and methods.
Use getter and setter methods to access and modify private attributes.
Write a program that uses encapsulation to protect data in a real-world scenario.
E.g. Create a bank account management system. The program allows users to create bank accounts, deposit and withdraw money, and retrieve the account balance. The program should ensure that the internal details and operations of the bank account are hidden and can only be accessed through well-defined methods.
Build Something 🔨

Option #1 - Scooter Application: Recreate the Scooter Application from Bootcamp using Python.
Option #2 - Inventory Management System: Create an online store inventory that allows users to add, update, and view products in an store's inventory. Users should also be able to perform operations such as checking stock availability, calculating total inventory value, and generating inventory reports.

4. Advanced Python
   This section covers the following topics:

Regular Expressions
Web Scraping
Data Visualization
These topics could easily take a day each - don't try to become an expert in all of it, just take a few hours to explore each one so that you know what is possible with Python and see a few interesting patterns.

Tasks
Regular Expressions

Understand the basics of regular expressions
Learn how to use the re module to search for and manipulate strings
Do an exercise involving regular expressions.
E.g. Use regular expressions to validate that email addresses are in a valid format.
Web Scraping

Understand the basics of web scraping
Learn how to use the requests and BeautifulSoup libraries to scrape websites
Utilize the requests and/or BeautifulSoup libraries to create a program that uses web scraping
Data Visualization

Learn about data visualization libraries like Matplotlib and Seaborn
Understand the basics of creating plots and charts
Create a program that creates a data visualization using Matplotlib and/or Seaborn

5.  Project Plan
    Recipe Finder
    Overview:
    Create a web app to browse and search recipes by ingredients or cuisine type.
    Steps:
    Data Source: Use a free recipe API like Spoonacular to get recipe data.
    Backend:
    Build endpoints to:
    List recipes based on an ingredient search.
    Fetch details about a specific recipe (e.g., instructions, ingredients, nutrition).
    Add a filter for dietary preferences like vegetarian, vegan, or gluten-free.
    Frontend:
    Create a simple UI where users can:
    Input ingredients or select cuisine types.
    Browse recipe results.
    View detailed recipe information.
    Enhancements:
    Add functionality to save favorite recipes.
    Display nutritional information for each recipe.

General Steps for All Projects:
Backend (FastAPI):
Create endpoints to fetch data from the source API or static dataset.
Use data processing or caching to optimize responses.
Document the API using FastAPI's built-in Swagger UI.
Frontend (UI):
Use HTML, CSS, and JavaScript to create the interface.
Integrate a library like Bootstrap for responsive design.
Fetch data using the FastAPI endpoints with fetch or axios.
Deployment:
Deploy the app using Docker or directly on Render or Heroku.
Use NGINX or Gunicorn to serve the application.
