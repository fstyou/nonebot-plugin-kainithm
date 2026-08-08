def _command_link(command: str) -> str:
    return (
        f"[{command}](mqqapi://aio/inlinecmd?command={command}&enter=false&reply=false)"
    )


def help_process() -> str:
    return help_text.format(
        help=_command_link("/help"),
        create=_command_link("/create"),
        join=_command_link("/join"),
        post=_command_link("/post"),
        start=_command_link("/start"),
        exit=_command_link("/exit"),
        stop=_command_link("/stop"),
        open=_command_link("/open"),
        submit=_command_link("/submit"),
        judge=_command_link("/judge"),
    )


help_text = """# 玩法
1. 创建一局游戏；
2. 邀请其他玩家加入你的游戏；
3. 每名玩家通过私聊投稿谜底的内容；
4. 开始游戏；
5. 玩家可以翻开所有谜底中的某个字符，并根据已有线索猜测谜底的内容；
6. 当有玩家提交对某个谜底的猜测时，由该谜底的投稿人判断其答案是否正确；
7. 所有谜底都被猜中后，游戏结束。

# 命令列表：
## {help}
- 获取此指令菜单。
## {create} <玩家数> <谜底数>
- 创建一局游戏并获取此游戏的 ID 和你的玩家 ID。
- 需指定：
    1. 此局游戏的玩家数（含游戏创建者）
    2. 每名玩家提交的谜底数
- 总谜底数最多 50 个。
## {join}
- 加入游戏并获取你的玩家 ID。
- 游戏创建者会自动加入游戏，无需手动加入。
## {post} <游戏 ID> <谜底序号> <谜底内容>
- 投稿谜底。
- 需指定：
    1. 游戏 ID
    2. 谜底的序号（即这是你投稿的第几个谜底）
    3. 谜底的内容
- **请不要在当前游戏所在的群聊使用此指令。**
- 可以前往其他群聊或通过私聊使用此指令。
## {start} ["force"]
- 开始游戏。
- 可指定：
    - `force` 参数，用于无视警告强行开始游戏。
- 仅游戏的创建者可使用。
## {exit} [<玩家 ID>]
- 退出游戏并公布你投稿的所有谜底。
- 对于游戏创建者需指定：
    - 玩家 ID，用于将对应玩家移出游戏并公布他投稿的所有谜底
## {stop}
- 停止游戏。
- 如果游戏已经开始则公布所有谜底。
- 仅游戏的创建者可使用。
## {open} <字符|"number"|"other">
- 翻开所有谜底中的某个字符。一次仅可翻开一个。
- 需指定：
    - 要翻开的字符
    - 如果参数为 `number`，则翻开所有数字字符
    - 如果参数为 `other`，则翻开所有除字母、数字外的其他字符
## {submit} <谜底序号> <猜测内容>
- 提交对谜底的猜测并获取该猜测的 ID。
- 需指定：
    1. 谜底的序号
    2. 猜测的内容
## {judge} <猜测 ID> <1|0>
- 对猜测的正确与否进行判断。
- 需指定：
    1. 猜测 ID
    2. 判断结果（1 代表正确，0 代表错误）
- 仅对应谜底的投稿人可使用。

# 参数说明：
- `<参数>`：必填参数。
- `[参数]`：可选参数。

# 开发相关
使用 [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html) 协议开源。
开发者：[枫上天游](https://github.com/fstyou)
问题反馈：[qqbot@fstu.cc](mailto:qqbot@fstu.cc?subject=Kainithm%20Bot%20问题反馈)
项目地址：[GitHub](https://github.com/fstyou/nonebot-plugin-kainithm)
"""
