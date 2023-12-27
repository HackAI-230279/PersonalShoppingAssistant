from uagents import Agent, Context
from . import *

from backend.sites.__main__ import sorted_results

price_agent = Agent(
    name="Shopping Assistant",
    port=8000,
    endpoint=["http://127.0.0.1:8000/submit"],
)


@price_agent.on_event("startup")
async def start(ctx: Context):
    ctx.logger.info(f"Hello, my name is {ctx.name} and address is {ctx.address}")


@price_agent.on_event("shutdown")
async def stop(ctx: Context):
    ctx.logger.info(f"Bye, this was {ctx.name}. Nice meeting ya!")


@price_agent.on_message(model=Query)
async def search(ctx: Context, sender: str, msg: Query):
    ctx.logger.info(f"Agent {sender} searching for {msg.text}")
    results = sorted_results(msg.text)
    await ctx.send(
        sender,
        Results(
            text=results[0],
            results=results[1],
        ),
    )


@price_agent.on_message(model=Choice)
async def search(ctx: Context, sender: str, msg: Choice):
    result = msg.results[msg.choice - 1]
    ctx.logger.info(f"Agent {sender} selected {result['name']} from {result['site']}")
    await ctx.send(
        sender,
        Product(
            text=f"\nYour link to {result['name']}:\n{result['link']}",
            result=result,
        ),
    )
