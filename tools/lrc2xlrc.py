import re
import sys
from pathlib import Path

TIME_PATTERN = re.compile(r"\[(\d{2}):(\d{2}\.\d{2})\](.*)")

def parse_lrc_line(line):
    match = TIME_PATTERN.match(line)
    if not match:
        return None
    
    mm = int(match.group(1))
    ss = float(match.group(2))
    text = match.group(3).strip()

    timestamp = mm * 60 + ss
    return timestamp, text

def format_timestamp(ts):
    mm = int(ts // 60)
    ss = ts % 60
    return f"[{mm:02d}:{ss:05.2f}]"

def convert_lrc_to_xlrc(lines, singer="A"):
    xlrc_lines = []
    xlrc_lines.append("@title: Converted Song")
    xlrc_lines.append("@artist: Unknown")
    xlrc_lines.append("@language: ja")
    xlrc_lines.append("")

    id_counter = 1
    last_ts = None
    last_text = None

    for line in lines:
        parsed = parse_lrc_line(line)
        if not parsed:
            continue

        ts, text = parsed

        # 同時刻・重複テキストを軽くまとめる
        if last_ts == ts and last_text:
            xlrc_lines.append(
                f"{format_timestamp(ts)}{{ref={id_counter-1};singer={singer};lang=en}}{text}"
            )
        else:
            xlrc_lines.append(
                f"{format_timestamp(ts)}{{id={id_counter};singer={singer};lang=ja}}{text}"
            )
            id_counter += 1

        last_ts = ts
        last_text = text

    return "\n".join(xlrc_lines)

def main():
    if len(sys.argv) < 3:
        print("Usage: python lrc2xlrc.py input.lrc output.xlrc")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = convert_lrc_to_xlrc(lines)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Converted: {input_path} -> {output_path}")

if __name__ == "__main__":
    main()
