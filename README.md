# School-Performance-Analysis

This project is a a python school performance analysis database which stores ,mangaes and analyses student and teachers information.It stores teachers,students,classes,subjects,exams,scores and attendance data in tables .The information can then be analysed and then used to track a student attendance and scores across different subjects and provide a report on that.

## Features
 
 * ** Year group data  :** has a year group identification nmuber, a year group name and the academic year.

 * ** Teachers data :**  has a  teacher identification number ,their names and their specific department.

 * ** Student data :** has the student identification number, names,gender,date of birth and  year group identification number.

 * ** Attendance data :** has the attendance identification number,student identification,attendance date and the status.

 * ** Exams data :** has the examination identification number,subject identification number,exam name ,date and maximum score.

 * ** Score :** has the score ,student and exam identication numbers and the score out of 100.

 * ** Attendance data : ** has the attendance and student identification numbers,attendance date and status.

 * ** data frame : ** store the data above

 * ** plot : ** to visualise the different analysis done

### Technical Stack
* ** Language : ** Python 3
* ** Modules:** requests (Standard Library)
* ** Storage :** file system

### Prerequisites
* **  install python in to your computer 


### Installation and setup
**Clone the Repository:**

    ```bash
       git clone https://github.com/graceobonyo/School-Performance-Analysis/git
       cd School-Performance-Analysis
    ```

2.  **Run the program:**
    In the terminal pip install pandas,seaborn and  matplotlib
    Then execute the script:

    ```bash
    python main.ipynb 
    ```


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

main.ipynb        # Main project information

main.py           # Store project information

README.md         # Project information

csv files  # store the analysis done from the data in the tables 

## License

This project is open-source and available under the [MIT License] https://github.com/graceobonyo/School-Performance-Analysis/blob/main/LICENSE


Grace Obonyo :https://github.com/graceobonyo