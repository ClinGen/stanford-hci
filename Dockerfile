# We use the official Python Docker image.
FROM python:3.13

# This prevents .pyc files from being written to disk in the Docker container.
ENV PYTHONDONTWRITEBYTECODE=1

# Write output to stdout or stderr immediately rather than buffering it.
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements lock file into the container.
COPY requirements-lock.txt requirements-lock.txt

# Install dependencies.
RUN pip install -r requirements-lock.txt

# Copy the rest of the application code into the container.
COPY . .

# Make sure we're in the application's root directory.
WORKDIR /app

# Make sure the run script is executable.
RUN ["chmod", "+x", "./run"]

# Build the application for production.
RUN ["./run", "build"]

# Expose port 8000 to the outside world.
EXPOSE 8000

# Run the Django application.
CMD ["./run", "prod"]