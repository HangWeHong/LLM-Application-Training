from langchain_community.llms import Ollama


def generate_pet_name():
    llm=Ollama(
    model="llama3.1",
)
    name=llm("I have a dog pet and i want a cool name for it, please suggest me five names")
    return name

if __name__ == "__main__":
    print(generate_pet_name)