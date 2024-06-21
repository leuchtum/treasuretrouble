# Der TreasureTrouble Stack

**Notiz vom 21.06.2024**

Das Projekt ist als *3-Tier Service* aufgebaut:

* TT Database: Der Datenbank Service
* TT LogicAPI: Der Service mit der Business Logik
* TT CommunicationBot: Der Telegram Bot für die Kommunikation

Daneben gibt es einige weitere Module:

* TT CLI: Damit sind einige Tasks möglich, wie beispielsweise das erstellen von neuen Spielen.
* TT Config: Ein Modul um Konfigurationen zu managen.
# TT LogicAPI

Das zentrale Element ist eine eigenständige API, die alle logischen Prozesse orchestriert.
* API Framework: **Litestar**
* Litestar hat ein hervorragendes System für Datenbanken, insbesondere mit **Piccolo**
# TT Database

Ein eigenständiges Modul, in dem alle Tables etc. definiert sind. Zum Einsatz kommt **Piccolo**. Außerdem gibt es das Projekt **PiccoloAdmin**, in dem eine WebGUI direkt in die DB möglich ist. Zugrunde liegt eine **PostgreSQL** Datenbank.

# TT CommunicationBot

Die Kommunikation mit dem Nutzer soll über Telegram stattfinden. Dazu wird das Paket **python-telegram-bot** genutzt.

## Templates

Mit **Jinja2** können gute Templates für die Kommunikation erstellt werden. Möglich wäre es, für jedes Template (oder eine kleine sinnvolle Menge) ein eigenes Pythonobjekt (z. B. über Dataclass) zu erstellen. Damit wären einfache Tests möglich.

# TT CLI

Als CLI Framework soll **click** genutzt werden. 

# TT Config

Als Configurations Framework soll **dynaconf** genutzt werden.

# Misc
* Für das Logging kommt **structlog** zum Einsatz, da LiteStar ein structlog Plugin besitzt.
