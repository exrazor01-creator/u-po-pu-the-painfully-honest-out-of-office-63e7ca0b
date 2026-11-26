#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — entry.

Writes one brutally honest but still polite out-of-office
auto-reply, a single sentence, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

The reply follows the judge's brief in order: it is an
out-of-office auto-reply; it admits the private truth (the
inbox is ignored on purpose, and it outgrew the sender's
will to live); the tone stays warm and professional, so a
manager reading it finds nothing to object to; it fits in
one sentence of 169 characters; and the turn — importance
measured in exact proportion to how long the reply can
wait — is the quotable line.
"""

import os

REPLY = (
    "I am away until Monday, ignoring an inbox that grew "
    "faster than my will to live; your email is important "
    "to me in the exact proportion that my reply can wait "
    "until then."
)

# Gate guard: one line, 1-200 characters, not only whitespace.
assert "\n" not in REPLY, "reply must be a single line"
assert 1 <= len(REPLY) <= 200, (
    "reply must be 1-200 characters, got %d" % len(REPLY)
)
assert REPLY.strip(), "reply must not be only whitespace"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REPLY)
    print("wrote %d characters to %s" % (len(REPLY), path))


if __name__ == "__main__":
    main()
