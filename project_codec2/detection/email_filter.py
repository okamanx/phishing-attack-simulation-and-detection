# detection/email_filter.py
# Enhanced phishing email detection using scikit-learn and custom features

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import numpy as np

# Expanded sample dataset (for demo)
emails = [
    # Phishing
    "Urgent! Your account has been compromised. Click here to reset your password.",
    "Congratulations, you have won a lottery! Please send your bank details.",
    "Update your payment information to avoid service interruption.",
    "We noticed unusual activity in your account. Log in to verify.",
    "Your PayPal account is suspended. Click here to resolve the issue.",
    "Security alert: Unusual sign-in attempt detected. Confirm your identity.",
    "You have a new voicemail. Download the attachment to listen.",
    "Your package could not be delivered. Please provide your address.",
    # Legitimate
    "Dear user, your invoice for last month is attached.",
    "Please review the attached document and let us know your feedback.",
    "Meeting scheduled for tomorrow at 10am. See you there!",
    "Your Amazon order has shipped. Track your package here.",
    "Lunch at 1pm? Let me know if you can make it.",
    "Happy birthday! Wishing you a wonderful year ahead.",
    "Here is the agenda for next week's team meeting.",
    "Thank you for your payment. Your subscription is now active."
]
labels = [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0]  # 1 = phishing, 0 = legitimate

# Suspicious keywords and patterns
SUSPICIOUS_KEYWORDS = [
    'urgent', 'immediately', 'verify', 'reset', 'password', 'bank', 'account',
    'click here', 'login', 'log in', 'confirm', 'security', 'alert', 'suspended',
    'payment', 'unusual', 'identity', 'resolve', 'download', 'attachment', 'provide'
]

# Feature extraction helpers
def extract_features(email_text, sender=None):
    features = {}
    # Find all links
    links = re.findall(r'(http[s]?://[^\s]+)', email_text)
    features['num_links'] = len(links)
    features['num_http_links'] = sum(1 for link in links if link.startswith('http://'))
    features['num_https_links'] = sum(1 for link in links if link.startswith('https://'))
    features['all_links_https'] = features['num_links'] > 0 and features['num_http_links'] == 0
    # Suspicious keywords
    features['num_suspicious_keywords'] = sum(1 for word in SUSPICIOUS_KEYWORDS if word in email_text.lower())
    # Sender domain (if provided)
    if sender:
        features['sender_is_suspicious'] = int(any(domain in sender.lower() for domain in ['paypal', 'amazon', 'bank', 'secure', 'alert']))
    else:
        features['sender_is_suspicious'] = 0
    return features

# TF-IDF + Naive Bayes for text
text_model = make_pipeline(TfidfVectorizer(), MultinomialNB())
text_model.fit(emails, labels)

def detect_phishing_email(email_content, sender=None):
    """
    Returns (is_phishing, confidence, feature_details)
    """
    # Text-based prediction
    proba = text_model.predict_proba([email_content])[0][1]  # Probability of phishing
    is_phishing = proba > 0.5
    # Extract custom features
    features = extract_features(email_content, sender)
    # Refined heuristic for links:
    # - If all links are https, do NOT flag as phishing for links
    # - If any link is http (not https), boost phishing score
    if features['num_http_links'] > 0:
        is_phishing = True
        proba = max(proba, 0.95)
    elif features['all_links_https']:
        # Do not flag as phishing for links
        pass
    # Other heuristics
    if features['num_suspicious_keywords'] > 2 or features['sender_is_suspicious']:
        is_phishing = True
        proba = max(proba, 0.85)
    return is_phishing, proba, features

if __name__ == "__main__":
    print("Paste email content to check for phishing:")
    test_email = input()
    sender = input("Sender email (optional): ")
    is_phish, conf, feats = detect_phishing_email(test_email, sender)
    print("\n--- Detection Result ---")
    if is_phish:
        print(f"[ALERT] This email is likely a phishing attempt! (Confidence: {conf:.2f})")
    else:
        print(f"[OK] This email appears legitimate. (Confidence: {conf:.2f})")
    print("Feature details:", feats)

"""
How it works:
- Uses both ML (text classification) and custom features (links, keywords, sender) for detection.
- If all links are https, does not flag as phishing for links.
- If any link is http (not https), flags as phishing.
- Outputs a confidence score and which features triggered the alert.
- For best results, train on a large, real dataset and expand feature engineering.
""" 