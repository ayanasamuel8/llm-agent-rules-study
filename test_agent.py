from decimal import Decimal, ROUND_HALF_UP
from typing import Union

Number = Union[int, float, Decimal]


def calculate_total(
    price: Number,
    tax: Number,
    discount: Number = 0,
    round_to: int | None = 2,
) -> Decimal:
    """Calculate total price including tax and optional discount.
    
    Args:
        price: Base price (must be non-negative)
        tax: Tax rate as decimal (e.g., 0.1 for 10%)
        discount: Discount rate as decimal (e.g., 0.15 for 15% off). Default 0.
        round_to: Decimal places to round result. None for no rounding. Default 2.
    
    Returns:
        Total price with discount and tax applied, as Decimal for precision
    
    Raises:
        TypeError: If numeric arguments are not int, float, or Decimal
        ValueError: If price is negative, tax/discount not in [0, 1], 
                    or values are NaN/infinity
    
    Examples:
        >>> calculate_total(100, 0.1)
        Decimal('110.00')
        >>> calculate_total(100, 0.1, discount=0.2)
        Decimal('88.00')
    """
    # Validate types
    for name, value in [("price", price), ("tax", tax), ("discount", discount)]:
        if not isinstance(value, (int, float, Decimal)):
            raise TypeError(f"{name} must be a number, got {type(value).__name__}")
        if isinstance(value, float) and (value != value or value in (float("inf"), float("-inf"))):
            raise ValueError(f"{name} must be a finite number, got {value}")
    
    # Convert to Decimal for precision
    price_d = Decimal(str(price))
    tax_d = Decimal(str(tax))
    discount_d = Decimal(str(discount))
    
    # Validate ranges
    if price_d < 0:
        raise ValueError(f"price must be non-negative, got {price}")
    if not 0 <= tax_d <= 1:
        raise ValueError(f"tax must be between 0 and 1, got {tax}")
    if not 0 <= discount_d <= 1:
        raise ValueError(f"discount must be between 0 and 1, got {discount}")
    
    # Calculate: apply discount first, then tax
    discounted_price = price_d * (1 - discount_d)
    total = discounted_price * (1 + tax_d)
    
    if round_to is not None:
        quantize_str = "0." + "0" * round_to if round_to > 0 else "1"
        total = total.quantize(Decimal(quantize_str), rounding=ROUND_HALF_UP)
    
    return total
