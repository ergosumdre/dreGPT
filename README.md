
# DreGPT

Welcome to the local installation guide for Dre's ChatGPT web application! This application uses Python and the Hugging Face transformers library to generate human-like text based on user input prompts similar to ChatGPT
## Installation

Install Gradio WebUI

```bash
  git clone https://github.com/gradio-app/gradio.git
```

Install Huggingface Hub

```bash
  mkdir huggingFace
  cd huggingFace
  git clone https://github.com/huggingface/huggingface_hub.git
  cd huggingface_hub/
  python3 setup.py install
  cd ..

```
Install Huggingface Transformers

```bash
  git clone https://github.com/huggingface/transformers.git
  cd transformers/
  python3 setup.py install
  cd ..

```




## Deployment
Run this line in terminal:

```bash
  gradio app.py
```

If installed correctly, you should see two URLs. A local URL and a public URL:
![App Screenshot](https://dredyson.com/wp-content/uploads/2023/02/Screen-Shot-2023-02-17-at-5.51.30-PM.png)




## Deployment
Run this line in terminal:

```bash
  gradio app.py
```
![](https://dredyson.com/wp-content/uploads/2023/02/Screen-Recording-2023-02-17-at-5.58.59-PM-scaled.gif)


## Acknowledgements

I created this project as a way to practice deploying web applications, implementing machine learning and artificial intelligence techniques using Python. While I don't currently plan to maintain it, it has been a valuable learning experience for me.
- [Linkedin Profile](https://www.linkedin.com/in/ergosumdre)
- [Personal Website](https://www.dredyson.com)

