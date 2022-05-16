FROM python:3.8

EXPOSE 5000

WORKDIR /app
COPY . . 

RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
