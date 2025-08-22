# Day 8: Sentiment Classification – Traditional vs Transformer

## Coding Exercise

Compare sentiment classification using a traditional Bag-of-Words model and a Transformer (DistilBERT):

- **Bag-of-Words Model:** Treats each word independently, ignores context. May misclassify sentences like "I do not enjoy this movie" as positive because it sees "enjoy" and "movie".
- **Transformer Model:** Understands context and word relationships. Correctly classifies "I do not enjoy this movie" as negative.

## Results
- Both models correctly classified the test sentences:
  - "I enjoy this movie." → Positive
  - "I do not enjoy this movie." → Negative
- The transformer model is more robust for complex sentences and context.

## Visualization
See the generated image `sentiment_comparison.png` for confusion matrices and accuracy comparison.

## Code
See `sentiment_transformer_comparison.py` for the full code example.

---

**Try running the code and see how context improves with transformers!**
