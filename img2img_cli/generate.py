import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source-images',
                        help='Directory contains source images',
                        required=True)
    parser.add_argument('-t', '--target-images',
                        help='Target Directory to write images to',
                        required=True)
    parser.add_argument('-m', '--model',
                        help='Model file to be used',
                        required=True)
    args = parser.parse_args()
    print(args)
