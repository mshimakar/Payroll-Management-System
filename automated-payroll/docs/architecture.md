# Architecture

This system consists of:
- Oracle DB schema with `employees`, `attendance`, `leaves`, `salary_runs`, `salary_details`.
- PL/SQL package `payroll.pkg_payroll` that calculates monthly payroll.
- Flask reporting application for payslips and basic reports.

## Data Flow
1. HR maintains employees and attendance.
2. Monthly run inserts a row in `salary_runs` and details into `salary_details`.
3. Flask app queries joined tables to render payslips.

## Security
- Use least-privilege DB user for the app.
- Externalize secrets (env vars) in production.
