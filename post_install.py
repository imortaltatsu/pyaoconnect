#!/usr/bin/env python3
"""
Post-install script for pyaoconnect
This script runs after pip install to set up dependencies
"""

import os
import sys
import subprocess
import shutil

def run_command(command, cwd=None):
    """Run a command and return success status"""
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")
        print(f"Error: {e}")
        return False

def install_node_dependencies():
    """Install Node.js dependencies"""
    print("Installing Node.js dependencies...")
    
    # Check if Node.js is installed
    if not shutil.which('node'):
        print("ERROR: Node.js is not installed. Please install Node.js first.")
        print("   Download from: https://nodejs.org/")
        return False
    
    # Check if npm is available
    if not shutil.which('npm'):
        print("ERROR: npm is not installed. Please install npm first.")
        return False
    
    # Install @permaweb/aoconnect globally
    print("Installing @permaweb/aoconnect...")
    if not run_command("npm install -g @permaweb/aoconnect"):
        print("ERROR: Failed to install @permaweb/aoconnect")
        return False
    
    print("SUCCESS: Node.js dependencies installed successfully!")
    return True

def clone_aopy_connect():
    """Clone the aopy-connect repository if needed"""
    print("Setting up aopy-connect dependency...")
    
    # Check if git is available
    if not shutil.which('git'):
        print("ERROR: Git is not installed. Please install Git first.")
        return False
    
    # Clone the repository if it doesn't exist
    aopy_connect_dir = "aopy-connect"
    if not os.path.exists(aopy_connect_dir):
        print("Cloning aopy-connect repository...")
        if not run_command(f"git clone https://github.com/imortaltatsu/aopy-connect.git {aopy_connect_dir}"):
            print("ERROR: Failed to clone aopy-connect repository")
            return False
    
    # Install the aopy-connect package
    print("Installing aopy-connect package...")
    if not run_command("pip install -e ./aopy-connect"):
        print("ERROR: Failed to install aopy-connect package")
        return False
    
    print("SUCCESS: aopy-connect dependency set up successfully!")
    return True

def main():
    """Main post-install function"""
    print("Setting up pyaoconnect dependencies...")
    
    # Install Node.js dependencies
    if not install_node_dependencies():
        print("WARNING: Node.js dependencies not installed. Some features may not work.")
    
    # Clone and install aopy-connect
    if not clone_aopy_connect():
        print("WARNING: aopy-connect dependency not installed. Some features may not work.")
    
    print("SUCCESS: pyaoconnect installation completed!")
    print("NOTE: If you see any warnings above, please install the missing dependencies manually.")

if __name__ == "__main__":
    main()
