from nonebot import on_command, on_regex
from nonebot.adapters.qq import Message, MessageSegment
from nonebot.params import CommandArg

from .command.answers_process import answers_process
from .command.create_process import create_process
from .command.exit_process import exit_process
from .command.guesses_process import guesses_process
from .command.help_process import help_process
from .command.join_process import join_process
from .command.judge_process import judge_process
from .command.open_process import open_process
from .command.post_process import post_process
from .command.results_process import results_process
from .command.start_process import start_process
from .command.stop_process import stop_process
from .command.submit_process import submit_process
from .command.unknown_process import unknown_process

help_command = on_command("help", aliases={"", "帮助"}, block=True)
create_command = on_command("create", block=True)
join_command = on_command("join", block=True)
post_command = on_command("post", block=True)
answers_command = on_command("answers", block=True)
start_command = on_command("start", block=True)
open_command = on_command("open", block=True)
results_command = on_command("results", block=True)
submit_command = on_command("submit", block=True)
guesses_command = on_command("guesses", block=True)
judge_command = on_command("judge", block=True)
exit_command = on_command("exit", block=True)
stop_command = on_command("stop", block=True)
unknown_command = on_regex(r"\S", priority=100)


@help_command.handle()
async def _(argument: Message = CommandArg()):
    topic = argument.extract_plain_text()
    await help_command.finish(MessageSegment.markdown(help_process(topic)))


@create_command.handle()
async def _():
    await create_command.finish(MessageSegment.markdown(create_process()))


@join_command.handle()
async def _():
    await join_command.finish(MessageSegment.markdown(join_process()))


@post_command.handle()
async def _():
    await post_command.finish(MessageSegment.markdown(post_process()))


@answers_command.handle()
async def _():
    await answers_command.finish(MessageSegment.markdown(answers_process()))


@start_command.handle()
async def _():
    await start_command.finish(MessageSegment.markdown(start_process()))


@open_command.handle()
async def _():
    await open_command.finish(MessageSegment.markdown(open_process()))


@results_command.handle()
async def _():
    await results_command.finish(MessageSegment.markdown(results_process()))


@submit_command.handle()
async def _():
    await submit_command.finish(MessageSegment.markdown(submit_process()))


@guesses_command.handle()
async def _():
    await guesses_command.finish(MessageSegment.markdown(guesses_process()))


@judge_command.handle()
async def _():
    await judge_command.finish(MessageSegment.markdown(judge_process()))


@exit_command.handle()
async def _():
    await exit_command.finish(MessageSegment.markdown(exit_process()))


@stop_command.handle()
async def _():
    await stop_command.finish(MessageSegment.markdown(stop_process()))


@unknown_command.handle()
async def _():
    await unknown_command.finish(MessageSegment.markdown(unknown_process()))
