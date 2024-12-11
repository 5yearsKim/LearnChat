from transformers import pipeline


class Generator:
    def __init__(self) -> None:
        self.pipe = pipeline("text-generation", model="microsoft/Phi-3.5-mini-instruct")

    def generate(self, prompt: str) -> str:
        output = self.pipe(prompt, max_length=100, num_return_sequences=1)
        generated_text = output[0]["generated_text"][len(prompt):].strip()

        # Extract the part of the text before the first newline
        first_line: str = generated_text.split("\n")[0]
        return first_line
