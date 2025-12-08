import os
import subprocess
import json
from textwrap import dedent

# --------------------------------------------------
# 1. Define mutation operators
# --------------------------------------------------
MUTATIONS = [
    {
        "name": "disc_lt_to_leq",
        "description": "Change discriminant < 0 to <= 0 (affects complex vs real root boundary).",
        "old": "if (discriminant < 0):",
        "new": "if (discriminant <= 0):",
    },
    {
        "name": "disc_lt_to_gt",
        "description": "Change discriminant < 0 to > 0 (inverts complex/real branch).",
        "old": "if (discriminant < 0):",
        "new": "if (discriminant > 0):",
    },
    {
        "name": "overflow_eq_to_neq",
        "description": "Change discriminant == b*b to discriminant != b*b in overflow check.",
        "old": "if (math.isnan(discriminant) or discriminant == b*b):",
        "new": "if (math.isnan(discriminant) or discriminant != b*b):",
    },
    {
        "name": "sign_gt_to_ge",
        "description": "Change sign(b): >0 to >=0, so b==0 treated as positive.",
        "old": "return 1 if (b > 0) else -1",
        "new": "return 1 if (b >= 0) else -1",
    },
]


SOURCE_FILE = "quadratic_equation_solver.py"
REPORT_FILE = "mutation_report.json"


# --------------------------------------------------
# 2. Utility: run pytest and return if mutant is killed
# --------------------------------------------------
def run_tests() -> bool:
    """
    Runs pytest in the current project directory.
    Returns True if tests FAIL (mutant killed),
    False if tests PASS (mutant survived).
    """
    print("  -> Running pytest on mutant...")
    completed = subprocess.run(
        ["pytest", "-q"],  # -q for quiet; remove if you want full output
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    killed = completed.returncode != 0
    if killed:
        print("  -> Mutant KILLED (tests failed)")
    else:
        print("  -> Mutant SURVIVED (tests passed)")

    # Optional: write raw pytest output per mutant
    with open("last_mutant_pytest_output.txt", "w", encoding="utf-8") as f:
        f.write(completed.stdout)

    return killed


# --------------------------------------------------
# 3. Main mutation runner
# --------------------------------------------------
def main():
    if not os.path.exists(SOURCE_FILE):
        raise FileNotFoundError(f"Could not find {SOURCE_FILE} in current directory.")

    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        original_source = f.read()

    results = []

    print("Starting mutation testing...")
    print(f"Source file: {SOURCE_FILE}")
    print(f"Number of mutation operators: {len(MUTATIONS)}")
    print("-" * 60)

    mutant_index = 0

    for mutation in MUTATIONS:
        old = mutation["old"]
        new = mutation["new"]

        if old not in original_source:
            print(f"Skipping mutation '{mutation['name']}' - pattern not found in source.")
            continue

        mutant_index += 1
        print(f"\nApplying mutant #{mutant_index}: {mutation['name']}")
        print(f"  Description: {mutation['description']}")

        # Create mutated version: replace only first occurrence
        mutated_source = original_source.replace(old, new, 1)

        # Backup original, write mutant, run tests, then restore
        try:
            with open(SOURCE_FILE, "w", encoding="utf-8") as f:
                f.write(mutated_source)

            killed = run_tests()

            results.append(
                {
                    "id": mutant_index,
                    "name": mutation["name"],
                    "description": mutation["description"],
                    "killed": killed,
                    "old": old,
                    "new": new,
                }
            )

        finally:
            # Always restore original file
            with open(SOURCE_FILE, "w", encoding="utf-8") as f:
                f.write(original_source)

    # --------------------------------------------------
    # 4. Compute mutation score and save report
    # --------------------------------------------------
    total = len(results)
    killed_count = sum(1 for r in results if r["killed"])
    survived_count = total - killed_count
    score = (killed_count / total * 100.0) if total > 0 else 0.0

    summary = {
        "total_mutants": total,
        "killed": killed_count,
        "survived": survived_count,
        "mutation_score": score,
        "mutants": results,
    }

    print("\n" + "=" * 60)
    print("MUTATION TESTING SUMMARY")
    print(f"Total mutants:   {total}")
    print(f"Killed mutants:  {killed_count}")
    print(f"Survived mutants:{survived_count}")
    print(f"Mutation score:  {score:.2f}%")
    print("=" * 60)

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)

    print(f"\nDetailed mutation report written to: {REPORT_FILE}")

    TXT_REPORT = "mutation_report.txt"

    with open(TXT_REPORT, "w", encoding="utf-8") as txt:

        txt.write("====== MUTATION TEST SUMMARY ======\n")
        txt.write(f"Total mutants generated: {total}\n")
        txt.write(f"Mutants killed:          {killed_count}\n")
        txt.write(f"Mutants survived:        {survived_count}\n")
        txt.write(f"Mutation Score:          {score:.2f}%\n\n")

        txt.write("====== MUTANT DETAILS ======\n")
        for r in results:
            status = "KILLED" if r["killed"] else "SURVIVED"
            txt.write(f"\n[{status}] {r['name']}\n")
            txt.write(f"  Description: {r['description']}\n")
            txt.write(f"  Old: {r['old']}\n")
            txt.write(f"  New: {r['new']}\n")

    print(f"\nTXT summary saved to: {TXT_REPORT}")
    print(f"JSON summary saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
