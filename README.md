# Project: SQL Injection

SQL injection is a common security vulnerability for web application developers
to defend against. Or - it used to be common, until many web application
frameworks started including built-in guards against it.

In this assignment, you'll use what you've learned to craft a SQL injection 
attack against a route in an application.

Then, you'll update the code in the application so that it's safe against SQL 
injection.

## The Assignment Scores Application

This example application shows the assignment scores for different students. The
index page shows a list of students with a link to view each of their scores.
The /scores page shows the scores for that student. It also allows the student
to update their name.

_Note: This application is bad in lots of ways (any student can view any other
student's grades, or change their name!) For this assignment, we're focused only 
on attacking and defending the SQL injection vulnerability, not fixing the other
issues._

## Your Task

Somewhere in this application, there is a SQL injection vulnerability. Your task
is to craft an attack URL that uses the vulnerability to change a students
grades. Then, you'll update the code for the application to protect against SQL
injection.

### Part 1 - Injection Attack

Your goal as an attacker is to update student 10's score for the Final Exam to a
95.

- Inspect the code in `app.py` to find any code paths that are vulnerable to SQL
    injection.
- When you find a vulnerability, craft a URL that makes the desired update in 
    the database.
- Test the URL that you've crafted to make sure that your attack works as
    intended 

While attempting to craft the attack, it may be helpful to execute some SQL 
directly. You can reset the database by removing the database file 
(`rm database.db`) and re-initializing it (`python3 initdb.py`).

Your attack must work with the code as it currently exists in app.py -- you 
can't change app.py to make your attack easier.

*Submission*

- Enter your attack URL in the file `attack.md`.
- Enter the SQL payload that it executes
- Write a brief description (a sentence or two is fine) about why the attack works.

### Part 2 - Protecting the application

Now that you've found the vulnerability, it's time to fix the application so
that it is safe against SQL injection attacks. 

*Submission*

- Update `app.py` to fix the vulnerability you found.
- Write a quick description (a sentence or two is fine) about why your fix works
    in `attack.md`

If you only fix app.py, but do not write why the fix works, that will not score
full points!
