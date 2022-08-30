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

class arithmetical(type(operator)):
    """
    Class for representing arithmetic operators. This class is derived from
    the type of the built-in functions found in the :obj:`operator` library.
    Thus, it is possible to invoke these operators on values of
    `numeric <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex>`__
    types and on objects that define the special
    `methods <https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types>`__
    associated with these built-in operators.

    >>> arithmetical.add_(1, 2)
    3

    The name and arity of an instance can be retrieved.

    >>> arithmetical.mul_.name()
    'mul'
    >>> arithmetical.mul_.arity()
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

    >>> from arithmetical import *
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
            self: arithmetical,
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
            self: arithmetical,
            *arguments: Tuple[Any, ...]
        ) -> Any:
        """
        Apply the function represented by this instance to zero or more
        arguments.

        >>> arithmetical.add_(1, 2)
        3
        """
        return self.function(*arguments)

    def name(self: arithmetical) -> str:
        """
        Return the canonical concise name for this operator.

        >>> arithmetical.mul_.name()
        'mul'
        """
        return arithmetical.names[self] # pylint: disable=unsubscriptable-object

    def arity(self: arithmetical) -> int:
        """
        Return the arity of this operator.

        >>> arithmetical.mul_.arity()
        2
        >>> arithmetical.neg_.arity()
        1
        """
        return arithmetical.arities[self] # pylint: disable=unsubscriptable-object

    def __repr__(self: arithmetical) -> str:
        """
        String representation of this instance.

        >>> arithmetical.mul_
        mul_
        """
        return arithmetical.names[self] + '_' # pylint: disable=unsubscriptable-object

    def __str__(self: arithmetical) -> str:
        """
        String representation of this instance.

        >>> str(arithmetical.mul_)
        'mul_'
        """
        return repr(self)

    def _precedence(self: arithmetical):
        """
        Return an integer that represents the precedence of an operator
        (with a higher integer representing a higher precedence).
        """
        if self == arithmetical.abs_:
            return 3
        if self == arithmetical.pow_:
            return 2
        if self in (
            arithmetical.mul_,
            arithmetical.truediv_,
            arithmetical.floordiv_,
            arithmetical.mod_
        ):
            return 1

        return 0

    def __lt__(self: arithmetical, other: arithmetical) -> bool:
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

    def __le__(self: arithmetical, other: arithmetical) -> bool:
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

    pos_: arithmetical = None
    """
    Identity operator.

    >>> pos_(2)
    2
    """

    neg_: arithmetical = None
    """
    Negation operator.

    >>> neg_(2)
    -2
    """

    abs_: arithmetical = None
    """
    Absolute value operator.

    >>> abs(-2)
    2
    """

    add_: arithmetical = None
    """
    Addition operator.

    >>> add_(1, 2)
    3
    """

    sub_: arithmetical = None
    """
    Subtraction operator.

    >>> sub_(3, 2)
    1
    """

    mul_: arithmetical = None
    """
    Multiplication operator.

    >>> mul_(2, 3)
    6
    """

    truediv_: arithmetical = None
    """
    Division operator.

    >>> truediv_(4, 2)
    2
    """

    floordiv_: arithmetical = None
    """
    Integer division operator.

    >>> floordiv_(3, 2)
    1
    """

    mod_: arithmetical = None
    """
    Modulus operator.

    >>> mod_(7, 4)
    3
    """

    pow_: arithmetical = None
    """
    Exponentiation operator.

    >>> pow_(2, 3)
    8
    """

# All operators as named class constants.
arithmetical.pos_ = arithmetical(operator.pos, 'pos')
arithmetical.neg_ = arithmetical(operator.neg, 'neg')
arithmetical.abs_ = arithmetical(operator.abs, 'abs')
arithmetical.add_ = arithmetical(operator.add, 'add')
arithmetical.sub_ = arithmetical(operator.add, 'sub')
arithmetical.mul_ = arithmetical(operator.mul, 'mul')
arithmetical.truediv_ = arithmetical(operator.truediv, 'truediv')
arithmetical.floordiv_ = arithmetical(operator.floordiv, 'floordiv')
arithmetical.mod_ = arithmetical(operator.mod, 'mod')
arithmetical.pow_ = arithmetical(operator.pow, 'pow')

# All operators as top-level constants.
pos_: arithmetical = arithmetical.pos_
neg_: arithmetical = arithmetical.neg_
abs_: arithmetical = arithmetical.abs_
add_: arithmetical = arithmetical.add_
sub_: arithmetical = arithmetical.sub_
mul_: arithmetical = arithmetical.mul_
truediv_: arithmetical = arithmetical.truediv_
floordiv_: arithmetical = arithmetical.floordiv_
mod_: arithmetical = arithmetical.mod_
pow_: arithmetical = arithmetical.pow_

# Operator names.
arithmetical.names: dict = {
    arithmetical.pos_: 'pos',
    arithmetical.neg_: 'neg',
    arithmetical.abs_: 'abs',
    arithmetical.add_: 'add',
    arithmetical.sub_: 'sub',
    arithmetical.mul_: 'mul',
    arithmetical.truediv_: 'truediv',
    arithmetical.floordiv_: 'floordiv',
    arithmetical.mod_: 'mod',
    arithmetical.pow_: 'pow'
}

# Operator arities.
arithmetical.arities: dict = {
    arithmetical.pos_: 1,
    arithmetical.neg_: 1,
    arithmetical.abs_: 1,
    arithmetical.add_: 2,
    arithmetical.sub_: 2,
    arithmetical.mul_: 2,
    arithmetical.truediv_: 2,
    arithmetical.floordiv_: 2,
    arithmetical.mod_: 2,
    arithmetical.pow_: 2
}

if __name__ == '__main__':
    doctest.testmod() # pragma: no cover
