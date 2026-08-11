from dataclasses import dataclass

from .unknown_process import unknown_process
from .utils import command_link


@dataclass(frozen=True)
class CommandHelp:
    name: str
    group: str
    summary: str
    arguments: str
    detail: str

    @property
    def usage(self) -> str:
        if self.arguments == "":
            return f"{command_link(f'/{self.name}')}"
        return command_link(f"/{self.name}", f"/{self.name} {self.arguments}")


COMMANDS = (
    CommandHelp(
        name="create",
        group="准备游戏",
        summary="创建游戏",
        arguments="",
        detail="""在当前群聊创建一局游戏，并获取此游戏的 ID。
- 一个群聊内不可以同时进行多个游戏。""",
    ),
    CommandHelp(
        name="join",
        group="准备游戏",
        summary="加入游戏",
        arguments="<投稿谜底数>",
        detail="""加入当前群聊中等待开始的游戏。
- 一局游戏中的总谜底数最多为 50。""",
    ),
    CommandHelp(
        name="post",
        group="准备游戏",
        summary="投稿谜底",
        arguments="<游戏 ID> <谜底序号> <谜底内容>",
        detail="""向指定游戏投稿谜底。
- 谜底序号表示这是你投稿的第几个谜底。
- 请在私聊或其他群聊使用，不可在该游戏所在群聊投稿。""",
    ),
    CommandHelp(
        name="answers",
        group="准备游戏",
        summary="查看已投稿谜底",
        arguments="<游戏 ID>",
        detail="""查看你当前在指定游戏中投稿的谜底。
- 请在私聊或其他群聊使用，不可在该游戏所在群聊查看。""",
    ),
    CommandHelp(
        name="start",
        group="准备游戏",
        summary="开始游戏",
        arguments="[force]",
        detail="""开始当前游戏。
- 加入 `force` 参数以强制开始游戏。""",
    ),
    CommandHelp(
        name="open",
        group="进行游戏",
        summary="翻开字符",
        arguments="<字符/number/other>",
        detail="""翻开全部谜底中的一个或一类字符。
- 使用 `number` 参数以翻开全部数字字符。
- 使用 `other` 参数以翻开全部非字母、非数字字符。
- 每次只能翻开一个或一类字符。""",
    ),
    CommandHelp(
        name="results",
        group="进行游戏",
        summary="查看当前结果",
        arguments="",
        detail="查看当前谜底列表与已翻开的字符。",
    ),
    CommandHelp(
        name="submit",
        group="进行游戏",
        summary="提交猜测",
        arguments="<谜底序号> <猜测内容>",
        detail="提交对指定谜底的猜测，并获取此猜测的 ID。",
    ),
    CommandHelp(
        name="guesses",
        group="进行游戏",
        summary="查看待处理猜测",
        arguments="",
        detail="查看当前等待你判定的猜测列表。",
    ),
    CommandHelp(
        name="judge",
        group="进行游戏",
        summary="判定猜测",
        arguments="<猜测 ID> <1/0>",
        detail="""判定他人对你的谜底提交的猜测。
- `1`：猜测正确。
- `0`：猜测错误。
- 仅对应谜底的投稿人可使用。""",
    ),
    CommandHelp(
        name="exit",
        group="进行游戏",
        summary="退出游戏",
        arguments="",
        detail="""退出游戏并公布你投稿的谜底。""",
    ),
    CommandHelp(
        name="stop",
        group="进行游戏",
        summary="停止游戏",
        arguments="",
        detail="""停止当前游戏并公布所有谜底。""",
    ),
)

COMMANDS_BY_NAME = {command.name: command for command in COMMANDS}

HELP_MAIN_TEXT = (
    """# 开你字母 Kainithm
---
## 游戏玩法
1. 创建游戏，玩家加入；
2. 在私聊或其他群聊投稿谜底；
3. 开始游戏；
4. 翻开字符并猜谜，由投稿人判定猜测是否正确；
5. 所有谜底被猜中后，游戏结束。
---
## 命令列表
输入 {help} 查看对应命令的参数和限制。
{commands}
## 参数含义
|参数|含义|
|---|---|
|`<参数>`|必填参数|
|`[参数]`|可选参数|
|`<参数1/参数2/…>`|从多种参数中取其一|
---
## 开发与反馈
本项目使用 GPL-3.0 协议开源于 [GitHub](https://github.com/fstyou/nonebot-plugin-kainithm)。
问题请反馈至 [GitHub Issue](https://github.com/fstyou/nonebot-plugin-kainithm/issues)"""
    " 或 [qqbot@fstu.cc](mailto:qqbot@fstu.cc?subject=Kainithm%20Bot%20问题反馈)。"
)


def _command_list() -> str:
    command_groups: dict[str, list[CommandHelp]] = {}
    for command in COMMANDS:
        command_groups.setdefault(command.group, []).append(command)
    return "\n".join(
        f"### {group}\n|命令|功能|用法|\n|---|---|---|\n"
        + "\n".join(
            f"|{command.usage}|{command.summary}"
            f"|{command_link(f'/help {command.name}', '查看用法')}|"
            for command in commands
        )
        for group, commands in command_groups.items()
    )


def _command_detail(command: CommandHelp) -> str:
    return f"# {command.usage}\n{command.detail}"


def help_process(topic: str = "") -> str:
    topic = topic.strip().removeprefix("/").casefold()
    if topic == "":
        return HELP_MAIN_TEXT.format(
            help=command_link("/help","/help <命令>"),
            commands=_command_list(),
        )
    command = COMMANDS_BY_NAME.get(topic)
    if command is not None:
        return _command_detail(command)
    return unknown_process()
