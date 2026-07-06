import subprocess
import sys
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Scripts to execute
scripts = [
    BASE_DIR / "data_ingestion.py",
    BASE_DIR / "data_cleaning.py",
    BASE_DIR / "scripts" / "compute_metrics.py"
]

print("Starting ETL Pipeline...\n")

for script in scripts:
    print(f"Running: {script.name}")
    result = subprocess.run([sys.executable, str(script)])

    if result.returncode != 0:
        print(f"\nError while running {script.name}")
        sys.exit(1)

print("\n✅ ETL Pipeline completed successfully!")