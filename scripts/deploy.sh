#!/bin/bash

# Deployment script for Unix-based systems

echo "Starting deployment..."

# Step 1: Pull the latest code from the repository
# This command fetches the latest changes from the main branch of the remote repository
# It's essential to ensure that the application is running the most recent version of the code.
git pull origin main

# Step 2: Install or update dependencies
# We need to install the necessary Python packages for the backend.
# This is done using Poetry to read the pyproject.toml file.
# Ensure that Poetry is installed on your system.

if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Please install it first."
    exit 1
fi

# Install or update dependencies listed in pyproject.toml
poetry install

# Navigate to the frontend directory to install Node.js dependencies.
cd frontend

# The following command installs all required packages listed in package.json.
# This ensures that all frontend dependencies are available for the React application.
npm install

# Step 3: Build the frontend application
# The build command compiles the React application into static files for production.
# These files are typically placed in a 'build' directory within the frontend folder.
npm run build

# Step 4: Restart the backend service (if applicable)
# If you are using a service manager (like systemd) to manage your backend application,
# this command restarts the service to reflect the latest changes.
# Uncomment and customize the following line to restart your specific backend service.
# sudo systemctl restart your_backend_service

echo "Deployment completed successfully!"
