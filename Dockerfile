FROM python:3.12-slim

WORKDIR /agent

COPY ./requirements.txt /agent/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /agent/requirements.txt

COPY . /agent

EXPOSE 8501

CMD ["streamlit","run","app.py","--server.address=0.0.0.0","--server.port=8501"]