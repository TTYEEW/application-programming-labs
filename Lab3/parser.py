import argparse

def parse() -> list:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the original image")
    parser.add_argument("--overlay", required=True, help="Path to the overlay")
    parser.add_argument("--output", required=True, help="The Way to Save the Result")
    parser.add_argument("--transparency", type=float, default=0.5, help="Overlay Opacity")

    args = parser.parse_args()
    return args