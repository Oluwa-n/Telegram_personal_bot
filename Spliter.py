MAX_MESSAGE_LENGTH = 4096

def split_message(text: str, limit: int = MAX_MESSAGE_LENGTH):
    parts = []

    while len(text) > limit:

        split_at = text.rfind("\n", 0, limit)

        if split_at == -1:
            split_at = text.rfind(" ", 0, limit)

        if split_at == -1:
            split_at = limit

        parts.append(text[:split_at])
        text = text[split_at:].lstrip()

    if text:
        parts.append(text)

    return parts