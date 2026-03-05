"""DEBUG: Live regex testing."""

import re
from pathlib import Path


def latex_escape(text):
    replacements = {'&': r'\&', '%': r'\%', '$': r'\$', '_': r'\_', '{': r'\{', '}': r'\}', '\\': r'\textbackslash{}'}
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def replace_newcommand(tex_content, command_name, new_value, escape=True):
    """DEBUG VERSION - shows exactly what happens."""
    print(f"\n🔍 DEBUG replace_newcommand:")
    print(f"  Command: {command_name}")
    print(f"  Old value target: {new_value}")

    if escape:
        new_value = latex_escape(new_value)
        print(f"  Escaped new: {repr(new_value)}")

    # BULLETPROOF PATTERN
    pattern = r'\\newcommand\{\\' + re.escape(command_name) + r'\}\{(.*?)\}\}'
    print(f"  Pattern: {repr(pattern)}")

    # Find matches
    matches = re.findall(pattern, tex_content, re.DOTALL)
    print(f"  Found {len(matches)} matches: {matches[:2]}")

    # Replace
    result = re.sub(pattern, rf'\\newcommand{{\\{command_name}}}{{{new_value}}}', tex_content, flags=re.DOTALL)

    old_count = len(re.findall(r'\\newcommand\{\\' + re.escape(command_name) + r'\}', tex_content))
    new_count = len(re.findall(r'\\newcommand\{\\' + re.escape(command_name) + r'\}', result))
    print(f"  Old commands: {old_count}, New: {new_count}")

    return result


def read_tex_file(file_path):
    return Path(file_path).read_text(encoding='utf-8')


def write_tex_file(file_path, content):
    Path(file_path).write_text(content, encoding='utf-8')
