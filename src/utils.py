def format_entities(entities):
    """Format named entities for Discord display"""
    if not entities:
        return "No entities found."
    
    formatted = []
    current_entity = None
    current_text = ""
    
    for entity in entities:
        if current_entity != entity['entity']:
            if current_text:
                formatted.append(f"**{current_entity}**: {current_text.strip()}")
            current_entity = entity['entity']
            current_text = entity['word'] + " "
        else:
            current_text += entity['word'] + " "
    
    if current_text:
        formatted.append(f"**{current_entity}**: {current_text.strip()}")
    
    return "🔍 Entities found:\n" + "\n".join(formatted)

def split_long_message(message, max_length=2000):
    """Split long messages into chunks that fit Discord's character limit"""
    if len(message) <= max_length:
        return [message]
    
    chunks = []
    while len(message) > max_length:
        # Find the last space within the limit
        split_index = message[:max_length].rfind(' ')
        if split_index == -1:
            split_index = max_length
        
        chunks.append(message[:split_index])
        message = message[split_index:].lstrip()
    
    if message:
        chunks.append(message)
    
    return chunks
