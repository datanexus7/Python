from package_manager import (
    ensure_package,
    log,
    upgrade_pip
)

# -------------------------------------------------------------
# START SCRIPT
# -------------------------------------------------------------
log("Starting package installation process")

# 🔥 IMPORTANT: upgrade pip first
upgrade_pip()

log("Proceeding with package installations")
log("=" * 70)


packages = [
    "requests",
    "numpy>=1.3.2",
    "pandas",
    "flask~=3.1"
    '''
        So for flask, pip will pick:
        
        3.1.0
        3.1.1
        3.1.x (latest in 3.1 series)
        
        ❌ It will NOT install:
        
        3.2.0
        4.x.x
    '''
]

for package in packages:
    ensure_package(package)

log("All packages processed successfully")