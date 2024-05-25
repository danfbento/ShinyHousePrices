import pandas as pd
from pathlib import Path

app_dir = Path(__file__).parent.parent
fullRRP = pd.read_csv(app_dir / "data/PPR-ALL_formated.csv")
