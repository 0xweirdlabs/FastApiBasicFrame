import os
import sys
from uvicorn import run

def main():
    env = sys.argv[1] if len(sys.argv) > 1 else "local"
    os.environ["ENV"] = env

    if env == "local":
        os.environ["ENVIRONMENT"] = "Local Environment"
        os.environ["DATABASE_URL"] = "sqlite:///./local.db"
    elif env == "dev":
        os.environ["ENVIRONMENT"] = "Development Environment"
        os.environ["DATABASE_URL"] = "postgresql://user:password@localhost/dev_db"
    elif env == "prod":
        os.environ["ENVIRONMENT"] = "Production Environment"
        os.environ["DATABASE_URL"] = "postgresql://user:password@localhost/prod_db"
    else:
        raise ValueError(f"Unknown environment: {env}")

    run("src.fastapibasic.main:app", host="0.0.0.0", port=8000, reload=(env != "prod"))

if __name__ == "__main__":
    main()
