import data_fetcher

def load_data(file_path):
  """ Loads a HTML file """
  with open(file_path, "r") as handle:
    return handle.read()

def build_html_data(animals_data):
    output = ""
    for animal in animals_data:
      output += f"name:{animal["name"]}\n"
      output +=f"diet:{animal["characteristics"]["diet"]}\n"
      output +=f"location:{animal["locations"][0]}\n"
      if animal["characteristics"].get("type"):
        output += f"type:{animal["characteristics"].get("type")}\n"
      output += "\n"

    return output


if __name__ == '__main__':
    template = load_data("animals_template.html")
    animal_name = input("Please enter an animal: ")
    data = data_fetcher.fetch_data(animal_name)
    html_animal = build_html_data(data)
    final_data_animal = template.replace("__REPLACE_ANIMALS_INFO__", html_animal)

    with open("index.html", "w") as handle:
        handle.write(final_data_animal)