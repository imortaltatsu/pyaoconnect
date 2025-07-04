#!/usr/bin/env python3
"""
Setup script for pyaoconnect - Super Simple AO Connect
"""

import os
import sys
import subprocess
import shutil
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop

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

def setup_dependencies():
    """Set up all dependencies - can be called from post-install"""
    print("Setting up pyaoconnect dependencies...")
    
    # Install Node.js dependencies
    if not install_node_dependencies():
        return False
    
    # Clone and install aopy-connect
    if not clone_aopy_connect():
        return False
    
    print("SUCCESS: All dependencies set up successfully!")
    return True

class CustomInstall(install):
    """Custom install command that sets up dependencies"""
    def run(self):
        setup_dependencies()
        install.run(self)
        print("SUCCESS: pyaoconnect installed successfully!")

class CustomDevelop(develop):
    """Custom develop command that sets up dependencies"""
    def run(self):
        setup_dependencies()
        develop.run(self)
        print("SUCCESS: pyaoconnect set up for development!")

# Read the README file
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Super Simple AO Connect - Child-friendly Python interface"

setup(
    name="pyaoconnect",
    version="1.0.0",
    description="Super Simple AO Connect - Child-friendly Python interface",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="Aditya Berry",
    author_email="adityaberry1234@gmail.com",
    url="https://github.com/imortaltatsu/pyaoconnect",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "websockets>=10.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio>=0.18.0",
        ],
    },
    cmdclass={
        "install": CustomInstall,
        "develop": CustomDevelop,
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt"],
    },
    entry_points={
        "console_scripts": [
            "pyaoconnect=pyaoconnect.simple:quick_start",
        ],
    },
    # This ensures the post-install script runs even with pip install git+https
    zip_safe=False,
) 