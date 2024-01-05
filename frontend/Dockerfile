# Use an official Python runtime as a parent image
FROM python:3.11

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


# Set the command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "frontend.wsgi:application"]

# Expose port 8000
EXPOSE 8000

