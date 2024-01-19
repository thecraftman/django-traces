# Python OpenTelemetry Django Project

This Django web application is instrumented with OpenTelemetry for tracing. It demonstrates a basic web application with automated and custom tracing, allowing for observability and monitoring of the backend processes.

## Prerequisites

Before starting, you should have:

- Python `3.x` installed on your system.
- An Axiom dataset and API token for trace data export, to be used in the `exporter.py` file.

## Installation

**Clone the Repository**:

```bash
git clone https://github.com/thecraftman/django-traces.git
cd django-traces
```

## Install Dependencies:

```
pip install -r requirements.txt
```

## Configuration

- Update the `exporter.py` file with your `SERVICE_NAME`, Axiom API token, and dataset name in place of the placeholders.
- Adjust the OpenTelemetry configuration in the `settings.py` and `exporter.py` files as needed for your environment.

## Running the Application

Start the Django application with the following command:

```py
python manage.py runserver
```

## Using the Application

Access the Application:

- Open a web browser and go to `http://localhost:8000/` for the homepage or `http://localhost:8000/rolldice` to trigger the dice roll function.
- Interacting with these endpoints will generate trace data.

View Traces:

Check your Axiom dataset to see the incoming traces.

## Modifying the Code

**Project Structure:**

- `views.py``: Contains the Django view functions, including the dice roll feature.
- `exporter.py``: Sets up OpenTelemetry tracing with the Axiom exporter.
- `settings.py``: Includes the Django settings along with OpenTelemetry instrumentation setup.

## License 

MIT

