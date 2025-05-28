import os
import requests
import json

def chat_with_gpt():
    # Configuration with your provided details #
    # Go To Azure AI Foundry Overview Page and Select Azure Open AI and Copy the EndPoint as follows.
    endpoint = "https://project13318301334.openai.azure.com/"
    api_key = "AbXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXGwibK"
    api_version = "2025-01-01-preview"
    
    # Headers for the API request
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    
    print("Azure AI Foundry GPT 4.1 Mini Chat")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    conversation_history = []
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
            
        conversation_history.append({"role": "user", "content": user_input})
        
        payload = {
            "messages": conversation_history,
            "max_tokens": 500,
            "temperature": 0.7,
            "top_p": 0.9
        }
        
        try:
            response = requests.post(
                f"{endpoint}/openai/deployments/gpt-4.1-mini/chat/completions?api-version={api_version}",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                assistant_reply = result['choices'][0]['message']['content']
                print("\nAssistant:", assistant_reply)
                conversation_history.append({"role": "assistant", "content": assistant_reply})
            else:
                print(f"\nError: {response.status_code} - {response.text}")
                
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    chat_with_gpt()
