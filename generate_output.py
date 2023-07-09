import argparse
from datetime import datetime, timedelta

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--TIMEOUT', help='duration of the silence', default='')
    args = parser.parse_args()
    duration=float(args.TIMEOUT.lower().split('h')[0])
    nine_hours_from_now = datetime.now() + timedelta(hours=duration)
    print(nine_hours_from_now)

if __name__=='__main__':
    main()
