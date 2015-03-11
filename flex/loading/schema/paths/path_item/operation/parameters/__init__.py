import functools
from flex.datastructures import (
    ValidationList,
)
from flex.constants import (
    ARRAY,
)
from flex.validation.common import (
    generate_object_validator,
    apply_validator_to_array,
)
from .single import (
    single_parameter_validator,
)


parameters_schema = {
    'type': ARRAY,
}

parameters_non_field_validators = ValidationList()
parameters_non_field_validators.add_validator(
    functools.partial(apply_validator_to_array, validator=single_parameter_validator),
)

parameters_validator = generate_object_validator(
    schema=parameters_schema,
    non_field_validators=parameters_non_field_validators,
)