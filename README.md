# Braille Translator

## Overview
The **Braille Translator** is a Python-based tool that facilitates the conversion of text between Braille and various languages. It supports bi-directional translation, enabling users to convert Braille to text and vice versa. The program currently includes built-in support for Persian and English alphabets, numbers, and basic mathematical operations.

## Features
- **Language Translation:** Convert Braille symbols to text and vice versa for supported languages (Persian and English).
- **Numeric and Mathematical Operations:** Translate numbers and mathematical symbols in both Persian and English Braille.
- **Custom Language Support:** Add or remove custom languages and their corresponding Braille translations.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohamadreza-darvishpour/Braille-to-Text-bidirectional-English-Persian.git
   cd braille-translator
   ```

2. **Install dependencies:**
   This project requires no external dependencies beyond Python itself.

3. **Run the script:**
   Execute the script directly in your Python environment.

## Usage
### Translating Braille to Text
To translate Braille text to a specified language:

```python
from translator import translator

translator_instance = translator()
braille_text = "⠃⠗⠁⠊⠇⠇⠑⠀⠝⠊⠝⠑⠗"
translated_text = translator_instance.braille_to_lang(lang='english', text=braille_text)
print(translated_text)  # Outputs: "Braille Niner"
```

### Translating Text to Braille
To convert text to Braille symbols:

```python
from translator import translator

translator_instance = translator()
language_text = "Braille Niner"
braille_text = translator_instance.lang_to_braille(lang='english', text=language_text)
print(braille_text)  # Outputs: "⠃⠗⠁⠊⠇⠇⠑⠀⠝⠊⠝⠑⠗"
```

### Adding a Custom Language
You can add or update a language using the `add_lang` method:

```python
from translator import translator

translator_instance = translator()
new_lang_data = """
space  =  ⠀,
⠁  =  A,
⠃  =  B,
⠉  =  C,
...
"""
result = translator_instance.add_lang('french', new_lang_data)
print(result)  # Outputs: "french added successfully."
```

### Removing a Language
To remove a language, pass the language name with an empty string as the second argument:

```python
result = translator_instance.add_lang('french', '')
print(result)  # Outputs: "french deleted successfully."
```

### Translating Numbers and Math Operations
The translator also supports conversion of numbers and basic math operations:

```python
braille_text = "⠼⠁⠖⠼⠃⠶⠼⠉"
translated_text = translator_instance.braille_to_lang(lang='english', text=braille_text)
print(translated_text)  # Outputs: "1+2=3"
```

## Customization
### Adding New Languages
Extend the translator by adding new languages. The language data should be formatted as a string, mapping Braille symbols to corresponding characters.

### Modifying Existing Languages
Update or correct an existing language's Braille mapping using the `add_lang` method. Provide the updated mappings as the second argument.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue on GitHub if you'd like to contribute to this project.

## Contact
For any questions or feedback, please reach out to me at (mailto:mohamadreza.drpr@gmail.com).

---

Thank you for using the Braille Translator!