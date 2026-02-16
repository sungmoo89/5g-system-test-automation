import os

def run():
    print("Starting System Test Execution...")

    os.system("pytest -s -v --html=reports/report.html")

    print("Test execution completed.")
    print("Report generated: reports/report.html")

if __name__ == "__main__":
    run()
