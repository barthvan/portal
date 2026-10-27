"""Exemplo independente de validação de telemetria ambiental.

Código demonstrativo para portfólio: não utiliza código nem endpoints
do projeto Terra Sentinel em produção.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from typing import Any


@dataclass(frozen=True)
class Telemetry:
    node_id: str
    temperature_c: float
    humidity_pct: float
    timestamp: str


def validate_telemetry(payload: dict[str, Any]) -> Telemetry:
    """Valida dados básicos de um nó IoT e retorna objeto imutável."""
    if not isinstance(payload, dict):
        raise ValueError("Payload precisa ser um objeto JSON")
    node_id = payload.get("node_id")
    if not isinstance(node_id, str) or not node_id.strip() or len(node_id) > 64:
        raise ValueError("node_id deve ser texto não vazio com até 64 caracteres")

    def numeric(name: str, minimum: float, maximum: float) -> float:
        value = payload.get(name)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{name} precisa ser numérico")
        value = float(value)
        if not minimum <= value <= maximum:
            raise ValueError(f"{name} fora do intervalo esperado")
        return value

    temp = numeric("temperature_c", -80, 100)
    humidity = numeric("humidity_pct", 0, 100)
    raw_time = payload.get("timestamp")
    if not isinstance(raw_time, str):
        raise ValueError("timestamp deve ser string ISO-8601")
    try:
        parsed = datetime.fromisoformat(raw_time.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("timestamp inválido") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp deve conter fuso horário")
    return Telemetry(node_id.strip(), temp, humidity, parsed.astimezone(timezone.utc).isoformat())


if __name__ == "__main__":
    sample = {
        "node_id": "sensor-demo-01",
        "temperature_c": 24.5,
        "humidity_pct": 58,
        "timestamp": "2026-10-27T12:00:00-03:00",
    }
    print(json.dumps(validate_telemetry(sample).__dict__, indent=2, ensure_ascii=False))
