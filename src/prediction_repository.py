"""Local SQLite storage for wastewater prediction history."""

import sqlite3
from datetime import datetime, timezone
from pathlib import Path


CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS prediction_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    ph REAL NOT NULL,
    turbidity_ntu REAL NOT NULL,
    temperature_c REAL NOT NULL,
    dissolved_oxygen_mg_l REAL NOT NULL,
    bod_mg_l REAL NOT NULL,
    lead_mg_l REAL NOT NULL,
    mercury_mg_l REAL NOT NULL,
    arsenic_mg_l REAL NOT NULL,
    predicted_pollution_level INTEGER NOT NULL
)
"""


def save_prediction(database_path: Path, values, predicted_level: int) -> None:
    """Store one prediction so past app results can be reviewed later."""
    if len(values) != 8:
        raise ValueError("Exactly eight wastewater parameters are required.")

    database_path.parent.mkdir(parents=True, exist_ok=True)
    parameters = tuple(float(value) for value in values)
    created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    connection = sqlite3.connect(database_path)
    try:
        connection.execute(CREATE_TABLE_SQL)
        connection.execute(
            """
            INSERT INTO prediction_history (
                created_at, ph, turbidity_ntu, temperature_c,
                dissolved_oxygen_mg_l, bod_mg_l, lead_mg_l,
                mercury_mg_l, arsenic_mg_l, predicted_pollution_level
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (created_at, *parameters, int(predicted_level)),
        )
        connection.commit()
    finally:
        connection.close()
