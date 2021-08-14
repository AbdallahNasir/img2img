import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source-images',
                        help='Directory contains source images',
                        required=True)
    parser.add_argument('-t', '--target-images',
                        help='Directory contains target images',
                        required=True)
    parser.add_argument('-m', '--model',
                        help='Model architecture to be used for training',
                        required=True)
    args = parser.parse_args()
    print(args)
