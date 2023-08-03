#!/usr/bin/env python3

from web_shop import create_app
import logging
from os import environ
from uwsgidecorators import postfork
from prometheus_flask_exporter import PrometheusMetrics
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.wsgi import OpenTelemetryMiddleware

app = create_app()
app.app_agent_receiver_endpoint = environ.get("APP_AGENT_RECEIVER_ENDPOINT")

# this postfork thingy is only required, when app runs in a wsgi container.
# this is explained here: https://opentelemetry-python.readthedocs.io/en/latest/examples/fork-process-model/README.html
# need to try with NGINX as an app server
@postfork
def init_tracing():
    resource = Resource(attributes={"service.name": "web-shop", "team.name": "frontend", "environment":"production"})
    trace.set_tracer_provider(TracerProvider(resource=resource))
    otlp_exporter = OTLPSpanExporter(endpoint=environ.get("OTEL_EXPORTER_OTLP_ENDPOINT"), insecure=True)
    span_processor = BatchSpanProcessor(otlp_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    # uncomment for local OTel debugging to get traces/span to console:
    #trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))

    # be careful not to call this line before the paragraph above!
    # getting the tracer explicitly is only required for the LoggingInstrumentor below
    # using "opentelemetry-instrument" to do auto instrumentation does not work either for the same reason
    tracer = trace.get_tracer(__name__)

    # instrumentation
    PrometheusMetrics(app)
    FlaskInstrumentor().instrument_app(app)
    app.wsgi_app = OpenTelemetryMiddleware(app.wsgi_app)
    RequestsInstrumentor().instrument()
    log_format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] traceID=%(otelTraceID)s span_id=%(otelSpanID)s resource.service.name=%(otelServiceName)s - %(message)s"
    LoggingInstrumentor().instrument(set_logging_format=True, logging_format=log_format, log_level=logging.INFO, tracer_provider=tracer)



if __name__ == "__main__":
    #if you set debug to True, then the /metrics endpoint returns 404
    # this section is only called, when executed directly, not when using
    # an app server, such as uwsgi
    app.run(debug=False, host='0.0.0.0', port=3389)
