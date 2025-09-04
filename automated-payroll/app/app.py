from flask import Flask, render_template, request
import oracledb

app = Flask(__name__)

DB_CONFIG = {
    'user': 'PAYROLL',
    'password': 'your_password',
    'dsn': 'localhost/XEPDB1'
}

def get_connection():
    return oracledb.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('report.html')

@app.route('/payslip')
def payslip():
    emp_code = request.args.get('emp_code')
    month = request.args.get('month')
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT sd.gross_salary, sd.total_deductions, sd.net_salary, sd.tax, sd.pf,
               e.emp_code, e.first_name, e.last_name, sr.run_month
        FROM salary_details sd
        JOIN employees e ON sd.emp_id = e.emp_id
        JOIN salary_runs sr ON sd.run_id = sr.run_id
        WHERE e.emp_code = :1 AND sr.run_month = :2
    ''', [emp_code, month])
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return f'No payslip found for {emp_code} for {month}', 404

    data = {
        'emp_code': row[5],
        'name': f"{row[6]} {row[7]}",
        'month': row[8],
        'gross': float(row[0]),
        'deductions': float(row[1]),
        'net': float(row[2]),
        'tax': float(row[3]),
        'pf': float(row[4])
    }
    return render_template('payslip.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
