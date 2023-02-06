# Informacja ogólna
Program koduje adres URL jako wektor 100 liczb i przesyła go do modelu sztucznej inteligencji, który ocenia, czy jest to bezpieczny adres URL czy też nie. W przypadku wyniku powyżej 0,5 program wyświetla ostrzeżenie o próbie phishingu. W przeciwnym razie program wyświetla informację o bezpiecznym adresie URL.

# Dokumentacja
## Phishing Warning System

## Overview
This program uses a TensorFlow-based artificial intelligence model to detect phishing attempts by analyzing URLs. The model is trained on a dataset of URLs, some of which are known to be phishing attempts. When a new URL is passed to the program, it predicts the likelihood of the URL being a phishing attempt. If the likelihood is greater than 0.5, a warning is issued.

## Requirements
- Python 3.x
- TensorFlow 2.x
- Numpy library

## Usage
1. Install the required libraries:
pip install tensorflow numpy

2. Run the program:
python phishing_warning_system.py <url>

Replace `<url>` with the URL you want to check.

## How it works
1. The program encodes the URL as a 100-dimensional vector and passes it to the AI model.
2. The model predicts the likelihood of the URL being a phishing attempt.
3. If the prediction is greater than 0.5, the program issues a warning message.
4. If the prediction is less than or equal to 0.5, the program displays a message indicating that the URL is safe.

## Limitations
The accuracy of the program depends on the quality of the training data and the performance of the AI model. The model may not be able to detect all phishing attempts and may occasionally issue false warnings for safe URLs.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

## License
This program is licensed under the MIT license.
