import re
import doctest


def validate_rgb(rgb_color):
    """
    Примеры:
    >>> validate_rgb("#2345")
    False
    >>> validate_rgb("ffffff")
    False
    >>> validate_rgb("rgb(257, 50, 10)")
    False
    >>> validate_rgb("hsl(20, 10, 0.5)")
    False
    >>> validate_rgb("hsl(34%, 20%, 50%)")
    False
    >>> validate_rgb("#3245fac")
    False
    >>> validate_rgb("#21f48D")
    True
    >>> validate_rgb("#888")
    True
    >>> validate_rgb("rgb(255, 255,255)")
    True
    >>> validate_rgb("rgb(10%, 20%, 0%)")
    True
    >>> validate_rgb("hsl(200,100%,50%)")
    True
    >>> validate_rgb("hsl(0, 0%, 0%)")
    True
    """
    valid_colors = r"^(#([0-9A-Fa-f]{3}){1,2})$|" \
                   r"(rgb\(\s*(\d{1,2}%?|1\d{2}%?|2[0-4]\d%?|25[0-5]%?)(,\s*(\d{1,2}%?|1\d{2}%?|2[0-4]\d%?|25[0-5]%?)){2}\s*\))$|" \
                   r"(hsl\(\s*(\d{1,2}|[12]?\d{2}|3[0-5]\d|360)(,\s*(\d{1,2}|100)%){2}\s*\))$"
    return bool(re.match(valid_colors, rgb_color))
if __name__ == "__main__":
    doctest.testmod()