# School-Performance-Analysis

This project is a DB sqllite school performance analysis database which stores ,mangaes and analyses student and teachers information.It stores teachers,students,classes,subjects,exams,scores and attendance data in tables .The information can then be analysed and then used to track a student attendance and scores across different subjects and provide a report on that.

## Features
 
 * ** Year group data  :** has a year group identification nmuber, a year group name and the academic year.

 * ** Teachers data :**  has a  teacher identification number ,their names and their specific department.

 * ** Student data :** has the student identification number, names,gender,date of birth and  year group identification number.

 * ** Attendance data :** has the attendance identification number,student identification,attendance date and the status.

 * ** Exams data :** has the examination identification number,subject identification number,exam name ,date and maximum score.

 * ** Score :** has the score ,student and exam identication numbers and the score out of 100.

 * ** Attendance data : ** has the attendance and student identification numbers,attendance date and status.

## Technical Stack
* ** Language : ** SQL
* ** Storage :DB Browser for SQL lite
* ** Storage :** file system

### Prerequisites
* **  Install DB Browser for sql lite in your computer 


### Installation and setup

Open the DB Browser for sql lite.

Click on new database add a new file school_performance and save.

Copy and paste the querries from peformance.py file and paste them into the execute SQL and run the querries.

To save the file as csv click on the top left file tab then sccroll down to export then click to csv file ,then choose the table ,and write your file name and save .


## Contributing

Contributions are what make the open-source community an excellent place to learn, inspire, and create. Any contributions you make are welcomed.

### How to Contribute

**Fork the Project**

**Create your Feature Branch**
    ```bash
    git checkout -b feature/AmazingFeature
    ```

**Commit your Changes**
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```

**Push to the Branch**
    ```bash
    git push origin feature/AmazingFeature
    ```

**Open a Pull Request**


### Areas for Improvement

  * Use streamlit to visualise the database.
  * Use a dashboard to visualise comparison.
  * Incorpotrate authentification for more security
  
  
## Project Structure

text

main.ipynb            # Main project information

README.md          # Project information

csv files  # store the analysis done from the data in the tables 

## License

This project is open-source and available under the [MIT License] https://github.com/graceobonyo/School-Performance-Analysis/blob/main/LICENSE


Grace Obonyo :https://github.com/graceobonyo