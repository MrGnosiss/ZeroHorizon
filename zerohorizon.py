# zerohorizon.py

import argparse
import os
from core import builder, shellgen, encoder, evader, pluginloader
from utils import logger, banners


def main():
    banners.print_banner()
    logger.info("Welcome to ZeroHorizon - Modular Exploit Framework by Mr.Axolotl")

    parser = argparse.ArgumentParser(description="ZeroHorizon - Offensive Exploit Framework")
    parser.add_argument('--build', help='Build custom payload', action='store_true')
    parser.add_argument('--reverse-shell', help='Generate reverse shell', action='store_true')
    parser.add_argument('--encode', help='Encode payload/shellcode', action='store_true')
    parser.add_argument('--evade', help='Run EDR bypass techniques', action='store_true')
    parser.add_argument('--plugins', help='List and run plugins', action='store_true')
    args = parser.parse_args()

    if args.build:
        builder.run()
    elif args.reverse_shell:
        shellgen.run()
    elif args.encode:
        encoder.run()
    elif args.evade:
        evader.run()
    elif args.plugins:
        pluginloader.run_plugins()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
