# Use the official Python image (slim version for optimization)
FROM python:3.9-slim

# Define environment variables to improve Python behavior
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Create the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Python dependencies without cache to save space
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code to the working directory
COPY . .

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# Ensure the entrypoint script has execute permissions
RUN chmod +x /entrypoint.sh

# Set the entrypoint to the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# CMD provides additional arguments that can be overridden at runtime
CMD ["jogoteca.py"]
