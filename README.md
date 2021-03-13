# Code Nation Data Daemon Manager

## Usage
#### Manual Usage
```
$ pip install -r requirements.txt
$ python course-util.py
```
Once app has completed data collection, converted version will be available as grades.csv

#### Automatic Usage
Script will auto-run Thursdays at 8:00 pm PST
`grades.csv` is batched into sheets by class
`grades_1.csv`, `grades_2.csv`, …, `grades_n.csv` will be imported into [this spreadsheet](https://docs.google.com/spreadsheets/d/19zeDtQOfzGAkhrl6fcX23E1D3_3_wSVFFzvMk6Sn6a8/edit#gid=1528347903).


## Purpose & Functionality
This tool extracts student grades from google classroom automatically. The application interfaces with the Google Classroom API to function as a scraper, working around Google’s missing rubric functionality within the Classroom API.

Student grades are scraped from the HTML of graded project rubrics, using standard API-accessible data from Google Classroom to index each individual submission, then navigate a browser to the submission & scrape grade data. The data hierarchy is as follows, with available identifiers within each json response listed:

- Course [courseId]
  - Coursework [courseworkId][courseId]
    - Submission [submissionId] [courseworkId][userId]
  - Student [userId]
  - Teacher [userId]

In order for the Daemon to sort between project and non-project assignments, each assignment containing graded rubrics must have the word “Project” in its title. **The Daemon will skip over any assignments that do not have “Project” in the title.** Additionally, the **assignments must be listed as “Graded”** within the classroom system. Without this designation, the tool will regard all submissions as ungraded and they will not be scraped (the exclusion of ungraded projects is for tool optimization). **If the assignment is categorized as “ungraded”, all submissions for the project will be indexed as “ungraded”, causing the tool to skip over them.**

Additionally, the application automatically uploads data to the [Program Data Tracker](https://docs.google.com/spreadsheets/d/19zeDtQOfzGAkhrl6fcX23E1D3_3_wSVFFzvMk6Sn6a8/edit#gid=2088638832) upon completion of data collection. This export is batched into separate sheets by program name in order to reduce the computational load of each raw data set.


## App Flow

###### `course_util.py`
- Creates Google API Client service, authorized to interface with Classroom & Sheets
- Iteratively creates batch requests to Classroom API
- Iteratively adds courses, teachers, students, courseworks, and submissions to batch requests
- Sends batch http requests, returns json-formatted data via ‘find_except.py’
- Sends processed json to ‘extract_data.py’
- Sends extracted data to ‘to_csv.py’ for final conversion

###### `extract_data.py`
- Uses ‘page_util.py’ to login to Google (within ‘page_util.py’, ‘noviz.py’ is used to create a headless instance of chrome) via Selenium
- Saves raw login credentials
- Generates regex for reading Rubric html or Submission html dependent on usage
- Uses generated regex to scrape key values in page html, via Selenium
- Returns json-formatted rubric or submission object dependent on use case

###### `to_csv.py`
- Reads raw json data & processes to a csv file of all submitted & graded student project work
- Writes csv file as ‘grades.csv’


## Admin / Maintenance Responsibilities

#### Responsibilities
- Ensure application runs as intended according to schedule. Report any issues to [human]
- Manage minor bugfixes, including small technical tweaks in encoding, batching, and data sources/destinations. This excludes major bugs such as logic errors, tool deprecation, and other large-scope issues.
- Describe & document large-scope issues for the Programs Data Team
- Work with Programs Data Team to ensure the application is producing expected results

#### Skills
- Unix terminal fluency
- Experience working with Python and common Python libraries (such as pandas, selenium, json, csv, etc.)
- Basic knowledge of web development & webpage structure (html, css, js) + ability to identify key pieces of webpage code
- Git version control
- Strong written skills / experience documenting & reporting errors in code
- Experience working with Google APIs / Google cloud and/or experience writing scrapers using industry standard tools (Selenium, Puppeteer, Chef, etc.) is a major plus
