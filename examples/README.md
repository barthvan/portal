# Exemplo público — Validação de telemetria em Python

Exercício **independente e demonstrativo** de como validar dados recebidos de um dispositivo IoT. Não é código extraído do Terra Sentinel.

## Executar

Requer Python 3.10+ e apenas a biblioteca padrão.

```bash
python examples/telemetry_validator.py
cd examples
python -m unittest -v
```

## O que demonstra

- Modelagem simples com `dataclass`
- Validação de tipos, faixas de valores e timestamps com fuso
- Tratamento de falhas de entrada
- Testes unitários sem bibliotecas externas

Possíveis evoluções: endpoint FastAPI, autenticação, persistência, logs e integração MQTT/LoRa. Essas evoluções ainda **não estão implementadas neste exemplo**.
