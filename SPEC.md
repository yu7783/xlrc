# xlrc Specification

## Overview

xlrc is an extended LRC format for structured lyric data.

---

## Line format


[time]{key=value;key=value}text


---

## Fields

| Key | Meaning |
|-----|--------|
| id | unique line id |
| ref | reference to another line |
| singer | singer identifier |
| lang | language code |

---

## Rules

- **Encoding:** UTF-8 is required for multilingual support.
- **Timestamp:** One timestamp `[mm:ss.xx]` per line.
- **Metadata:**
  - Order of keys is arbitrary.
  - Unknown keys should be ignored by parsers for forward compatibility.
- **Languages:** Use `ref` to link translations to the original `id`.
- **Legacy Support:** Stripping `{...}` results in a valid standard LRC line.

---

## Example

```
[00:00.00]{id=1;singer=A;lang=ja}こんにちは
[00:00.00]{ref=1;singer=A;lang=en}Hello
```

### More example?
Please check /examples folder
