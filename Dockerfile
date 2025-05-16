FROM python:3.6-slim

WORKDIR /app

# Copy all source code into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Expose the port
EXPOSE 5000

# Run the app using Flask CLI
CMD ["flask", "run"]
