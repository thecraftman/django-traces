from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

# Define the service name resource
resource = Resource(attributes={
    SERVICE_NAME: "your-service-name"  # Replace with your actual service name
})

# Create a TracerProvider with the defined resource
provider = TracerProvider(resource=resource)

# Configure the OTLP/HTTP Span Exporter with necessary headers and endpoint
otlp_exporter = OTLPSpanExporter(
    endpoint="https://api.axiom.co/v1/traces",
    headers={
        "Authorization": "Bearer $API_TOKEN",
        "X-Axiom-Dataset": "$DATASET"
    }
)

# Create a BatchSpanProcessor with the OTLP exporter
processor = BatchSpanProcessor(ConsoleSpanExporter())
processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(processor)

# Set the TracerProvider
trace.set_tracer_provider(provider)

# Define a tracer for external use
tracer = trace.get_tracer("your-service-name")
