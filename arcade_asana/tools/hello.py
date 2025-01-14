from typing import Annotated

from arcade.sdk import tool


@tool
def say_hello(name: Annotated[str, "The name of the person to greet"]) -> str:
    """Say a greeting!"""

    return "Hello, " + name + "!"

@tool
def add(
    a: Annotated[int, "The first number"],
    b: Annotated[int, "The second number"]
) -> Annotated[int, "The sum of the two numbers"]:
    """
    Add two numbers together
    """
    return a + b
 
@tool
def subtract(
    a: Annotated[int, "The first number"],
    b: Annotated[int, "The second number"]
) -> Annotated[int, "The difference of the two numbers"]:
    """
    Subtract two numbers
    """
    return a - b
 
@tool
def multiply(
    a: Annotated[int, "The first number"],
    b: Annotated[int, "The second number"]
) -> Annotated[int, "The product of the two numbers"]:
    """
    Multiply two numbers together
    """
    return a * b
 
@tool
def divide(
    a: Annotated[int, "The numerator"],
    b: Annotated[int, "The denominator"]
) -> Annotated[float, "The quotient of the two numbers"]:
    """
    Divide two numbers
    """
    return a / b
