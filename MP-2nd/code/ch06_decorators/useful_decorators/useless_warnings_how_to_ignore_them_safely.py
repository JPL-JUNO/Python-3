"""
@Title: Useless warnings – How to ignore them safely
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-28 11:59:27
@Description: 隐藏一些预期内的警告，但不是全部警告
"""

import warnings
import functools


def ignore_warnings(warning, count=None):
    def _ignore_warnings(function):
        @functools.wraps(function)
        def __ignore_warnings(*args, **kwargs):
            # Execute the code while catching all warnings
            with warnings.catch_warnings(record=True) as ws:
                # Catch all warnings of the give type
                warnings.simplefilter("always", warning)
                # execute the function
                result = function(*args, **kwargs)
            # re-warn all warnings beyond the expected count
            if count is not None:
                for w in ws[count:]:
                    warnings.warn(w.message)
            return result
        return __ignore_warnings
    return _ignore_warnings


@ignore_warnings(DeprecationWarning, count=1)
def spam():
    warnings.warn("Deprecation 1", DeprecationWarning)
    warnings.warn("Deprecation 2", DeprecationWarning)


# Note, we use catch_warnings here because doctest normally
# capture the warnings quietly
with warnings.catch_warnings(record=True) as ws:
    spam()

    for i, w in enumerate(ws):
        print(w.message)
