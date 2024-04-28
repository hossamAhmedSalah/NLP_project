from transformers import BartTokenizer, BartForConditionalGeneration

# Load pre-trained BART model and tokenizer
model = BartForConditionalGeneration.from_pretrained("Moatasem22/bart_CNN_NLP")
tokenizer = BartTokenizer.from_pretrained("Moatasem22/bart_CNN_NLP")


def summarize_text(text):

    inputs = tokenizer.batch_encode_plus(
        [text], max_length=1024, return_tensors="pt", truncation=True, padding="longest"
    )

    summary_ids = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=1024,
        early_stopping=True,
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary
