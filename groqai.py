from groq import Groq
# This library allows us to interact with Groq’s API, which gives us access to powerful language models (LLMs) like the one we’re using (llama-3.3-70b-versatile)

client = Groq(api_key="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")
# This line creates a client object that we can use to interact with the Groq API. The api_key is a unique identifier that allows us to authenticate with the API and access its features.

chat_completion = client.chat.completions.create(
    #
    # Required parameters
    #
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],

    # The language model which will generate the completion.
    model="llama-3.3-70b-versatile",

    #
    # Optional parameters
    #

    # Controls randomness: lowering results in less random completions.
    # As the temperature approaches zero, the model will become deterministic
    # and repetitive.
    temperature=0.5,

    # The maximum number of tokens to generate. Requests can use up to
    # 32,768 tokens shared between prompt and completion.
    # what is a token? A token is a chunk of text that the model processes at once.
    max_completion_tokens=1024,
    # 

    # Controls diversity via nucleus sampling: 0.5 means half of all
    # nucleus sampling is the most likely tokens, while 1.0 means all tokens
    # are considered. The model will sample from the top_p most likely tokens
    # likelihood-weighted options are considered.
    top_p=1,

    # A stop sequence is a predefined or user-specified text string that
    # signals an AI to stop generating content, ensuring its responses
    # remain focused and concise. Examples include punctuation marks and
    # markers like "[end]".
    stop=None,

    # If set, partial message deltas will be sent.
    stream=False,
)

# Print the completion returned by the LLM.
print(chat_completion.choices[0].message.content)