import subprocess
from src.logger import setup_logging

logger = setup_logging(__name__)


def run_bash_script(dry_run=True):
    command = ["bash", "scripts/install_nginx.sh"]
    try:
        if dry_run:
            logger.info(f"[DRY-RUN] Would run {" ".join(command)}")
        else:
            subprocess.run(command, check=True)
            logger.info("Nginx installation completed")
    except subprocess.CalledProcessError as e:
        logger.error(f"Nginx installation failed: {e}")