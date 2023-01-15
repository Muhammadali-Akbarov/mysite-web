import subprocess


def setup_linux_packages():
    subprocess.run(["sudo","apt ","update"])
    subprocess.run(["sudo","apt","install","python3-venv", "python3-dev", "postgresql", "postgresql-contrib", "nginx", "curl"])


def setup_git():
    # Clone repository
    subprocess.run(["cd"])
    subprocess(["git", "clone", "git@github.com:Muhammadali-Akbarov/mysite-web.git"])
    subprocess(["mv", "mysite-web", "mysite"])
    subprocess(["cd", "mysite"])


def setup_dependencies_migrations():
    # Install dependencies
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

    # Apply database migrations
    subprocess.run(["python", "manage.py", "migrate"])

    # Collect static files
    subprocess.run(["python", "manage.py", "collectstatic", "--noinput"])

