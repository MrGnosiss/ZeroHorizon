# ZeroHorizon - Advanced Exploit Framework
# Created by: Mr. Axolotl | Team: NulLNet

import argparse
from core.builder import PayloadBuilder
from core.shellgen import ShellGenerator
from core.encoder import Encoder
from core.evader import EvasionEngine
from core.pluginloader import PluginLoader
from utils.logger import log
from utils.banners import print_banner


def main():
    print_banner("ZeroHorizon")

    parser = argparse.ArgumentParser(description="ZeroHorizon - Advanced Exploit Framework")
    parser.add_argument("--mode", choices=["build", "shell", "encode", "evade", "plugin"], required=True, help="Mode to operate")
    parser.add_argument("--input", help="Input for encoder/evader")
    parser.add_argument("--plugin", help="Plugin name to load")
    parser.add_argument("--output", help="Output file")
    parser.add_argument("--type", help="Shell/Payload type")

    args = parser.parse_args()

    if args.mode == "build":
        builder = PayloadBuilder()
        builder.build(args.type, args.output)

    elif args.mode == "shell":
        shell = ShellGenerator()
        shell.generate(args.type, args.output)

    elif args.mode == "encode":
        encoder = Encoder()
        encoder.encode(args.input, args.output)

    elif args.mode == "evade":
        evader = EvasionEngine()
        evader.bypass(args.input, args.output)

    elif args.mode == "plugin":
        plugin = PluginLoader()
        plugin.load(args.plugin)

    else:
        log("Invalid mode selected.", level="error")


if __name__ == "__main__":
    main()
