#!/usr/bin/env python3

import dotenv
dotenv.load_dotenv()

import asyncio
from vhbot.main import main


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(" Shutting Down...")
        exit(0)
