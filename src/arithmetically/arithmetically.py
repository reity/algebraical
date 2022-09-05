"""
Class for representing arithmetic operators as callable, immutable, hashable,
and sortable objects.

Instances of the class exported by this library can be used as gate operations
within circuits as they are implemented within the
`circuit <https://pypi.org/project/circuit>`__ library. This library is intended
to complement the `logical <https://pypi.org/project/logical>`__ library for
logical operations.
"""
from __future__ import annotations
from typing import Any, Tuple
import doctest
import operator

class arithmetically(type(operator)):
    """
    Class for representing arithmetic operators. This class is derived from
    the type of the built-in functions found in the :obj:`operator` library.
    Thus, it is possible to invoke these operators on values of
    `numeric <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex>`__
    types and on objects that define the special
    `methods <https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types>`__
    associated with these built-in operators.

    >>> arithmetically.add_(1, 2)
    3

    The name and arity of an instance can be retrieved.

    >>> arithmetically.mul_.name()
    'mul'
    >>> arithmetically.mul_.arity()
    2

    Instances can be compared according to their precedence.

    >>> pow_ > mul_
    True
    >>> pow_ < add_
    False
    >>> sorted([pow_, mul_, add_]) # From lowest to highest precedence.
    [add_, mul_, pow_]

    Instances are also hashable and can be used as members of :obj:`set`
    instances and as keys within :obj:`dict` instances.

    >>> from arithmetically import *
    >>> {add_, add_, add_}
    {add_}
    >>> sorted({add_: 0, mul_: 1}.items())
    [(add_, 0), (mul_, 1)]
    """
    names: dict = None
    """Typical concise names for arithmetic operators."""

    arities: dict = None
    """Arities of arithmetic operators."""

    def __init__(
            self: arithmetically,
            function: operator, # pylint: disable=redefined-outer-name
            name: str
        ):
        """
        Create an instance given a built-in operator object.
        """
        super().__init__(name)

        # Store the original function for use in :obj:`__call__`.
        self.function = function

    def __call__(
            self: arithmetically,
            *arguments: Tuple[Any, ...]
        ) -> Any:
        """
        Apply the function represented by this instance to zero or more
        arguments.

        >>> arithmetically.add_(1, 2)
        3
        """
        return self.function(*arguments)

    def name(self: arithmetically) -> str:
        """
        Return the canonical concise name for this operator.

        >>> arithmetically.mul_.name()
        'mul'
        """
        return arithmetically.names[self] # pylint: disable=unsubscriptable-object

    def arity(self: arithmetically) -> int:
        """
        Return the arity of this operator.

        >>> arithmetically.mul_.arity()
        2
        >>> arithmetically.neg_.arity()
        1
        """
        return arithmetically.arities[self] # pylint: disable=unsubscriptable-object

    def __repr__(self: arithmetically) -> str:
        """
        String representation of this instance.

        >>> arithmetically.mul_
        mul_
        """
        return arithmetically.names[self] + '_' # pylint: disable=unsubscriptable-object

    def __str__(self: arithmetically) -> str:
        """
        String representation of this instance.

        >>> str(arithmetically.mul_)
        'mul_'
        """
        return repr(self)

    def _precedence(self: arithmetically):
        """
        Return an integer that represents the precedence of an operator
        (with a higher integer representing a higher precedence).
        """
        if self == arithmetically.abs_:
            return 3
        if self == arithmetically.pow_:
            return 2
        if self in (
            arithmetically.mul_,
            arithmetically.truediv_,
            arithmetically.floordiv_,
            arithmetically.mod_
        ):
            return 1

        return 0

    def __lt__(self: arithmetically, other: arithmetically) -> bool:
        """
        Compare two operators according to their precedence, where an operator
        with lower precedence is *less than* an operator with higher precedence.

        >>> add_ < mul_
        True
        >>> add_ < pow_
        True
        >>> pow_ < mul_
        False
        >>> add_ > abs_
        False

        Operators that have the same precedence are not *less than* one another.

        >>> mul_ < mul_
        False
        >>> sub_ > add_
        False
        """
        return self._precedence() < other._precedence()

    def __le__(self: arithmetically, other: arithmetically) -> bool:
        """
        Compare two operators according to their precedence, where an operator
        with lower precedence is *less than or equal to* an operator with
        higher precedence.

        >>> add_ <= mul_
        True
        >>> add_ <= pow_
        True
        >>> mul_ >= pow_
        False
        >>> mul_ >= mul_
        True
        """
        return self._precedence() <= other._precedence()

    pos_: arithmetically = None
    """
    Identity operator.

    >>> pos_(2)
    2
    """

    neg_: arithmetically = None
    """
    Negation operator.

    >>> neg_(2)
    -2
    """

    abs_: arithmetically = None
    """
    Absolute value operator.

    >>> abs(-2)
    2
    """

    add_: arithmetically = None
    """
    Addition operator.

    >>> add_(1, 2)
    3
    """

    sub_: arithmetically = None
    """
    Subtraction operator.

    >>> sub_(3, 2)
    1
    """

    mul_: arithmetically = None
    """
    Multiplication operator.

    >>> mul_(2, 3)
    6
    """

    truediv_: arithmetically = None
    """
    Division operator.

    >>> truediv_(4, 2)
    2
    """

    floordiv_: arithmetically = None
    """
    Integer division operator.

    >>> floordiv_(3, 2)
    1
    """

    mod_: arithmetically = None
    """
    Modulus operator.

    >>> mod_(7, 4)
    3
    """

    pow_: arithmetically = None
    """
    Exponentiation operator.

    >>> pow_(2, 3)
    8
    """

# All operators as named class constants.
arithmetically.pos_ = arithmetically(operator.pos, 'pos')
arithmetically.neg_ = arithmetically(operator.neg, 'neg')
arithmetically.abs_ = arithmetically(operator.abs, 'abs')
arithmetically.add_ = arithmetically(operator.add, 'add')
arithmetically.sub_ = arithmetically(operator.add, 'sub')
arithmetically.mul_ = arithmetically(operator.mul, 'mul')
arithmetically.truediv_ = arithmetically(operator.truediv, 'truediv')
arithmetically.floordiv_ = arithmetically(operator.floordiv, 'floordiv')
arithmetically.mod_ = arithmetically(operator.mod, 'mod')
arithmetically.pow_ = arithmetically(operator.pow, 'pow')

# All operators as top-level constants.
pos_: arithmetically = arithmetically.pos_
neg_: arithmetically = arithmetically.neg_
abs_: arithmetically = arithmetically.abs_
add_: arithmetically = arithmetically.add_
sub_: arithmetically = arithmetically.sub_
mul_: arithmetically = arithmetically.mul_
truediv_: arithmetically = arithmetically.truediv_
floordiv_: arithmetically = arithmetically.floordiv_
mod_: arithmetically = arithmetically.mod_
pow_: arithmetically = arithmetically.pow_

# Operator names.
arithmetically.names: dict = {
    arithmetically.pos_: 'pos',
    arithmetically.neg_: 'neg',
    arithmetically.abs_: 'abs',
    arithmetically.add_: 'add',
    arithmetically.sub_: 'sub',
    arithmetically.mul_: 'mul',
    arithmetically.truediv_: 'truediv',
    arithmetically.floordiv_: 'floordiv',
    arithmetically.mod_: 'mod',
    arithmetically.pow_: 'pow'
}

# Operator arities.
arithmetically.arities: dict = {
    arithmetically.pos_: 1,
    arithmetically.neg_: 1,
    arithmetically.abs_: 1,
    arithmetically.add_: 2,
    arithmetically.sub_: 2,
    arithmetically.mul_: 2,
    arithmetically.truediv_: 2,
    arithmetically.floordiv_: 2,
    arithmetically.mod_: 2,
    arithmetically.pow_: 2
}

if __name__ == '__main__':
    doctest.testmod() # pragma: no cover
