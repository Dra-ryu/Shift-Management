# Shift Management Tool
#### Video Demo:  <https://youtu.be/-ron83BVvT4>
#### Description:

## Summary: This web application is to record workers's working hours automatically and manage those information easily

## Background

    - In my workplace, we manage working hours by hand, so it is waste of time.
    - If we can register working hours and manage them automatically, we can save time.
    - Therefore, I decided to develop automatic management tool of working hours

## Function

    1. Register
        - Users can register your account with "username" and "password".
        - For user's safety, passwords are recorded as hushed password.
        - Same username cannot be registered.
        - If users don't input same password in "password" and "confirmation", register process will be rejected.
        - Every infomation is recorded in database(shift.db).
    2. Login
        - Users can login with username and password.
        - If either username or password are wrong, users should input them again.
        - Manager can login to a manager's page with specific username and password.
    3. Record Time
        - What users should do is to press buttons.
        - Users can record time when they attend, leave workplace.
        - Besides, users can record time when they start or finish taking a break.
        - Every data is recorded when user press buttons automatically.
        - With the bottommost button, you can calculate working hours.
    4. Calculate
        - When the calculate button is pressed, working hours is calculated automatically.
        - Working hours is calculated with this equation; working hours = leave_time - attendance_time - (break_end - break_start)
        - Working hours are recorded to the database as “sum_time”.
        - Users can get working hours of any date.
        - If some data don’t exist, total working hours cannot be calculated.
    5. Download Excel File
        - Only manager can download chart about working hours of each workers.
        - This excel file contains “username”, "date", “attendance_time”, “break_start”, ”break_end”, “sum_time”.
        - Every data is sorted by username.
        - Manager can get charts of any days, so it is convenient to manage working hours day by day.
## Roles of each files

    -"attendance.html", "break-start.html", "break-end.html", "leave.html"：To show time when each buttons are pressed
    -"attendance.py"：This python file implements every functions. For example, inputting data to a database, routing, calculating total working hours, downloading excel file. As a library, I used flask. In order to implement a function to download excel, I imported openpyxl.
    -"styles.css"：This css file arranges user interface. I used bootstrap to make buttons beautiful.
    -"register-again-username", "register-again-password.html"：To show notice if user input wrong username or password to register their account. Color of notice is red, so it is outstanding.
    -"login-agein.html"：To show notice if user input wrong username or password to login
    -"working_hours.html"：To show total working hours when "caliculate button" is pressed
    -"management.html"：To download exvel file.
    -"shift.db"：Database about user's information and working hours

## Future tasks

    - Function to correct records if users input wrong information
    - To make user interface better for mobile users
    - To implement function to calculate salaries automatically
    - To add information about worker’s categories, for example Sales, Manager, Office workers. It will be more convenient to manage working hours and salaries by each working sections.


