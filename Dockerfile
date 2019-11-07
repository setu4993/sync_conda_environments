# Original miniconda image
FROM continuumio/miniconda3

RUN conda install pytest -y

RUN mkdir /app
WORKDIR /app
COPY . .

ENTRYPOINT [ "pytest" ]
