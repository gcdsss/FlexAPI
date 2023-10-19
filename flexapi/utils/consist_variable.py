from enum import Enum


class ServiceType(Enum, str):
    HTTP = "http"
    SOAP = "soap"
    HL7V2 = "hl7v2"
    SCHEDULE = "schedule"
