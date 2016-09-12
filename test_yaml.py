# -*- coding: utf-8 -*-
import yaml

content = """
{
    format: "hierarchy",
    data: {
        "name": "\u5317\u4eac"
    }
}
"""

result = yaml.load(content)
print(result)
