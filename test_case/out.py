import os
import subprocess
# coding=utf-8

def generate_allure_report():

    current_dir = os.path.dirname(os.path.abspath(__file__))

    results_dir = os.path.join(current_dir, 'allure_results')
    report_dir = os.path.join(current_dir, 'allure_report')
    print(f'results_dir={results_dir}')
    print(f'report_dir={report_dir}')
    pytest_command = f'pytest --alluredir={results_dir} --clean-alluredir'
    subprocess.run(pytest_command, shell=True)

    generate_command = f'allure generate --clean {results_dir} -o {report_dir}'
    subprocess.run(generate_command, shell=True)

    serve_command = f'allure serve {report_dir}'
    subprocess.run(serve_command, shell=True)


if __name__ == '__main__':
    generate_allure_report()