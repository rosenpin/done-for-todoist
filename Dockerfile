FROM python:3

EXPOSE 9991/tcp

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD [ "python", "./main.py" ]
