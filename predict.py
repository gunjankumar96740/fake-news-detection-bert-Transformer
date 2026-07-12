import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("saved_model")
model = AutoModelForSequenceClassification.from_pretrained("saved_model")

model.to(device)
model.eval()


def predict_news(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.softmax(outputs.logits, dim=1)

    prediction = torch.argmax(probabilities, dim=1).item()
    confidence = probabilities[0][prediction].item()

    label = "Fake News" if prediction == 0 else "Real News"

    return label, confidence


# Only runs when executing predict.py directly
if __name__ == "__main__":
    text = input("Enter News: ")
    label, confidence = predict_news(text)
    print(label, confidence)