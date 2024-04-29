from typing import Annotated

from pydantic import StringConstraints

# Regex from https://stackoverflow.com/questions/8634139/phone-validation-regex
Phone = Annotated[str, StringConstraints(pattern=r"^([+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$")]
