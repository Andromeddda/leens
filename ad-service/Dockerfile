FROM python:3.10-slim AS build

RUN apt-get update && apt-get install -y gcc

WORKDIR /app

# install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# install requirements for common
COPY --from=common /requirements.txt /app/common-requirements.txt
RUN pip install --no-cache-dir -r common-requirements.txt

# copy packages
COPY --from=common / /app/common
COPY . .

EXPOSE 8081

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]