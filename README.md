# Metro Lisboa — Home Assistant Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

A Home Assistant custom integration that tracks the service status of all Lisbon Metro lines in real time.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=k0t3n&repository=ha-metro-lisboa&category=integration)

## Sensors

Four binary sensors are created, one per line, grouped under a single **Metro de Lisboa** device:

| Entity | Line | `off` | `on` |
|---|---|---|---|
| `binary_sensor.metro_de_lisboa_linha_amarela` | Linha Amarela | OK | Disrupted |
| `binary_sensor.metro_de_lisboa_linha_azul` | Linha Azul | OK | Disrupted |
| `binary_sensor.metro_de_lisboa_linha_verde` | Linha Verde | OK | Disrupted |
| `binary_sensor.metro_de_lisboa_linha_vermelha` | Linha Vermelha | OK | Disrupted |

Device class: `problem` — `on` means there is a disruption, `off` means normal service.

Each sensor exposes two attributes:

| Attribute | Example |
|---|---|
| `status` | `Ok` / `circulação com atrasos. O tempo de espera pode ser superior ao normal.` |
| `message_type` | `0` (no message) |

Status is polled every **5 minutes**.

## Installation

### HACS (recommended)

Click the button above, or add `https://github.com/k0t3n/ha-metro-lisboa` as a custom repository in HACS with category **Integration**, then install and restart Home Assistant.

### Manual

Copy `custom_components/metro_lisboa/` into your HA `config/custom_components/` directory and restart.

## Setup

After installation and restart, go to **Settings → Devices & Services → Add Integration** and search for **Metro Lisboa**. Click Submit — no configuration needed.

## Dashboard example

```yaml
type: entities
title: Metro de Lisboa
entities:
  - entity: binary_sensor.metro_de_lisboa_linha_amarela
  - entity: binary_sensor.metro_de_lisboa_linha_azul
  - entity: binary_sensor.metro_de_lisboa_linha_verde
  - entity: binary_sensor.metro_de_lisboa_linha_vermelha
```

## Data source

Uses the Metro Lisboa public status API. Data is provided by [Metropolitano de Lisboa, E.P.E.](https://www.metrolisboa.pt)
