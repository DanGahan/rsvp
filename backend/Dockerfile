# Use an official Python runtime as a parent image

# Stage 1: Build stage
FROM python:3.13.0-slim-bookworm AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Test stage
FROM builder AS tester

# Run the unit tests
CMD ["python", "-m", "unittest", "APIunittest.py"]

# Stage 3: Production stage
FROM builder AS production

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]

