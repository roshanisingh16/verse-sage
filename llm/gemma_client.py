import torch
import kagglehub
from transformers import AutoTokenizer, AutoModelForCausalLM

class GemmaClient:
    def __init__(self, kaggle_model: str = "google/gemma-3/transformers/gemma-3-4b-it",
                 enable_thinking: bool = False):
        self.enable_thinking = enable_thinking
        
        print(f"Downloading and loading native {kaggle_model} model from Kagglehub...")
        model_path = kagglehub.model_download(kaggle_model)
        
        self.processor = AutoTokenizer.from_pretrained(model_path)
        
        # ⚡ bfloat16 memory prevents the blank string NaN overflow bug!
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="cuda:0", 
            torch_dtype=torch.bfloat16, 
            attn_implementation="sdpa"
        )
        self.device = next(self.model.parameters()).device

    def generate(self, messages: list, max_new_tokens: int = 450) -> str:
        if self.enable_thinking:
            messages = self._inject_thinking_token(messages)

        inputs = self.processor.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(self.device)

        input_len = inputs["input_ids"].shape[-1]

        with torch.inference_mode():
            output_ids = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False, 
                use_cache=True 
            )

        new_tokens = output_ids[0][input_len:]
        return self.processor.decode(new_tokens, skip_special_tokens=True)

    @staticmethod
    def _inject_thinking_token(messages: list) -> list:
        messages = [dict(m) for m in messages]
        for m in messages:
            if m["role"] == "system":
                m["content"][0]["text"] = "<|think|>" + m["content"][0]["text"]
                return messages
        messages.insert(0, {"role": "system", "content": [{"type": "text", "text": "<|think|>"}]})
        return messages
