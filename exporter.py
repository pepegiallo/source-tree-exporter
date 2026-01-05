import os
import fnmatch

DEFAULT_IGNORED_DIRS = {".venv", "venv", "__pycache__"}


def export_sources(
    folder=".",
    output_name="_source.txt",
    allowed_types=None,
    ignore_dirs=None,
    ignore_files=None,
):
    folder = os.path.abspath(folder)

    if os.path.isabs(output_name):
        output_file = output_name
    else:
        output_file = os.path.join(folder, output_name)

    self_file = os.path.abspath(__file__)

    if allowed_types:
        normalized = []
        for t in allowed_types:
            t = t.strip()
            if not t:
                continue
            if not t.startswith("."):
                t = "." + t
            normalized.append(t.lower())
        allowed_types = normalized
    else:
        allowed_types = None

    dir_patterns = set(DEFAULT_IGNORED_DIRS)
    if ignore_dirs:
        dir_patterns.update(ignore_dirs)

    file_patterns = set(ignore_files or [])

    with open(output_file, "w", encoding="utf-8") as out:
        for root, dirs, files in os.walk(folder):

            dirs[:] = [
                d for d in dirs
                if not any(fnmatch.fnmatch(d, pat) for pat in dir_patterns)
            ]

            for file in sorted(files):
                if any(fnmatch.fnmatch(file, pat) for pat in file_patterns):
                    continue

                file_path = os.path.abspath(os.path.join(root, file))

                if file_path in {
                    self_file,
                    os.path.abspath(output_file),
                }:
                    continue

                if allowed_types is not None:
                    _, ext = os.path.splitext(file)
                    if ext.lower() not in allowed_types:
                        continue

                rel_path = os.path.relpath(file_path, folder)

                out.write(f"### {rel_path} ###\n")
                with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                    out.write(f.read())
                out.write("\n\n")

    return output_file
