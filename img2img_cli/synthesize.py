import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source-images',
                        help='Directory contains source images',
                        required=True)
    parser.add_argument('-t', '--target-images',
                        help='Target Directory to write images to',
                        required=True)
    parser.add_argument('-o', '--operation',
                        help='Synthesizing operation to do on source images',
                        required=True)
    args = parser.parse_args()
    print(args)
