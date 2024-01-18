# Use an official Python runtime as a parent image
FROM python:3.12 AS builder

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local directory to the working directory in the container
COPY . /app/

# Run collectstatic command against the frontend directory
# RUN python manage.py collectstatic --no-input --clear --settings=frontend.settings

# Stage 2: Test stage
FROM builder AS tester

#Run Unit Tests
CMD ["python", "manage.py", "test", "--settings=frontend.settings"]
#RUN python manage.py test --settings=frontend.settings

# Stage 3: Production stage
FROM builder AS production

# Set the command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "frontend.wsgi:application", "--workers", "3", "--timeout", "15"]

# Expose port 8000
EXPOSE 8000

