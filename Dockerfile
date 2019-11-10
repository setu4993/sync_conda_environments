# Original miniconda image.
FROM continuumio/miniconda3

# Add project to /app.
RUN mkdir /app
WORKDIR /app
COPY . .

# Install requirements using pip.
RUN pip install -r requirements.txt
# Install requirements-tests using pip.
RUN pip install -r requirements-tests.txt

# Run pytest.
ENTRYPOINT [ "pytest" ]
