# Healthcare-Information-Management-System

__Healthcare Information Management System (HIMS) is an application created for Software Engineering course. The __HIMS__ application can be used by hospitals, clinics and healthcare centres to manage data/records for patients, doctors, prescriptions, medical tests and various departments within the healthcare facility. 

The application uses sqlite3 module for database management purposes, streamlit to create the user interface and make the application work, and pandas to facilitate working with the data.

### Requirements

* __Python 3.7.4__ or any higher version
* __pandas__ and __streamlit__
  * To install the packages mentioned above, go to command prompt/terminal and execute the following commands:
  ```cmd
  > pip install pandas
  > pip install streamlit
  ```

## Instructions to run the application

1. Clone this repository to your local system.
2. After cloning this repository to your local system, create a __config.py__ file in the same repository.
3. Add the following Python statements to __config.py__ :
  ```
  password = '<user_authentication_password>'                               
  database_name = '<current_database_name>'                                 
  edit_mode_password = '<edit_mode_password>'                               
  dr_mls_access_code = '<doctor_or_medical_lab_scientist_access_code>'     
  ```
4. Move to the same directory in command prompt/terminal and execute the following command (running this command will open the application in a new tab in your default browser automatically; you don't need internet connection to work with this application):
> streamlit run hims_app.py



