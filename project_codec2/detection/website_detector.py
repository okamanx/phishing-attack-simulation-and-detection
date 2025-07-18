# detection/website_detector.py
# Website phishing detector using ML and rule-based features

import re
from urllib.parse import urlparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample dataset of URLs (for demo)
urls = [
    # Phishing
    'http://secure-login-paypal.com',
    'http://update-account-info.com',
    'http://192.168.1.100/verify',
    'http://amaz0n-login.com',
    'http://bankofamerica-login.com',
    'http://verify-paypal-account.com',
    'http://login-facebook-support.com',
    'http://appleid-verify.com',
    # Legitimate
    'https://www.paypal.com',
    'https://www.amazon.com',
    'https://www.bankofamerica.com',
    'https://www.facebook.com',
    'https://appleid.apple.com',
    'https://www.google.com',
    'https://www.microsoft.com',
    'https://github.com'
]
labels = [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0]  # 1 = phishing, 0 = legitimate

SUSPICIOUS_KEYWORDS = [
    'login', 'secure', 'verify', 'update', 'account', 'bank', 'paypal', 'support', 'appleid', 'facebook', 'password', 'signin', 'confirm'
]

# Feature extraction for URLs
def extract_url_features(url):
    features = {}
    parsed = urlparse(url)
    features['uses_https'] = int(parsed.scheme == 'https')
    features['has_ip'] = int(bool(re.match(r'^\d+\.\d+\.\d+\.\d+$', parsed.hostname or '')))
    features['num_suspicious_keywords'] = sum(1 for word in SUSPICIOUS_KEYWORDS if word in url.lower())
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['length'] = len(url)
    features['has_at_symbol'] = int('@' in url)
    features['has_double_slash'] = int('//' in url[8:])  # after protocol
    features['has_https_in_path'] = int('https' in parsed.path.lower())
    return features

# ML model for URL text
url_model = make_pipeline(TfidfVectorizer(), MultinomialNB())
url_model.fit(urls, labels)

def detect_phishing_website(url):
    """
    Returns (is_phishing, confidence, feature_details)
    """
    # ML prediction
    proba = url_model.predict_proba([url])[0][1]
    is_phishing = proba > 0.5
    features = extract_url_features(url)
    # Rule-based heuristics
    if not features['uses_https']:
        is_phishing = True
        proba = max(proba, 0.95)
    if features['has_ip'] or features['num_suspicious_keywords'] > 1 or features['has_at_symbol']:
        is_phishing = True
        proba = max(proba, 0.90)
    return is_phishing, proba, features

if __name__ == "__main__":
    url = input("Enter website URL to check for phishing: ")
    is_phish, conf, feats = detect_phishing_website(url)
    print("\n--- Detection Result ---")
    if is_phish:
        print(f"[ALERT] This website is likely a phishing site! (Confidence: {conf:.2f})")
    else:
        print(f"[OK] This website appears legitimate. (Confidence: {conf:.2f})")
    print("Feature details:", feats)

"""
How it works:
- Uses both ML (URL text classification) and rule-based features (https, IP, keywords, etc.).
- Flags as phishing if not https, or if suspicious patterns are found.
- Outputs a confidence score and feature details.
- For best results, train on a large, real dataset and expand feature engineering.
""" 