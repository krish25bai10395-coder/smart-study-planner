Smart Study Planner
A Python-based productivity and performance tracking system for students.
📌 Project Overview
Smart Study Planner is a data-driven academic management system built using Python.
It helps students track study hours, manage subject-wise scores, and visualize academic performance using graphical insights.
This project demonstrates practical implementation of:
Data handling using CSV files
Data analysis using Pandas
Data visualization using Matplotlib
Version control using Git & GitHub
🎯 Objectives
Develop a structured study tracking system
Store academic performance in CSV format.
Analyze subject-wise scores.
Monitor daily study hours.
Generate graphical performance reports.
Improve time management using data insights.
🛠️ Tech Stack
Category
Technology
Programming Language
Python 3.x
Data Processing
Pandas
Visualization
Matplotlib
Data Storage
CSV Files
Version Control
Git
Repository Hosting
GitHub
📂 Project Structure

smart-study-planner/
│
├── data/
│   ├── scores.csv
│   └── study_log.csv
│
├── main.py
├── requirements.txt
└── README.md
Dataset Details
1️⃣ scores.csv
Stores subject-wise marks.
Example:

Name,Subject,Score
Krish,Maths,85
Krish,Physics,78
Krish,Chemistry,88
Krish,English,90
Krish,Computer,95
2️⃣ study_log.csv
Stores daily study hours.
Example:

Date,Subject,Hours
2026-03-20,Maths,2
2026-03-21,Physics,1.5
2026-03-22,Chemistry,2
2026-03-23,English,1
2026-03-24,Computer,3
⚙️ Installation & Setup
Step 1: Install Python
Download and install Python from: https://www.python.org/downloads/⁠�
Step 2: Clone the Repository
Bash
git clone https://github.com/krish25bai10395-coder/smart-study-planner.git
cd smart-study-planner
Step 3: Install Required Libraries
Bash
pip install -r requirements.txt
Or manually:
Bash
pip install pandas matplotlib
Step 4: Run the Project
Bash
python main.py
🧠 Working Mechanism
Reads CSV files using Pandas.
Calculates:
Average score
Total study hours
Groups study hours subject-wise.
Displays bar chart visualization.
Provides performance insights in console output.
📈 Sample Output
Console Output:

Average Score: 87.2
Total Study Hours: 9.5
Graph Output:
Bar chart showing study hours per subject.
🔍 Key Features
✔ Subject-wise performance tracking
✔ Study time analysis
✔ Automatic average calculation
✔ Graphical representation of data
✔ Easy CSV data management
✔ Beginner-friendly structure
📌 Advantages
Improves productivity
Encourages disciplined study habits
Simple and lightweight
No database required
Easy to extend and modify
⚠️ Limitations
No graphical user interface (GUI)
Single-user system
CSV-based storage (not secure for large systems)
🚀 Future Enhancements
Add Tkinter GUI
Add login authentication system
Add progress percentage tracker
Convert into web application using Flask
Connect to SQL database
Add AI-based study recommendations
📚 Learning Outcomes
Through this project, the following concepts are applied:
File handling in Python
DataFrame operations
Data aggregation
Data visualization
Git version control workflow
Real-world project structuring
🧪 Requirements

Python 3.x
pandas
matplotlib
📖 References
Python Documentation – https://docs.python.org/3/⁠�
Pandas Documentation – https://pandas.pydata.org/docs/⁠�
Matplotlib Documentation – https://matplotlib.org/⁠�
Git Documentation – https://git-scm.com/docs⁠�
GitHub Guides – https://guides.github.com/⁠�
W3Schools Python Tutorial – https://www.w3schools.com/python/⁠�
GeeksforGeeks Python – https://www.geeksforgeeks.org/python-programming-language/⁠�
👨‍💻 Author
Krish Kumar
B.Tech Student
Smart Study Planner Project – 2026
