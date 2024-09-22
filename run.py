import os
import subprocess
import signal
import sys
from dotenv import load_dotenv

load_dotenv()

def run_frontend(mode):
    # os.chdir("frontend")
    if mode == "dev":
        subprocess.Popen(["npm", "run", "dev"])
    elif mode == "build":
        subprocess.run(["npm", "run", "build"])
    # os.chdir("..")

def run_backend(mode):
    # os.chdir("backend")
    env = os.environ.copy()
    env["ENV"] = mode
    subprocess.Popen(["uvicorn", "main:app", "--reload", "--port", "8000"], env=env)
    # os.chdir("..")

def main():
    if len(sys.argv) < 2:
        print("Usage: python run.py [dev|prod]")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "dev":
        os.environ["ENV"] = "development"
        run_frontend(mode)
        run_backend(mode)
    elif mode == "prod":
        os.environ["ENV"] = "production"
        run_frontend("build")
        run_backend(mode)
    else:
        print("Invalid mode. Use 'dev' or 'prod'.")
        sys.exit(1)

    try:
        signal.pause()
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()