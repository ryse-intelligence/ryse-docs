import json
import textwrap

def recursive_find_text(obj, min_length=50):
    """Finds the longest string in the nested structure."""
    longest = ""
    if isinstance(obj, str):
        if len(obj) > min_length:
            return obj
    elif isinstance(obj, list):
        for item in obj:
            res = recursive_find_text(item)
            if res and len(res) > len(longest):
                longest = res
    return longest

def simplify_structure(obj, depth=0):
    """Creates a simplified view of the structure."""
    indent = "  " * depth
    if isinstance(obj, list):
        if not obj:
            return "[]"
        res = "[\n"
        for i, item in enumerate(obj):
            # simplify large lists
            if isinstance(item, list) and len(item) > 0 and isinstance(item[0], list):
                 res += f"{indent}  [ ... (nested lists) ... ],\n"
                 continue
            
            val = simplify_structure(item, depth + 1)
            # Truncate long strings for display
            if isinstance(item, str) and len(item) > 50:
                val = f'"{item[:20]}...{item[-20:]}" (Length: {len(item)})'
            
            res += f"{indent}  {val}"
            if i < len(obj) - 1:
                res += ","
            res += "\n"
        res += f"{indent}]"
        return res
    elif isinstance(obj, str):
        # check if it's a nested json
        if obj.startswith("[") and obj.endswith("]"):
             return f"JSON_STRING< {simplify_structure(json.loads(obj), depth+1)} >"
        return f'"{obj}"'
    else:
        return str(obj)

try:
    with open('chunk.json.txt', 'r') as f:
        data = json.load(f)
    
    print("### Structure Overview")
    # The outer array: [RPC_ID, null, PAYLOAD_STRING]
    if len(data) > 2 and isinstance(data[2], str):
        payload_str = data[2]
        print(f"Outer Array Length: {len(data)}")
        print(f"Index 0: {data[0]}")
        print(f"Index 2 (Payload) Length: {len(payload_str)}")
        
        inner_json = json.loads(payload_str)
        
        # Let's show the structure of this inner json
        # print("\nSimplified Inner Structure:")
        # print(simplify_structure(inner_json))
        
        # Extract the content
        content = recursive_find_text(inner_json)
        
        print("\n### Extracted Content (Cleaned)")
        print("-" * 40)
        # Parse the content as markdown effectively by just printing it
        # The content in the JSON is already a string with \n escapes handled by json parser
        print(content)
        print("-" * 40)
        
    else:
        print("Unexpected structure.")

except Exception as e:
    print(f"Error: {e}")
