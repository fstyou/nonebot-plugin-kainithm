from .utils import command_link

UNKNOWN_TEXT = """# 不存在的命令
使用 {help} 查询命令列表。"""


def unknown_process() -> str:
    return UNKNOWN_TEXT.format(help=command_link("/help"))
