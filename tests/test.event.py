import json
import sys
from pathlib import Path

def check_event(file_path: str) -> None:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Sjekk at "message" finnes og har riktig verdi
        if data.get("message") == "hello World":
            print("✅ event.json inneholder riktig message.")
        else:
            print(f"❌ Feil: 'message' er {data.get('message')!r}, forventet 'hello World'.")

    except FileNotFoundError:
        print(f"❌ Fant ikke filen: {file_path}")
    except json.JSONDecodeError as e:
        print(f"❌ Kunne ikke lese JSON: {e}")


if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "./sentiment-demo/event.json"
    check_event(file)
