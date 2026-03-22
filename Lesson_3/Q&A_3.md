# 🧠 Python for Everybody: Chapter 3 Quiz Summary
**Student:** Abdelaziz Merzoug  
**Course:** Python for Everybody  
**Module:** Conditional Execution

---

### 🔀 Section 1: Conditional Execution & Indentation

**Q1: Indicating Conditional Code**
* **Question:** What do we do to a Python statement that is immediately after an `if` statement to indicate that the statement is to be executed only when the `if` statement is true?
* **Answer:** **Indent the line below the if statement.**
* **Logic:** Python uses indentation (spaces or tabs) to define the scope and boundaries of a code block. Everything indented under the `if` statement belongs to that condition.

**Q2: Block Execution**
* **Question:** What is true about the following code segment?
  ```python
  if x == 5:
      print('Is 5')
      print('Is Still 5')
      print('Third 5')
  
* **Answer**: Depending on the value of x, either all three of the print statements will execute or none of the statements will execute.

* **Logic**: Because all three print statements share the exact same indentation level directly beneath the if statement, they form a single cohesive block of code.

**Q3: Ending a Conditional Block**

* **Question**: When you have multiple lines in an if block, how do you indicate the end of the if block?

* **Answer**: You de-indent the next line past the if block to the same level of indent as the original if statement.

* **Logic**: Returning to the previous indentation level signals to the Python interpreter that the conditional block has concluded.

**Q4: Invisible Indentation Errors**

* **Question**: You look at the following text:
    ```python
    if x == 6:
        print('Is 6')
        print('Is Still 6')
        print('Third 6')
  
It looks perfect but Python is giving you an 'Indentation Error' on the second print statement. What is the most likely reason?

* **Answer**: You have mixed tabs and spaces in the file.

* **Logic**: Python 3 is extremely strict about consistent indentation. Mixing spaces and tabs might look perfectly aligned in a text editor, but the interpreter reads them differently, causing an error.

### ⚖️ Section 2: Operators & Multi-Way Decisions
**Q5: Identifying Operators**

* **Question**: Which of these operators is not a comparison / logical operator? (>=, =, >, !=, ==)

* **Answer**: =

* **Logic**: The single = is the assignment operator (used to store a value in a variable). The double == is the comparison operator used to check for equality.

**Q6: Two-Way Decisions**

* **Question**: What is the Python reserved word that we use in two-way if tests to indicate the block of code that is to be executed if the logical test is false?

* **Answer**: else

* **Logic**: The if/else structure creates a fork in the road. The else block acts as the catch-all for any situation where the initial if condition evaluates to False.

**Q7: Reading Multi-Way Decisions**

* **Question**: What will the following code print out?
    ```python
    x = 0
    if x < 2:
        print('Small')
    elif x < 10:
        print('Medium')
    else:
        print('LARGE')
    print('All done') 
    ```
* **Answer**: Small All done

* **Logic**: Python evaluates if/elif structures top-to-bottom. Since 0 < 2 is True, it prints 'Small', completely skips the remaining elif and else blocks, and proceeds to the unindented 'All done'.

**Q8: Unreachable Code**

* **Question**: For the following code, what value of 'x' will cause 'Something else' to print out?
    ```python
    if x < 2:
        print('Small')
    elif x >= 2:
        print('Large')
    else:
        print('Something else')

* **Answer**: This code will never print 'Something else' regardless of the value for 'x'.

* **Logic**: Every possible number is either strictly less than 2, or greater than/equal to 2. Because those two conditions exhaust all mathematical possibilities, the else block is completely unreachable.

### 🛡️ Section 3: Handling Errors (try / except)
**Q9: Program Flow and Tracebacks**

* **Question**: In the following code (numbers added), which will be the last line to execute successfully?

    ```Python
    (1) astr = 'Hello Bob'
    (2) istr = int(astr)
    (3) print('First', istr)
    (4) astr = '123'
    (5) istr = int(astr)
    (6) print('Second', istr)

* **Answer**: 1

* **Logic**: Line 1 safely assigns a string. Line 2 attempts to convert the text 'Hello Bob' into an integer using int(). This triggers a traceback (ValueError) and stops the program immediately. Therefore, Line 1 is the last successful execution.

**Q10: The Safety Net**

* **Question**: For the following code, what will the value be for istr after this code executes?

    ```Python
    astr = 'Hello Bob'
    istr = 0
    try:
        istr = int(astr)
    except:
        istr = -1
  
* **Answer**: -1

* **Logic**: The try block attempts to convert 'Hello Bob' into an integer, which fails. Instead of crashing, the program catches the error and drops into the except block, safely reassigning istr to -1.