# setting up the machine to get python
FROM python:3.9

# work directory
WORKDIR /usr/src/app

# import things to install in requirements file
COPY requirements.txt .

# run and install from requirements.txt
RUN pip3 install --no-cache-dir  -r requirements.txt

# 
COPY . .

# run python app.py on cmd
CMD ["python", "app.py"]