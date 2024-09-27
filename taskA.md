# The first part

**Spam messages:**
- M1: Buy bicycles for free
- M2: Bicycles and motorbikes for free
- M3: Motorbikes rides easy and free
**Normal messages:**
- M4: Let's go ride bicycles
- M5: Last week I bought motorbikes and they are cool
- M6: Some messages about bicycles and motorbikes, that are free, are spam messages

Unique tokens: [buy, bicycles, for, free, and, motorbikes, rides, easy, let's, go, ride, last, week, I, bought, they, cool, some, messages, about, that, spam]

|V| = |Unique tokens| = 22

### Probabilities for spam
- p(buy | spam) = (c(buy & spam) + 1) / (c(any word & spam) + |V|) = (1 + 1) / (14 + 22) = 0.05556
- p(bicycles | spam) = (c(bicycles & spam) + 1) / (c(any word & spam) + |V|) = (1 + 1) / (14 + 22) = 0.05556
- in the similar fashion...
- p(for | spam) = (2 + 1) / 36 = 0.0833
- p(free | spam) = 0.11111
- p(and | spam) = 0.05556
- p(motorbikes | spam) = 0.08333
- p(rides | spam) = 0.05556
- p(easy | spam) = 0.05556

### Probabilities for normal
- p(let's | normal) = 0.05128
- p(go | normal) = 0.05128
- p(ride | normal) = 0.05128
- p(bicycles | normal) = 0.10256
- p(last | normal) = 0.05128
- p(week | normal) = 0.05128
- p(I | normal) = 0.05128
- p(bought | normal) = 0.05128
- p(motorbikes | normal) = 0.07692
- p(and | normal) = 0.05128
- p(they | normal) = 0.05128
- p(cool | normal) = 0.05128
- p(some | normal) = 0.05128
- p(messages | normal) = 0.05128
- p(about | normal) = 0.05128
- p(that | normal) = 0.05128
- p(spam | normal) = 0.05128

### Probability of the sentence generated under classes (spam | normal)
- Sentence: Cool bicycles and motorbikes
- p(sentence | spam) = p(cool | spam) * p(bicyles | spam) * p(and | spam) * p(motorbikes | spam) = 0.05556 x 0.08333 x 0.05556 x 0.08333 
- p(sentence | normal) = p(cool | normal) * p(bicyles | normal) * p(and | normal) * p(motorbikes | normal) = 0.05556 x 0.08333 x 0.05556 x 0.08333 


# The second part

## Confusion Matrix

|                       | Selected as Sport | Selected as Politics | Selected as Culture |
|-----------------------|-------------------|----------------------|---------------------|
| Classified as Sport      | 200               | 20                   | 30                  |
| Classified as Politics   | 10                | 150                  | 15                  |
| Classified as Culture     | 60                | 90                   | 10                  |

### Sport
- TP = 200
- FP = 60 + 10 = 70
- FN = 20 + 30 = 50
- Precision = TP / (TP + FP) = 200 / (200 + 70) = 0.7407
- Recall = TP / (TP + FN) = 200 / (200 + 50) = 0.8
- F1 Score = 2 * Precision * Recall / (Precision + Recall) = 2 * 0.8 * 0.7407 / (0.8 + 0.7407) = 0.7647

### Politics
- TP = 150
- FP = 90 + 20 = 110
- FN = 15 + 10 = 25
- Precision = TP / (TP + FP) = 150 / (150 + 110) = 0.5769
- Recall = TP / (TP + FN) = 150 / (150 + 25) = 0.8571
- F1 Score = 2 * Precision * Recall / (Precision + Recall) = 2 * 0.5769 * 0.8571 / (0.5769 + 0.8571) = 0.6923

### Culture
- TP = 10
- FP = 15 + 30 = 45
- FN = 60 + 90 = 150
- Precision = TP / (TP + FP) = 10 / (10 + 45) = 0.1818
- Recall = TP / (TP + FN) = 10 / (10 + 150) = 0.0625
- F1 Score = 2 * Precision * Recall / (Precision + Recall) = 2 * 0.1818 * 0.0625 / (0.1818 + 0.0625) = 0.0909
