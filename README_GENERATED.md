# README Architect

README Architect is a streamlined automation tool designed to generate professional, high-quality GitHub documentation for your Python projects. By leveraging the power of Gemini AI, it analyzes your codebase and produces a structured README that highlights your project's value and functionality.

## Features

- **Automated Code Analysis**: Scans your local directory for Python files and extracts relevant code context automatically.
- **Gemini AI Integration**: Utilizes advanced AI models to interpret your code and write meaningful documentation.
- **Instant Generation**: Produces a `README_GENERATED.md` file in seconds, saving you from manual writing.
- **Developer Centric**: Minimal configuration requiredâ€”just drop it into your project and run.

## Installation

Ensure you have the Gemini CLI installed and configured in your environment before using this tool.

```bash
# Clone the repository
git clone https://github.com/yourusername/readme-architect.git
cd readme-architect
```

## Usage

1. **Place the script**: Copy `architect.py` into the root directory of the project you want to document.
2. **Run the architect**:
   ```bash
   python architect.py
   ```
3. **Review results**: Open the newly created `README_GENERATED.md` file to see your professional documentation.

## How it Works

The tool performs the following steps:
1. **Scanning**: Identifies all `.py` files (excluding `architect.py` itself).
2. **Context Aggregation**: Reads the contents of your files to build a comprehensive view of the codebase.
3. **AI Generation**: Pipes the aggregated code to the Gemini CLI with specific instructions to craft a professional README.
4. **Output**: Writes the AI's response to a file, ready for staging and committing.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.