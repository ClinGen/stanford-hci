# We use the official Python Docker image.
FROM python:3.13

# This prevents .pyc files from being written to disk in the Docker container.
ENV PYTHONDONTWRITEBYTECODE=1

# Write output to stdout or stderr immediately rather than buffering it.
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container.
COPY . .

# Install dependencies.
RUN ["./run", "container:deps"]

# Make sure we're in the application's root directory.
WORKDIR /app

# Build the application for production.
RUN ["./run", "build"]

# Expose port 8000 to the outside world.
EXPOSE 8000

# Run the Django application.
CMD ["./run", "prod"]