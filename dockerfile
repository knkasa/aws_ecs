# Use python 3.11
FROM python:3.11-slim

# Set the working directory to /my_dir.  
# This will be the directory that will be used when the container launches.
WORKDIR /my_dir

# Copy the current directory contents into the container at /my_dir
COPY . /my_dir

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
# You only need this if you are running web app and users need to access the web.
EXPOSE 80

# Define environment variable.
# You can retrieve the env variable in the test.py. 
ENV MY_STRING my_env_string

# Run python script when the container launches
CMD ["python", "test.py"]