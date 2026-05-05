"""nist-mapper CLI skeleton.

Usage:
    python -m nist_mapper.cli --help
"""
from __future__ import annotations

import argparse
import sys


def cmd_map(args: argparse.Namespace) -> int:
    print(f"[stub] would map {args.input} -> {args.output} using {args.model}")
    print("[stub] embedding similarity not implemented yet (see roadmap in README)")
    return 0


def cmd_catalog(args: argparse.Namespace) -> int:
    print("[stub] would print the loaded NIST 800-53 Rev 5 control catalog")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="nist-mapper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_map = sub.add_parser("map", help="map a policy doc to NIST controls")
    p_map.add_argument("--input", required=True, help="input file (.pdf or .docx)")
    p_map.add_argument("--output", default="crosswalk.csv", help="output CSV path")
    p_map.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2",
                       help="sentence-transformers model name")
    p_map.set_defaults(func=cmd_map)

    p_cat = sub.add_parser("catalog", help="show the NIST control catalog")
    p_cat.set_defaults(func=cmd_catalog)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
