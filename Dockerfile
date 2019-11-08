# Original miniconda image.
FROM continuumio/miniconda3

# Install pytest to the conda environment.
RUN conda install pytest -y

# Add project to /app.
RUN mkdir /app
WORKDIR /app
COPY . .

# Run pytest.
ENTRYPOINT [ "pytest" ]
