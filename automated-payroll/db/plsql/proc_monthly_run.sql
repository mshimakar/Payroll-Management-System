-- Optional wrapper procedure for convenience
CREATE OR REPLACE PROCEDURE payroll.proc_monthly_run(p_month VARCHAR2, p_user VARCHAR2 DEFAULT 'system') AS
BEGIN
  payroll.pkg_payroll.RUN_MONTHLY_PAYROLL(p_month => p_month, p_created_by => p_user);
END;
/
