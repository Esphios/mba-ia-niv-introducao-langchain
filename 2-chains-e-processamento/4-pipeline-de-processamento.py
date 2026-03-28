from dotenv import load_dotenv
from typing import Iterator, Dict, Any

from langchain_classic.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()


class TranslationSummaryPipeline:
    """
    Canonical demonstration of LangChain execution models over the same logic.

    Execution modes:
    0. Baseline composed pipeline (reference / docs parity)
    1. Explicit step-by-step invocation (max clarity, debugging)
    2. Runnable pipeline with captured intermediates (idiomatic, observable)
    3. Streaming (token-level output, UX-focused)
    """

    def __init__(self, model: str = "gpt-5-mini", temperature: float = 0.0):
        self.llm = ChatOpenAI(model=model, temperature=temperature)
        self.output_parser = StrOutputParser()

        self.translate_prompt = PromptTemplate(
            input_variables=["initial_text"],
            template="Translate the following text to English:\n```{initial_text}```"
        )

        self.summary_prompt = PromptTemplate(
            input_variables=["text"],
            template="Summarize the following text in 4 words:\n```{text}```"
        )

        self.translate_chain = (
            self.translate_prompt
            | self.llm
            | self.output_parser
        )

    # -------------------------------------------------
    # 0. BASELINE: composed pipeline (reference only)
    # -------------------------------------------------

    def run_baseline(self, text: str) -> str:
        pipeline = (
            {"text": self.translate_chain}
            | self.summary_prompt
            | self.llm
            | self.output_parser
        )

        result = pipeline.invoke({"initial_text": text})

        print("\n[MODE 0: BASELINE COMPOSED]")
        print("Final output:")
        print(result)

        return result

    # -------------------------------------------------
    # 1. EXPLICIT: manual step-by-step invocation
    # -------------------------------------------------

    def run_explicit(self, text: str) -> Dict[str, str]:
        print("\n[MODE 1: EXPLICIT STEPS]")

        translated = self.translate_chain.invoke({
            "initial_text": text
        })
        print("Step 1 - Translation:")
        print(translated)

        summary_prompt_value = self.summary_prompt.invoke({
            "text": translated
        })

        summary_message = self.llm.invoke(summary_prompt_value)
        summary = self.output_parser.invoke(summary_message)

        print("Step 2 - Summary:")
        print(summary)

        return {
            "translation": translated,
            "summary": summary,
        }

    # -------------------------------------------------
    # 2. PIPELINE: composed with captured intermediates
    # -------------------------------------------------

    def run_pipeline(self, text: str) -> Dict[str, str]:
        print("\n[MODE 2: PIPELINE WITH CAPTURED INTERMEDIATE]")

        captured: Dict[str, Any] = {}

        def capture_translation(value: str) -> str:
            captured["translation"] = value
            return value

        translate_with_capture = self.translate_chain | capture_translation

        pipeline = (
            RunnablePassthrough.assign(
                text=translate_with_capture
            )
            | self.summary_prompt
            | self.llm
            | self.output_parser
        )

        summary = pipeline.invoke({"initial_text": text})

        print("Step 1 - Captured translation:")
        print(captured.get("translation"))

        print("Step 2 - Final summary:")
        print(summary)

        return {
            "translation": captured.get("translation"),
            "summary": summary,
        }

    # -------------------------------------------------
    # 3. STREAMING: token-level output
    # -------------------------------------------------

    def run_streaming(self, text: str) -> Iterator[str]:
        print("\n[MODE 3: STREAMING OUTPUT]")

        pipeline = (
            {"text": self.translate_chain}
            | self.summary_prompt
            | self.llm
            | self.output_parser
        )

        for chunk in pipeline.stream({"initial_text": text}):
            print(chunk, end="", flush=True)
            yield chunk

        print()


# -------------------------------------------------
# Main execution
# -------------------------------------------------

def main():
    text = "LangChain é um framework para desenvolvimento de aplicações de IA"

    pipeline = TranslationSummaryPipeline()

    pipeline.run_baseline(text)
    pipeline.run_explicit(text)
    pipeline.run_pipeline(text)
    list(pipeline.run_streaming(text))


if __name__ == "__main__":
    main()
