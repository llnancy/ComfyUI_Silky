from typing import List
import random

class PromptSelector:
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompts": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": 'Please enter your prompts\n!'
                    }
                ),
                "selector_mode": (
                    [ "sequential", "random" ],
                    { "default": "sequential" },
                ),
                "seed": (
                    "INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}
                )
            },
            "optional": {
                "repeat": ("INT",),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "select"

    CATEGORY = "SILKY/BasicNodes"

    def select(self, prompts: str, selector_mode: str, seed: int, repeat: int = 1) -> str:
        prompt_list = prompts.splitlines()
        if selector_mode == "sequential":
            # 按顺序轮询
            index = getattr(self, 'current_index', 0)
            selected_prompt = prompt_list[index]
            print(f"index = {index}, selected_prompt = {selected_prompt}")
            self.current_index = (index + 1) % len(prompt_list)
        else:
            # 随机选择
            random.seed(seed)
            selected_prompt = random.choice(prompt_list)
            print(selected_prompt)
        return (selected_prompt,)
