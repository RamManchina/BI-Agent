import requests
import os

MONDAY_API_KEY = os.getenv("MONDAY_API_KEY")
MONDAY_BOARD_ID = os.getenv("MONDAY_BOARD_ID")

MONDAY_URL = "https://api.monday.com/v2"

def fetch_board_items():
    query = f"""
    {{
      boards(ids: {MONDAY_BOARD_ID}) {{
        name
        items_page(limit: 500) {{
          items {{
            id
            name
            column_values {{
              id
              text
              value
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(
        MONDAY_URL,
        json={"query": query},
        headers={
            "Authorization": MONDAY_API_KEY,
            "Content-Type": "application/json",
        },
    )

    response.raise_for_status()
    data = response.json()

    return data["data"]["boards"][0]["items_page"]["items"]
