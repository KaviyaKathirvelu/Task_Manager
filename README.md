# Task_Manager

Task Manager App (MicroSaaS)

**Project Description**
The Task Manager App is a simple, efficient web application designed to help users manage their tasks and improve productivity. It allows users to add, update, delete, and view their tasks in a clean, user-friendly interface. This app has been developed using Flask as the backend framework and deployed on AWS Elastic Beanstalk for easy scalability and management.

The app is built with simplicity in mind and is perfect for individuals or small teams looking for a quick and effective way to manage their daily tasks.

**Setup Instructions**
**Prerequisites:**  <br>
--- Python 3.x installed on your local machine.<br>
--- Pip for installing dependencies.<br>
--- AWS Account (for deploying the app to Elastic Beanstalk).<br>

**Steps to Run Locally:**
1. Clone the repository:
Copy code
>> git clone https://github.com/yourusername/task-manager-flask.git<br>
>> cd task-manager-flask

2. Set up a virtual environment:
Copy code
>> python3 -m venv venv<br>
>> source venv/bin/activate  # On Windows: venv\Scripts\activate<br>

3. Install dependencies:
Copy code
>> pip install -r requirements.txt

4. Run the Flask app:
Copy code
>> flask run
Your app should now be running at http://127.0.0.1:5000/.

**Deployment on AWS Elastic Beanstalk:**

-Log in to the Elastic Beanstalk console.<br>
-Create a new application and environment (choose Python as the platform).<br>
-Upload the source bundle (your .zip file containing the project).<br>
-Click on "Create environment" and Elastic Beanstalk will handle the deployment automatically.<br>
-Once the environment is ready, you can access your app via the provided URL.<br>

**Features Overview**
Task Management: Users can add, view, update, and delete tasks.<br>
User Interface: A simple and intuitive UI to manage tasks effectively.<br>
Cloud Hosting: Deployed on AWS Elastic Beanstalk for easy management and scalability.<br>
Persistence: All tasks are saved in the database for persistence across sessions.<br>

**Screenshots**
![image](https://github.com/user-attachments/assets/fbd1b3f6-615c-47ac-a241-df5207dc5d00)
![image](https://github.com/user-attachments/assets/5e812c1b-df11-4684-ad10-3d65369816a1)



**Basic Implementation Details:**  <br>

This Task Manager app is built using Flask (a lightweight Python web framework). The backend handles user requests and serves data through HTTP routes, and the frontend is rendered using HTML templates. The app uses an SQLite database to persist the tasks.

**Technologies Used:**  <br>

-- Flask: For creating the web application and routing.<br>
-- AWS Elastic Beanstalk: For deploying the app on the cloud.<br>
-- SQLite: For storing task data.<br>
-- HTML/CSS: For creating a user-friendly frontend.<br>

**Conclusion**  <br>
This project demonstrates how to build a simple web app using Flask and deploy it on AWS Elastic Beanstalk. The Task Manager app can be expanded further by adding features such as user authentication, reminders, or integrations with other productivity tools.

