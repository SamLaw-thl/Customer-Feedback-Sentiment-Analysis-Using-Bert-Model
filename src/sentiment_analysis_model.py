from transformers import pipeline


def analyze_sentiment(comment: str) -> str:
    """
    Analyzes the sentiment of a given comment using a pre-trained BERT model.

    This function takes a customer comment as input, processes it using the specified BERT model,
    and returns the sentiment label ('positive' or 'negative').

    Args:
        comment (str): The customer's comment.

    Returns:
        str: The sentiment label ('positive' or 'negative').
    """
    sentiment_analyzer = pipeline(model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')
    result = sentiment_analyzer(comment)[0]
    return result['label']