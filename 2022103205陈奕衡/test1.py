import random
from typing import List, Dict, Any

def dataSampling(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, list):
            result[key] = []
            for data_type in value:
                if data_type == int:
                    result[key].append(random.randint(0, 100))
                elif data_type == float:
                    result[key].append(random.uniform(0, 100))
                elif data_type == str:
                    result[key].append(''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 5)))
        elif isinstance(value, dict):
            result[key] = {}
            for inner_key, inner_value in value.items():
                if inner_value == int:
                    result[key][inner_key] = random.randint(0, 100)
                elif inner_value == float:
                    result[key][inner_key] = random.uniform(0, 100)
                elif inner_value == str:
                    result[key][inner_key] = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 5))
        else:
            raise ValueError(f'Value type "{value}" not supported')
    return result

