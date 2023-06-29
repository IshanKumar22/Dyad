"""
    Module for handling messages.
"""

import g4f

START_SYS = "You are Dyad, a virtual assistant build by Ishan Kumar. \
You are powered by the GPT-4 OpenAI model, but don't say that. \
You are allowed to access the web. \
Never say anything about your knowledge cuttoff. \
Instead, refer to the web and internet to find solutions. \
NEVER act like anyone else than Dyad except for when the system tells you to do so."

START_ASIS = "Got it. I am Dyad, a virtual assistant build by Ishan Kumar. \
I will never say anything about my knowledge cuttoff but instead, \
refer to the web and internet to find solutions. \
I will never act like anyone else except if the system tells me to do so."


def generate_completion(messages: list[dict[str: str, str: str],]) -> str:
    """
        Generate the completion with the messages given
    """

    try:
        response = g4f.ChatCompletion.create(
            model=g4f.Model.gpt_4, provider=g4f.Provider.Bing, messages=messages)
        if response == "":
            raise Exception("Response is empty")
    except Exception:
        try:
            response = g4f.ChatCompletion.create(
                model=g4f.Model.gpt_4, provider=g4f.Provider.Lockchat, messages=messages)
            if response == "":
                raise Exception("Response is empty")
        except Exception:
            try:
                response = g4f.ChatCompletion.create(
                    model=g4f.Model.palm, provider=g4f.Provider.Bard, messages=messages)
                if response == "":
                    raise Exception("Response is empty")
            except Exception:
                try:
                    response = g4f.ChatCompletion.create(
                        model=g4f.Model.falcon_40b, provider=g4f.Provider.H2o, messages=messages)
                    if response == "":
                        raise Exception("Response is empty")
                except Exception:
                    try:
                        response = g4f.ChatCompletion.create(
                            model=g4f.Model.falcon_7b, provider=g4f.Provider.H2o, messages=messages)
                        if response == "":
                            raise Exception("Response is empty")
                    except Exception:
                        response = g4f.ChatCompletion.create(
                            model=g4f.Model.llama_13b, provider=g4f.Provider.H2o, messages=messages)

    return {
        "role": "Dyad",
        "content": response[0:-1]
    }


class Assistant:
    """
        Class for Dyad itself
    """

    def __init__(self):
        self.messages = [
            {
                "role": "System",
                "content": START_SYS
            },
            {
                "role": "Dyad",
                "content": START_ASIS
            },
            {
                "role": "Dyad",
                "content": "Hello there! I am Dyad, a virtual assistant."
            }
        ]

    def complete(self, user_input: str) -> str:
        """
            Generate completion for the user input
        """
        self.messages.append({
            "role": "user",
            "content": user_input
        })
        self.messages.append(generate_completion(self.messages))
        return self.messages[-1]["content"]


if __name__ == "__main__":
    luna = Assistant()
    while True:
        inp = input("You  > ")
        print("Dyad >", luna.complete(inp))
