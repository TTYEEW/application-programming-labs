import argparse

def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the original image")
    parser.add_argument("--overlay", required=True, help="Path to the overlay")

    args = parser.parse_args()
    return args