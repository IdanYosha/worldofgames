FROM python:3-alpine
COPY . /
RUN pip install -r requirements.txt
CMD [ "python", "/MainGame.py" ]