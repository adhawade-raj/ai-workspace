# List, Tuple, and Dictionary in Python

| Feature | List | Tuple | Dictionary | Set |
| --- | --- | --- | --- | --- |
| Syntax | [1, 2, 3] | (1, 2, 3) | {"a": 1, "b": 2} | {1, 2, 3} |
| Data type | list | tuple | dict | set |
| Ordered | ✅ Yes | ✅ Yes | ✅ Yes* | ❌ No |
| Mutable | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Can change elements? | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes (add/remove items) |
| Allows duplicates | ✅ Yes | ✅ Yes | Keys ❌, Values ✅ | ❌ No |
| Index-based access | ✅ Yes | ✅ Yes | ❌ No** | ❌ No |
| Key-value pairs | ❌ No | ❌ No | ✅ Yes | ❌ No |
| Access example | a[0] | a[0] | a["name"] | for x in s |
| Can store different data types | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| Can be nested | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No (elements must be hashable) |
| Performance | Moderate | Generally faster than list | Fast key lookup | Fast membership test |
| Memory usage | Higher | Generally lower than list | Higher | Higher than list for some cases |
| Use when | Data may change | Data should not change | Data has key-value relationships | Need unique values / membership checks |
| Example | [10, "Raj", 20] | (10, "Raj", 20) | {"name": "Raj", "age": 29} | {10, 20, 30} |

> * In Python 3.7+, dictionaries preserve insertion order.  
> ** Dictionary access is by key, not by index.