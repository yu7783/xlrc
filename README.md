# xlrc
xlrc is a human-readable extended LRC format that adds structured metadata for multilingual and multi-singer lyrics while remaining backward-compatible.
xlrc is a **next-generation lyric subtitle format (LRC extension)** designed for:

- karaoke subtitle systems
- multilingual lyrics
- multi-singer songs
- AI-friendly lyric processing

---

## Why xlrc?

LRC format is widely used but limited:

- No structured metadata per line
- No multi-singer support
- No multilingual structure

xlrc extends LRC while keeping human readability.

---

## Features

- 🎤 Multi-singer support
- 🌐 Multilingual lyrics per line
- 🧠 AI-friendly structured format
- 🔄 Compatible conversion from LRC
- ✏️ Human editable

---

## Tools

- LRC → XLRC converter (Python)

---

## Compatibility

- Standard LRC files can be converted to XLRC
- XLRC can be downgraded to LRC (metadata stripped)

---

## Status

Experimental specification (early draft v0.1)

---

## 📝 Example

```text
@title: Sample Song
@artist: VPTensor35

[00:12.34]{id=1;singer=A;lang=ja}こんにちは世界
[00:12.34]{ref=1;singer=A;lang=en}Hello world
[00:15.50]{id=2;singer=B;lang=ja}新しい時代の幕開けだ
[00:15.50]{ref=2;singer=B;lang=en}A new era begins
```

---

## Try xlrc?
1.Clone the repository.
2.Check SPEC.md for the full syntax specification.
3.Try converting your .lrc files using the scripts in tools/.

---

## License

MIT

---
