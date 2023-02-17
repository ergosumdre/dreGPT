import gradio as gr
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def language_model(input_prompt, input_numBeams, input_min_text_length, input_max_length,
                   input_length_penalty, input_temp):
  model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
  tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")

  text_input = input_prompt
  beams = int(input_numBeams)
  min_text_length = int(input_min_text_length)
  max_text_length = int(input_max_length)
  penalty = int(input_length_penalty)
  temp = float(input_temp)

  inputs = tokenizer(text_input, return_tensors = "pt")
  outputs = model.generate(**inputs,
               min_length=min_text_length, \
               max_new_tokens=max_text_length, \
               length_penalty=penalty, \
               num_beams=beams, \
               no_repeat_ngram_size=2, \
               early_stopping=True, \
               temperature=temp)
  #output_text_Flan_t5 = tokenizer.batch_decode(outputs, \
  #                      skip_special_tokens=True)
  return tokenizer.batch_decode(outputs, skip_special_tokens=True)


language_model_UI = gr.Interface(fn=language_model,
                               inputs=[gr.Textbox(lines = 1, placeholder="Enter your prompt..."),
                                       gr.Slider(10, 100),
                                       gr.Slider(20, 5000),
                                       gr.Slider(20, 5000),
                                       gr.Slider(0, 10),
                                       gr.Slider(0, 1)],
                               outputs="text",
                               title = "Dre's ChatGPT")

language_model_UI.launch(share=True)
