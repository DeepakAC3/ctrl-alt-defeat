import streamlit as st
import pymysql

# Function to create database connection
def create_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 database='finance',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

# Function to create table if not exists
def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      username VARCHAR(50) UNIQUE,
                      password VARCHAR(50),
                      email VARCHAR(50))''')
    connection.commit()
    connection.close()

# Function to insert user details into database
def insert_user(username, password, email):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                   (username, password, email))
    connection.commit()
    connection.close()
    
# Function to authenticate user
def authenticate_user(username, password):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    connection.close()
    return user

# Main function to run the Streamlit app
def main():
    st.title("Login Page with Registration")

    # Create table if not exists
    create_table()

    # Display login form
    login = st.form(key='login_form')
    login.write("## Login")
    username_login = login.text_input("Username")
    password_login = login.text_input("Password", type='password')
    submit_login = login.form_submit_button("Login")

    if submit_login:
        user = authenticate_user(username_login, password_login)
        if user:
            st.success(f"Welcome back, {user['username']}!")
        else:
            st.error("Invalid username or password.")

    # Display registration form
    registration = st.form(key='registration_form')
    registration.write("## Register")
    username_reg = registration.text_input("Username")
    password_reg = registration.text_input("Password", type='password')
    email_reg = registration.text_input("Email")
    submit_reg = registration.form_submit_button("Register")

    if submit_reg:
        insert_user(username_reg, password_reg, email_reg)
        st.success("Registration successful! You can now login.")

if __name__ == '__main__':
    main()