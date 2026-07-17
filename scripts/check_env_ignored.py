import subprocess
import sys

result = subprocess.run(["git", "check-ignore", "-q", ".env"], capture_output=True)
if result.returncode != 0:
    print("ERROR: .env is not ignored by git. Add it to .gitignore before committing.")
    sys.exit(1)
print(".env is ignored by git.")
