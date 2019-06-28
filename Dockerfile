FROM python:3.7-alpine
RUN pip install flask && pip install requests

COPY init.py /app/
COPY templates/ /app/templates

WORKDIR /app
ENTRYPOINT ["python"]
CMD ["init.py"]