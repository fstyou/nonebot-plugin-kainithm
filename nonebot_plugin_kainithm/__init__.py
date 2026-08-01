from nonebot import on_command
from nonebot.adapters.qq import MessageSegment

from .command.help_process import help_process

help_command = on_command("help", aliases={"", "帮助"})
create_command = on_command("create")
join_command = on_command("join")
post_command = on_command("post")
start_command = on_command("start")
exit_command = on_command("exit")
stop_command = on_command("stop")
open_command = on_command("open")
submit_command = on_command("submit")
judge_command = on_command("judge")


@help_command.handle()
async def _():
    await help_command.finish(MessageSegment.markdown(help_process()))
