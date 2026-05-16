"""
Reusable Python package installer utility
with detailed timestamp logging.

Features
--------
1. Install package if missing
2. Install specific version if requested
3. Skip installation if correct version already exists
4. Detailed timestamp logs

NOTE
----
This script DOES NOT perform package upgrades.
"""

import sys
import subprocess

from datetime import datetime
from importlib.metadata import (
    version,
    PackageNotFoundError
)


# -------------------------------------------------------------
# LOGGING FUNCTION
# -------------------------------------------------------------
def log(message):
    """
    Print log message with timestamp.

    Format
    ------
    DD-MMM-YYYY HH:MM:SS AM/PM
    """

    timestamp = datetime.now().strftime(
        "%d-%b-%Y %I:%M:%S %p"
    )

    print(f"[{timestamp}] {message}")


def upgrade_pip():
    """
    Upgrade pip to latest version before installing any packages.

    Why this matters
    -----------------
    - Prevents build failures
    - Ensures latest wheel support
    - Avoids old resolver issues
    """

    log("Checking pip upgrade availability...")

    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "--upgrade",
        "pip"
    ])

    log("pip upgrade completed successfully")
# -------------------------------------------------------------
# RUN TERMINAL COMMAND
# -------------------------------------------------------------
def run_command(command):
    """
    Execute terminal command.

    Parameters
    ----------
    command : list
        Terminal command list
    """

    log(f"Executing command: {' '.join(command)}")

    result = subprocess.run(
        command,
        text=True,
        capture_output=True
    )

    if result.returncode != 0:

        log("Command execution failed")

        log(
            f"Error details: "
            f"{result.stderr.strip()}"
        )

        raise Exception(result.stderr)

    log("Command executed successfully")

    return result.stdout.strip()


# -------------------------------------------------------------
# PACKAGE DETAILS
# -------------------------------------------------------------
def get_package_details(package_string):
    """
    Extract package name and version.

    Examples
    --------
    requests
        -> ("requests", None)

    numpy==1.26.4
        -> ("numpy", "1.26.4")
    """

    if "==" in package_string:

        package_name, required_version = (
            package_string.split("==")
        )

        return (
            package_name.strip(),
            required_version.strip()
        )

    return package_string.strip(), None


# -------------------------------------------------------------
# INSTALL PACKAGE
# -------------------------------------------------------------
def install_package(package_string):
    """
    Install package using pip.
    """

    log(
        f"Starting installation for package: "
        f"{package_string}"
    )

    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        package_string
    ])

    log(
        f"Package installation completed: "
        f"{package_string}"
    )


# -------------------------------------------------------------
# MAIN VALIDATION FUNCTION
# -------------------------------------------------------------
def ensure_package(package_string):
    """
    Ensure package exists with requested version.

    Parameters
    ----------
    package_string : str

    Examples
    --------
    requests

    numpy==1.26.4
    """

    package_name, required_version = (
        get_package_details(package_string)
    )

    log("=" * 70)

    log(
        f"Started processing package: "
        f"{package_name}"
    )

    # ---------------------------------------------------------
    # STEP 1:
    # Check installed version
    # ---------------------------------------------------------
    try:

        installed_version = version(package_name)

        log(
            f"Installed package version found: "
            f"{installed_version}"
        )

    except PackageNotFoundError:

        log(
            f"Package not installed: "
            f"{package_name}"
        )

        install_package(package_string)

        log(
            f"Package installed successfully: "
            f"{package_string}"
        )

        log("=" * 70)

        return

    # ---------------------------------------------------------
    # STEP 2:
    # Handle specific version request
    # ---------------------------------------------------------
    if required_version:

        log(
            f"Requested package version: "
            f"{required_version}"
        )

        if installed_version != required_version:

            log(
                "Installed version does not match "
                "requested version"
            )

            log(
                f"Installed version: "
                f"{installed_version}"
            )

            log(
                f"Required version : "
                f"{required_version}"
            )

            install_package(
                f"{package_name}=={required_version}"
            )

            log(
                "Requested package version "
                "installed successfully"
            )

        else:

            log(
                "Requested package version "
                "already installed"
            )

    # ---------------------------------------------------------
    # STEP 3:
    # No version specified
    # ---------------------------------------------------------
    else:

        log(
            "Package already installed "
            "and no version specified"
        )

    log(
        f"Completed processing package: "
        f"{package_name}"
    )

    log("=" * 70)