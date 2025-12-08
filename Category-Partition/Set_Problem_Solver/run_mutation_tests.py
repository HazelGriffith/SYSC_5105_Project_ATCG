import subprocess
import json
import os

def run_mutmut():
    print("Running mutation tests...")
    subprocess.run(["mutmut", "run"], check=False)

def load_survivors():
    result = subprocess.run(
        ["mutmut", "json"],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout)
    return data

def save_reports(data):
    with open("mutation_report.json", "w") as f:
        json.dump(data, f, indent=4)

    with open("mutation_report.txt", "w") as f:
        for item in data.get("survived_mutants", []):
            f.write(f"{item}\n")

def main():
    run_mutmut()
    data = load_survivors()
    save_reports(data)

    survivors = data.get("survived_mutants", [])
    print(f"Survived mutants: {len(survivors)}")
    if survivors:
        print("You need to strengthen tests to kill these mutants!")

if __name__ == "__main__":
    main()
