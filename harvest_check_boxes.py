import re

def detection_line_to_dict(line: str)->dict:
    """ 
    Returns a dict containing data extracted from a line beginning with "## Detected object" 
    """
    pattern = r'## Detected object (\d+) confidence: ([\d.]+) object_index: (\d+)'

    match = re.search(pattern, line)

    if match:
        # Construct the dictionary with appropriate type casting
        result = {
            'detected_object': int(match.group(1)),
            'confidence': float(match.group(2)),
            'object_index': int(match.group(3))
        }
        
        return result
    else:
        return {}
        
# # Usage example:
# line = '## Detected object 26 confidence: 0.260 object_index: 1'
# mydict =  detection_line_to_dict(line)
# print(mydict)


def parse_checkbox(line):
    # Regex explanation:
    # -\s* : Match a hyphen followed by optional whitespace
    # \[(.*?)\] : Capture the content inside square brackets
    # \s+       : Match one or more whitespace characters
    # (.*)      : Capture the remaining text as the label
    match = re.search(r'-\s*\[(.*?)\]\s+(.*)', line)
    
    if match:
        status_char = match.group(1).strip().lower()
        label = match.group(2).strip()
        
        # Consider 'x' as True, any other character (like a space) as False
        is_checked = (status_char == 'x')
        
        return {label: is_checked}
    
    return None

# Example usage:
line = '- [x] accept'
result = parse_checkbox(line)
print(result)  # Output: {'accept': True}





# with open('sam3.md') as f:
#     lines = f.readlines()
    



# for line in lines:
#     s = []
#     if line.startswith('## Detected object'):
#         print(line.strip())
#     if line.startswith('- ['):
#         print(line.strip())