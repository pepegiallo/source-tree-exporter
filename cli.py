import sys
import argparse
from .exporter import export_sources


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Exportiert Dateien eines Ordners in eine Ausgabedatei."
    )

    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Zielordner (default: aktueller Ordner).",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="_source.txt",
        help="Name oder Pfad der Ausgabedatei.",
    )

    parser.add_argument(
        "-t",
        "--types",
        nargs="*",
        help="Erlaubte Dateitypen (z. B.: -t py txt).",
    )

    parser.add_argument(
        "--ignore-dirs",
        nargs="*",
        help="Zu ignorierende Ordnernamen/Patterns.",
    )

    parser.add_argument(
        "--ignore-files",
        nargs="*",
        help="Zu ignorierende Dateinamen/Patterns.",
    )

    return parser.parse_args(argv)


def main():
    args = parse_args(sys.argv[1:])
    output = export_sources(
        folder=args.folder,
        output_name=args.output,
        allowed_types=args.types,
        ignore_dirs=args.ignore_dirs,
        ignore_files=args.ignore_files,
    )
    print(f"Export abgeschlossen: {output}")
