def command_link(command: str, label: str | None = None) -> str:
    text = command if label is None else label
    return f"[{text}](mqqapi://aio/inlinecmd?command={command}&enter=false&reply=false)"
