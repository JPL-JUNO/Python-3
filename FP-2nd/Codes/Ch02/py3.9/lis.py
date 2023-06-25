"""
@Description: Matching patterns without match/case
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-25 12:37:51
"""
import math
import operator as op
from collections import ChainMap
from itertools import chain
from typing import Any, Union, NoReturn

Symbol = str
# The Union type hint is used to
# indicate that the annotated variable can be of any of the specified types.
Atom = Union[float, int, Symbol]
Expression = Union[Atom, list]


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


def evaluate(exp: Expression, env: Environment) -> Any:
    if isinstance(exp, Symbol):
        return env[exp]
    elif not isinstance(exp, list):
        return exp
    elif exp[0] == 'quote':
        (_, x) = exp
        return x
    elif exp[0] == 'if':
        (_, test, consequence, alternative) = exp
        if evaluate(test, env):
            return evaluate(consequence, env)
        else:
            return evaluate(alternative, env)
    elif exp[0] == 'lambda':
        (_, parms, *body) = exp
        return Procedure(parms, body, env)
    elif exp[0] == 'define':
        (_, name, value_exp) = exp
        env[name] = evaluate(value_exp, env)
    elif exp[0] == 'set!':
        (_, name, value_exp) = exp
        env.change(name, evaluate(value_exp, env))
    else:
        (func_exp, *args) = exp
        proc = evaluate(func_exp, env)
        args = [evaluate(arg, env) for arg in args]
        return proc(*args)


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
