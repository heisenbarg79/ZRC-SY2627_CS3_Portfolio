1. What is/are the parent class/es of the Programmer class in the video?
Answer: The direct parent class of "Programmer" is "Employee", while its indirect parent class is "Person". Because "Programmer" inherits from "Employee" and "Employee" inherits from "Person", the "Programmer" class receives all the shared properties and methods from both classes through multilevel inheritance.

2. If you were to add a new role called Intern, where would you place it in the inheritance hierarchy? Why?
Answer: I would place "Intern" as a child class of "Employee", putting it on the same level as "Programmer", "Manager", and "Cleaner". This would fit because an intern is a type of employee, meaning it can reuse existing traits from both "Person" and "Employee" without repeating code. This placement keeps the structure organized while allowing us to simply add intern-specific details, such as school affiliation or internship duration.

