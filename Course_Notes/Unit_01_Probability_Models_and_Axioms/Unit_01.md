# 6.041x - Unit 1: Probability Models and Axioms
### Notes by Leo Robinovitch
***
## Core Concepts:
*  **Sample space $\mathbf{\Omega}$** contains list (set) of all possible outcomes
  * Mutually exhaustive
  * Collectively exhaustive
  * At the right granularity  
  
  
* **Event:** a subset of the sample space
  
  
* **Fundamental Axioms:**
  1. Nonnegativity: $P(A) >= 0$
  2. Normalization: $P(\Omega) = 1$
  3. Finite (Countable) Additivity: If $A \cap B = \emptyset$, then $P(A \cup B) = P(A) + P(B)$
    * Generally: $A \cap B \neq \emptyset$, then $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
    * **NOTE:** additivity only holds for countable (i.e. sequencable) sequences of events (works for area, but not unit square, real line, etc.)
  
  
* **Consequences:**
  * $P(A) <= 1$
  * $P(\emptyset) = 0$
  * $P(A) + P(A^c) = 1$
  * $P(\{s_1,s_2,...,s_k\}) = P(s_1) + P(s_2) + ... + P(s_k)$
  * If $A \subset B$, then $P(A) <= P(B)$
  * $P(A \cup B \cup C) = P(A) + P(A^c \cap B) + P(A^c \cap B^c \cap C)$
  
  
* **Discrete Uniform Law:** if $\Omega$ consists of n equally likely elements, and event A consists of k elements. then: $\mathbf{P(A) = k * \frac{1}{n}}$
  
  
* For a continuous sample space, **Probability = Area** (Uniform Probability Law)
  
  
* **Probability calculations:**
  1. Specify sample space
  2. Specify probability law
  3. Identify event of interest
  4. Calculate outcome
  
  
* Probability can be interpreted as:
  * Frequencies
  * Descriptions of beliefs
  * Betting preferences