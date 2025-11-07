import asyncio
import logging
import os

from .zello import ZelloController

log_level = os.environ.get('LOG_LEVEL', 'INFO')
log_format = os.environ.get('LOG_FORMAT', '%(levelname)s:%(name)s:%(message)s')
logging.basicConfig(level=log_level, format=log_format)
logger = logging.getLogger('__main__')


async def _main():
    loop = asyncio.get_running_loop()

    logger.info('Initialising Zello')
    zello = ZelloController()

    await asyncio.gather(*[
        zello.run(),
    ])

    loop.run_forever()

def main():
    asyncio.run(_main())

if __name__ == '__main__':
    main()
