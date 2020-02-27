FROM python:2.7.12
RUN pip install requests
COPY src/pokesheets.py /
ENTRYPOINT [ "python", "pokesheets.py" ]
