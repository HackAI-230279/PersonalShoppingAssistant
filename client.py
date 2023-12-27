from dotenv import load_dotenv

load_dotenv()

from typing import Dict, List

from uagents import Agent, Context, Model


class Message(Model):
    message: str

class Query(Model):
    text: str


class Results(Model):
    text: str
    results: List


class Choice(Model):
    choice: int
    results: List


class Product(Model):
    text: str
    result: Dict


client_agent = Agent(
    name="Shopper",
    port=8001,
    seed="our seed for shopping assistant lol",
    endpoint=["http://127.0.0.1:8001/submit"],
)

@client_agent.on_event("startup")
async def start(ctx: Context):
    # ctx.logger.info(f"Hello, my name is {ctx.name} and address is {ctx.address}")
    await ctx.send(
        "agent1qw7gh69x7q2lj23mrc3n24yt7qjfe6jaec863907geqpz3mx47q06zg7rnr",
        Query(
            text=input("\nPlease enter product name: ")
        )
    )

@client_agent.on_event("shutdown")
async def stop(ctx: Context):
    print("Thanks for shopping!")

@client_agent.on_message(model=Results)
async def search(ctx: Context, sender: str, msg: Results):
    print(msg.text)
    await ctx.send(
        sender,
        message=Choice(
            choice=input("\nEnter choice: "),
            results=msg.results,
        )
    )

@client_agent.on_message(model=Product)
async def search(ctx: Context, sender: str, msg: Product):
    print(msg.text)

from uagents.setup import fund_agent_if_low

if __name__ == "__main__":
    print("Starting shopping agent...")
    fund_agent_if_low(str(client_agent.wallet.address()))
    client_agent.run()
