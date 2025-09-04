# 📊 Automated Payroll Management System (Oracle + PL/SQL + Flask)

## 📌 Overview
This project is an **Oracle-powered Payroll Management System** that automates salary processing for employees.  
It integrates **employee records, attendance, and leave data** to calculate **gross salary, tax, provident fund (PF) deductions, and net pay**.  
A **Flask-based web app** allows HR and employees to view real-time reports and download payslips.

---

## 🏗️ Features
- 👨‍💼 **Employee Management** – Store and manage employee details, salary structure, and department info.  
- ⏱️ **Attendance & Leave Tracking** – Maintain monthly attendance and leave records.  
- 💰 **Payroll Automation** – Compute salary, PF (12% of Basic), and Income Tax (slab-based).  
- 📑 **Payslip Generation** – Generate and view payslips via Flask web interface.  
- ⚡ **Oracle PL/SQL Packages** – Automates payroll runs at month-end.  
- 🔒 **Secure & Scalable** – Built on Oracle XE with reliable transaction control.  

---

## 🏛️ Tech Stack
- **Database:** Oracle XE (via Docker)  
- **Backend:** PL/SQL (Packages, Procedures, Functions, Triggers)  
- **Frontend:** Flask (Python) for reporting and payslip generation  
- **Deployment:** Docker + SQL Developer / DBeaver  

---

## ⚙️ Installation & Setup

### 1️⃣ Run Oracle XE in Docker
Create `docker-compose.yml`:
```yaml
version: '3'
services:
  oracle-db:
    image: gvenzl/oracle-xe:21-slim
    container_name: oracle-xe
    ports:
      - "1521:1521"
      - "5500:5500"
    environment:
      ORACLE_PASSWORD: payroll123
      APP_USER: payroll_user
      APP_USER_PASSWORD: payroll123
    volumes:
      - oracle-data:/opt/oracle/oradata
volumes:
  oracle-data:

1️⃣ Start the container

To launch the Oracle database container in the background, run the following command:

docker-compose up -d

2️⃣ Connect to Oracle

Once the container is running, connect to the database using sqlplus with the specified credentials:

docker exec -it oracle-xe sqlplus system/payroll123@//localhost:1521/XEPDB1

3️⃣ Initialize Database

Run the provided SQL scripts to set up the database schema and load initial data.

Run schema.sql to create the following tables:

employees

attendance

salary_runs

salary_details

Run seed.sql to insert sample employee data into the employees table.

4️⃣ Setup Flask App

To install the necessary dependencies and run the Flask web application, use the following commands:

pip install flask cx_Oracle

python app.py

After the app starts, you can visit the reporting dashboard at: http://127.0.0.1:5000

📂 Project Structure

The project is organized into the following file structure:

📦 payroll-system
 ┣ 📜 schema.sql          # Table definitions
 ┣ 📜 seed.sql            # Sample employee data
 ┣ 📜 payroll_pkg.sql     # PL/SQL package for salary, PF, tax
 ┣ 📜 app.py              # Flask web app for reporting
 ┣ 📂 templates/          # HTML templates (Jinja2)
 ┣ 📜 docker-compose.yml  # Docker container configuration
 ┗ 📜 README.md           # This documentation

🖥️ Usage Flow

HR inputs employee and attendance data into the system.

Run the monthly payroll calculation by executing the PL/SQL package with the desired month:

BEGIN
  payroll_pkg.run_monthly_payroll(p_month => '2025-09');
END;

The payroll results are automatically stored in the salary_details table.

The Flask app fetches and displays payslips and reports from the database.

📊 Sample Salary Calculation

The core salary calculation logic is based on the following formulas:

Gross Salary = Basic + HRA + DA

PF Deduction = 12% of Basic

Tax Deduction = As per Indian slabs (5%, 20%, 30%)

Net Salary = Gross – (PF + Tax)

🚀 Future Enhancements

PDF export for payslips

Role-based access (Admin/Employee login)

REST API for third-party integration (ERP/HRMS)

Configurable tax/PF rules in the database (instead of hardcoded)
