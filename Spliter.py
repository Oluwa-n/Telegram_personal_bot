import re

MAX_MESSAGE_LENGTH = 4096


def split_message(text: str, limit: int = MAX_MESSAGE_LENGTH):
    if not text:
        return []

    parts = []
    current = ""
    open_tags = []

    tokens = re.findall(r"<[^>]+>|[^<]+", text)

    for token in tokens:

        # HTML tag
        if token.startswith("<"):
            current += token

            # opening tag
            match = re.match(r"<([a-zA-Z0-9]+)>", token)

            if match:
                tag = match.group(1)
                open_tags.append(tag)

            # closing tag
            match = re.match(r"</([a-zA-Z0-9]+)>", token)

            if match:
                tag = match.group(1)
                if tag in open_tags:
                    # remove last occurrence
                    open_tags.reverse()
                    open_tags.remove(tag)
                    open_tags.reverse()

        else:
            # text
            if len(current) + len(token) > limit:

                # close tags safely
                chunk = current

                for tag in reversed(open_tags):
                    chunk += f"</{tag}>"

                parts.append(chunk)

                # reopen tags
                current = ""

                for tag in open_tags:
                    current += f"<{tag}>"

            current += token


    if current:
        for tag in reversed(open_tags):
            current += f"</{tag}>"

        parts.append(current)

    return parts