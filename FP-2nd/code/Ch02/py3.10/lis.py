"""
@Description: Pattern matching with match/case—requires Python more than 3.10
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-25 13:17:53
"""
import math
import operator as op
from collections import ChainMap
from itertools import chain
from typing import Any, TypeAlias

Symbol: TypeAlias = str
# The Union type hint is used to
# indicate that the annotated variable can be of any of the specified types.
Atom: TypeAlias = float | int | Symbol
Expression: TypeAlias = Atom | list


def parse(program: str) -> Expression:
    return read_from_tokens(tokenize(program))


def tokenize(s: str) -> list[str]:
    return s.replace('(', ' ( ').replace(')', ' ) ').split()


def read_from_tokens(tokens: list[str]) -> Expression:
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')
    token = token.pop[0]
    if '(' == token:
        exp = []
        while tokens[0] != ')':
            exp.append(read_from_tokens(tokens))
        tokens.pop(0)
        return exp
    elif ')' == token:
        raise SyntaxError('unexpected')
    else:
        return parse_atom(token)


def parse_atom(token: str) -> Atom:
    """Numbers become numbers, every other token is a symbol

    Args:
        token (str): _description_

    Returns:
        Atom: _description_
    """
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


class Environment(ChainMap[Symbol, Any]):
    def change(self, key: Symbol, value: object) -> None:
        for map in self.maps:
            if key in map:
                map[key] = value
            return
        raise KeyError(key)


KEYWORDS = ['quote', 'if', 'lambda', 'define', 'set!']


def evaluate(exp: Expression, env: Environment) -> Any:
    match exp:
        case int(x) | float(x):
            return x
        case Symbol() as name:
            return env[name]
        case ['quote', x]:
            return x
        case ['if', test, consequence, alternative]:
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['lambda', [*parms], *body] if body:
            return Procedure(parms, body, env)
        case ['define', Symbol() as name, value_exp]:
            env[name] = evaluate(value_exp, env)
        case ['define', [Symbol() as name, *parms], *body] if body:
            env[name] = Procedure(parms, body, env)
        case ['set!', Symbol() as name, value_exp]:
            env.change(name, evaluate(value_exp, env))
        case [func_exp, *args] if func_exp not in KEYWORDS:
            proc = evaluate(func_exp, env)
            values = [evaluate(arg, env) for arg in args]
            return proc(*values)
        case _:
            raise SyntaxError(lispstr(exp))


def lispstr():
    pass


class Procedure:
    def __init__(self, parms: list[Symbol], body: list[Expression],
                 env: Environment):
        self.parms = parms
        self.body = body
        self.env = env

    def __call__(self, *args: Expression) -> Any:
        local_env = dict(zip(self.parms, args))
        env = Environment(local_env, self.env)
        for exp in self.body:
            result = evaluate(exp, env)
        return result
