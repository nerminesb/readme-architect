import os
import subprocess

def get_code_summary():
    # Grabs your .py files
    files = [f for f in os.listdir('.') if f.endswith('.py') and f != 'architect.py']
    context = ""
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            context += f"\nFILE {file}:\n{f.read()}\n"
    return context

def generate_readme():
    print("🔍 Scanning project files...")
    code_content = get_code_summary()
    
    if not code_content:
        print(" No .py files found to analyze!")
        return

    # We make the instruction very clear and separate from the code
    instruction = "Write a professional GitHub README.md for the following code. Use sections like Features and Usage. Return ONLY the markdown text."
    full_prompt = f"{instruction}\n\nCODE TO ANALYZE:\n{code_content}"
    
    print(" Sending to Gemini CLI...")
    
    try:
        # We pass the prompt directly as an argument to the 'gemini' command
        result = subprocess.run(['gemini', full_prompt], capture_output=True, text=True, shell=True)
        
        if result.stdout:
            # We clean the output (sometimes CLIs add extra spaces)
            clean_output = result.stdout.strip()
            
            with open("README_GENERATED.md", "w", encoding='utf-8') as f:
                f.write(clean_output)
            print("SUCCESS! Your README is ready.")
        else:
            print(" Gemini output was empty. Error details:")
            print(result.stderr)

    except Exception as e:
        print(f" SYSTEM ERROR: {e}")

if __name__ == "__main__":
    generate_readme()