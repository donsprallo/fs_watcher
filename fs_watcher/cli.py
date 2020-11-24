import time
import logging
import argparse
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


def main():
    # argument parser
    parser = argparse.ArgumentParser(
        prog='Filesystem Watcher'
    )
    parser.add_argument(
        '--path', '-p',
        type=Path, required=True,
        help="The path to be monitored for changes."
    )
    parser.add_argument(
        '--recursive', '-r',
        type=bool, default=True,
        help="Sets whether the file system is monitored recursively."
    )
    parser.add_argument(
        '--sleep', '-s',
        type=float, default=0.2,
        help="Bedtime for the Watcher."
    )
    args = parser.parse_args()

    # logger config
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # filesystem watcher
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(
        event_handler,
        args.path,
        recursive=args.recursive
    )
    observer.start()

    try:
        while True:
            time.sleep(args.sleep)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    main()
