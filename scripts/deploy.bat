@echo off
REM Deployment script for Windows

echo Starting deployment...

REM Step 1: Pull the latest code from the repository
REM This command fetches the latest changes from the main branch of the remote repository.
REM It's essential to ensure that the application is running the most recent version of the code.
git pull origin main

REM Step 2: Install or update dependencies
REM We need to install the necessary Python packages for the backend.
REM This is done by using Poetry to read the pyproject.toml file.
REM Ensure that Poetry is installed on your system.

WHERE poetry >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Poetry is not installed. Please install it first.
    exit /B 1
)

REM Install or update dependencies listed in pyproject.toml
poetry install

REM Navigate to the frontend directory to install Node.js dependencies.
cd frontend

REM The following command installs all required packages listed in package.json.
REM This ensures that all frontend dependencies are available for the React application.
npm install

REM Step 3: Build the frontend application
REM The build command compiles the React application into static files for production.
REM These files are typically placed in a 'build' directory within the frontend folder.
npm run build

REM Step 4: (Optional) Restart the backend service if applicable
REM If you are using a service manager to manage your backend application,
REM these commands can restart the service to reflect the latest changes.
REM Uncomment and customize the following lines to restart your specific backend service.
REM net stop your_backend_service
REM net start your_backend_service

echo Deployment completed successfully!
