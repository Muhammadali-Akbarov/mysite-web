from . install import setup_git
from . install import setup_linux_packages
from . install import setup_dependencies_migrations

from . database import setup_database


class AutoDeploymentProccess:
    def __call__(self):
        setup_linux_packages()
        setup_git()
        setup_database()
        setup_dependencies_migrations()


AutoDeploymentProccess()