"""Testes unittest, sem dependências externas."""
import unittest
from telemetry_validator import validate_telemetry


class TelemetryTest(unittest.TestCase):
    def setUp(self):
        self.payload = {
            "node_id": "node-01",
            "temperature_c": 23.2,
            "humidity_pct": 55,
            "timestamp": "2026-10-27T12:00:00-03:00",
        }

    def test_valid_payload(self):
        result = validate_telemetry(self.payload)
        self.assertEqual(result.node_id, "node-01")
        self.assertEqual(result.humidity_pct, 55.0)
        self.assertEqual(result.timestamp, "2026-10-27T15:00:00+00:00")

    def test_humidity_out_of_range(self):
        self.payload["humidity_pct"] = 110
        with self.assertRaisesRegex(ValueError, "fora do intervalo"):
            validate_telemetry(self.payload)

    def test_invalid_timestamp(self):
        self.payload["timestamp"] = "2026-10-27T12:00:00"
        with self.assertRaisesRegex(ValueError, "fuso horário"):
            validate_telemetry(self.payload)

    def test_bool_is_not_numeric(self):
        self.payload["temperature_c"] = True
        with self.assertRaisesRegex(ValueError, "numérico"):
            validate_telemetry(self.payload)


if __name__ == "__main__":
    unittest.main()
