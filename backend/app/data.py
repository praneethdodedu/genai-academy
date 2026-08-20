# -*- coding: utf-8 -*-
"""
Curriculum content for GenAI Academy.

Structure:
TOPICS -> list of topic metadata (id, name, description, icon, color)
LESSONS -> dict keyed by topic_id -> dict keyed by level -> list of lesson dicts

Each lesson dict:
  id: str (unique slug)
  title: str
  minutes: int (estimated read time)
  summary: str (one-liner shown in lists)
  content: str (markdown body)
  takeaways: list[str]
"""

LEVELS = ["basics", "intermediate", "pro"]

LEVEL_META = {
    "basics": {"label": "Basics", "description": "Start here — no prior AI knowledge needed."},
    "intermediate": {"label": "Intermediate", "description": "You understand the fundamentals — go deeper."},
    "pro": {"label": "Pro", "description": "Advanced, production-grade concepts and techniques."},
}

TOPICS = [
    {
        "id": "ai",
        "name": "AI Foundations",
        "tagline": "The building blocks of artificial intelligence",
        "color": "#6366F1",
    },
    {
        "id": "genai",
        "name": "Generative AI",
        "tagline": "How machines create text, images, and more",
        "color": "#8B5CF6",
    },
    {
        "id": "rag",
        "name": "RAG",
        "tagline": "Grounding AI in real, retrievable knowledge",
        "color": "#0EA5E9",
    },
    {
        "id": "prompt-engineering",
        "name": "Prompt Engineering",
        "tagline": "The craft of talking to AI models effectively",
        "color": "#F59E0B",
    },
]

LESSONS = {
    "ai": {
        "basics": [
            {
                "id": "ai-b-1",
                "title": "What is Artificial Intelligence?",
                "minutes": 6,
                "summary": "A plain-language introduction to what AI actually is — and isn't.",
                "content": """Artificial Intelligence (AI) is the field of building systems that perform tasks which normally require human intelligence — recognizing images, understanding language, making decisions, or spotting patterns in data.

AI is not one single technology. It's an umbrella term covering many techniques, from simple rule-based systems written decades ago to the large neural networks powering today's chatbots.

### A useful way to think about it

Instead of asking "is this AI?", it's more useful to ask "how is this system achieving its behavior?" A thermostat that turns on heating below a set temperature is *automation*, not AI — it follows a fixed rule. A system that learns from thousands of examples of cat photos to recognize a cat it has never seen before is exhibiting AI, specifically the sub-field called Machine Learning.

### Why AI feels different today

Three things converged over the last decade to make AI dramatically more capable:

- **Data** — the internet created enormous datasets to learn from.
- **Compute** — GPUs made it feasible to train huge models.
- **Algorithms** — breakthroughs like the Transformer architecture (2017) unlocked new capabilities.

That combination is why AI went from a research curiosity to something you use every day, often without noticing.""",
                "takeaways": [
                    "AI is an umbrella term for systems that mimic human-like intelligence, not one specific technology.",
                    "The key distinction is whether behavior is learned from data (AI) or explicitly hard-coded (automation).",
                    "Data, compute, and algorithmic breakthroughs are why AI accelerated so quickly in the last decade.",
                ],
            },
            {
                "id": "ai-b-2",
                "title": "Types of AI: Narrow, General, and Super",
                "minutes": 5,
                "summary": "Understand the difference between the AI we have and the AI in science fiction.",
                "content": """AI is usually grouped into three categories based on how broadly it can perform tasks.

### Narrow AI (Artificial Narrow Intelligence, ANI)

This is *all* AI that exists today. Narrow AI is trained to do one thing, or a limited set of things, extremely well: recognizing faces, recommending videos, translating languages, or generating text. Even a system as capable as a modern chatbot is narrow AI — it doesn't have goals, self-awareness, or understanding outside the patterns it learned.

### General AI (Artificial General Intelligence, AGI)

A hypothetical system that could understand, learn, and apply intelligence across *any* task a human can, transferring knowledge between completely different domains the way people do. AGI does not exist yet, and there's active debate among researchers about how close we are, and even how we'd recognize it if we built it.

### Super AI (Artificial Superintelligence, ASI)

An even more hypothetical stage where AI would surpass human intelligence across every domain. This is firmly in the realm of speculation and long-term research and safety discussions, not current technology.

### Why this distinction matters

When you read headlines about AI "understanding" or "thinking," it's easy to imagine AGI-like capabilities. In reality, every AI product today — including the most impressive GenAI tools — is narrow AI operating on patterns learned from data.""",
                "takeaways": [
                    "All AI in production today is Narrow AI — highly capable at specific tasks, not general reasoning.",
                    "AGI (human-level, general-purpose intelligence) remains a research goal, not a shipped product.",
                    "Superintelligence is a speculative, long-horizon concept discussed mostly in AI safety research.",
                ],
            },
            {
                "id": "ai-b-3",
                "title": "Machine Learning vs AI vs Deep Learning",
                "minutes": 6,
                "summary": "Untangle three terms that get used interchangeably — and shouldn't be.",
                "content": """These three terms are nested inside each other like Russian dolls.

### AI (the outermost layer)

The broad goal: building machines that behave intelligently, by any method.

### Machine Learning — ML (a subset of AI)

Instead of programming explicit rules, you show the system many examples and let it learn the patterns itself. A spam filter that improves as it sees more labeled emails is Machine Learning.

### Deep Learning — DL (a subset of ML)

Deep Learning uses artificial neural networks with many layers ("deep" stacks of layers) to learn increasingly abstract representations of data. Early layers might learn to detect edges in an image; deeper layers combine those into shapes, then objects. Deep Learning is responsible for the breakthroughs in image recognition, speech, and language that power modern GenAI.

### Putting it together

```
AI
 └─ Machine Learning
      └─ Deep Learning
           └─ Large Language Models (like the ones behind ChatGPT, Claude, Gemini)
```

Every Large Language Model is a deep learning model, every deep learning model is a machine learning model, and every machine learning model is a form of AI — but the reverse isn't true. A simple chess-playing rule engine from the 1980s is AI, but it's neither ML nor DL.""",
                "takeaways": [
                    "AI is the broad field; Machine Learning is a method within it that learns from data instead of fixed rules.",
                    "Deep Learning is a subset of ML that uses multi-layered neural networks.",
                    "Modern LLMs sit at the innermost layer: AI → ML → Deep Learning → LLMs.",
                ],
            },
            {
                "id": "ai-b-4",
                "title": "How Machines \"Learn\": Data, Models, and Training",
                "minutes": 7,
                "summary": "The core loop behind every machine learning system, explained with no math.",
                "content": """Every machine learning system, no matter how advanced, follows the same basic loop.

### 1. Data

You collect examples relevant to the task — photos labeled "cat" or "dog," emails labeled "spam" or "not spam," or (for today's LLMs) enormous amounts of text from books, websites, and code.

### 2. Model

A model is a mathematical structure with adjustable internal values, called *parameters* or *weights*. Initially these are random, so the model's outputs are essentially noise.

### 3. Training

The model is shown examples repeatedly. Each time, it makes a prediction, compares it to the correct answer, and slightly adjusts its internal parameters to reduce the error — a process called *gradient descent*. Do this millions or billions of times, across massive datasets, and the parameters gradually settle into values that capture real patterns in the data.

### 4. Inference

Once trained, the model is used on new, unseen inputs — this is called *inference*. This is what happens every time you send a message to a chatbot: the trained model runs your input through its learned parameters to produce a response.

### Why this matters for GenAI

Large Language Models follow this exact loop, just at an enormous scale — trained on hundreds of billions of words with parameter counts in the billions or trillions. Understanding this loop demystifies phrases like "the model learned" or "the model was trained on X" that you'll see throughout this course.""",
                "takeaways": [
                    "Training is a repeated loop of predict → compare to the correct answer → adjust internal parameters.",
                    "A model's 'knowledge' is really just the final values of millions/billions of adjustable parameters.",
                    "Inference is using an already-trained model on new inputs — this is what happens when you chat with an AI.",
                ],
            },
        ],
        "intermediate": [
            {
                "id": "ai-i-1",
                "title": "Supervised, Unsupervised, and Reinforcement Learning",
                "minutes": 7,
                "summary": "The three major paradigms machines use to learn from data.",
                "content": """Machine learning approaches differ mainly in what kind of feedback the model gets while training.

### Supervised Learning

The model learns from labeled examples — input paired with the correct output. Show it thousands of emails labeled "spam" or "not spam," and it learns to predict the label for new emails. Most classification and prediction tasks (fraud detection, medical diagnosis support, price prediction) use supervised learning.

### Unsupervised Learning

The model is given data with **no labels** and must find structure on its own — grouping similar items together (clustering) or reducing data to its most important dimensions. Recommendation systems and customer segmentation often start here.

### Reinforcement Learning (RL)

The model (called an *agent*) learns by taking actions in an environment and receiving rewards or penalties, gradually learning a strategy that maximizes reward over time. This is how game-playing AI (like AlphaGo) was trained — and, crucially, it's also how modern LLMs are fine-tuned for helpfulness through a technique called **Reinforcement Learning from Human Feedback (RLHF)**, where human preferences between different model responses become the reward signal.

### Why it matters for GenAI

Today's chatbots are typically trained in stages: a huge unsupervised/self-supervised pretraining phase (predicting the next word in raw text), followed by supervised fine-tuning on curated examples, followed by RLHF to align the model's behavior with what humans actually find helpful and safe.""",
                "takeaways": [
                    "Supervised learning uses labeled input/output pairs; unsupervised learning finds patterns without labels.",
                    "Reinforcement learning trains an agent through rewards and penalties from interacting with an environment.",
                    "Modern LLMs combine all three ideas: self-supervised pretraining, supervised fine-tuning, and RLHF alignment.",
                ],
            },
            {
                "id": "ai-i-2",
                "title": "Neural Networks Explained",
                "minutes": 8,
                "summary": "How layers of simple math units combine to model complex patterns.",
                "content": """A neural network is loosely inspired by biological neurons, but it's really just layers of simple math.

### The basic unit: a neuron

Each artificial neuron takes several numeric inputs, multiplies each by a learned "weight," sums them up, adds a bias, and passes the result through a non-linear *activation function* (like ReLU or sigmoid). That non-linearity is essential — without it, stacking layers would collapse into one simple linear equation, incapable of modeling complex patterns.

### Layers

- **Input layer**: receives the raw data (pixel values, word tokens, etc.)
- **Hidden layers**: intermediate layers that progressively transform the data into more abstract representations
- **Output layer**: produces the final prediction (a class label, a probability distribution over the next word, etc.)

### Why "deep" matters

A network with many hidden layers can represent far more complex functions than a shallow one. In image recognition, early layers might detect edges, middle layers detect shapes, and later layers detect entire objects — each layer building on the abstractions of the last.

### Backpropagation

Training a neural network means adjusting every weight in every layer to reduce prediction error. **Backpropagation** is the algorithm that efficiently calculates how much each individual weight contributed to the error, working backward from the output layer to the input layer, so that gradient descent knows exactly how to adjust each one.

Every modern GenAI model — including Transformers — is built from these same fundamental building blocks, just arranged in far more sophisticated configurations.""",
                "takeaways": [
                    "Neurons compute a weighted sum of inputs, then apply a non-linear activation function.",
                    "Depth (many hidden layers) lets networks learn increasingly abstract representations of data.",
                    "Backpropagation efficiently computes how to adjust every weight to reduce the model's error.",
                ],
            },
            {
                "id": "ai-i-3",
                "title": "The Rise of Deep Learning",
                "minutes": 6,
                "summary": "Why deep learning went from niche research to the foundation of modern AI.",
                "content": """Neural networks were theorized decades before they became practical. Understanding why they finally took off helps explain the current AI moment.

### The ingredients that came together

- **ImageNet and big labeled datasets (2009+)** gave researchers a common, large-scale benchmark to train and compare models on.
- **GPUs** turned out to be extremely good at the parallel matrix math neural networks require — repurposing gaming hardware accelerated training from months to days.
- **AlexNet (2012)** was a deep convolutional neural network that dramatically beat previous approaches on image recognition, convincing the field that "deep" really did matter.
- **Better training techniques** — improved activation functions, regularization, and initialization methods — made it possible to train much deeper networks without them becoming unstable.

### From vision to language

Deep learning's early wins were mostly in computer vision. Language proved harder because text is sequential and context-dependent. Recurrent Neural Networks (RNNs) and LSTMs were the first serious attempts, but they struggled with long-range dependencies and were slow to train because they process text one token at a time.

### The turning point

The 2017 paper "Attention Is All You Need" introduced the **Transformer** architecture, which processes entire sequences in parallel and uses an *attention mechanism* to directly model relationships between any two words in a sequence, regardless of distance. This single architectural shift is the direct ancestor of GPT, Claude, Gemini, and virtually every modern LLM.""",
                "takeaways": [
                    "Deep learning's rise required big datasets, GPU compute, and architectural breakthroughs happening together.",
                    "Early deep learning wins were in computer vision (AlexNet, 2012) before extending to language.",
                    "The 2017 Transformer architecture solved language modeling's long-range dependency and speed problems, enabling modern LLMs.",
                ],
            },
            {
                "id": "ai-i-4",
                "title": "Key AI Terminology You Need to Know",
                "minutes": 6,
                "summary": "A reference glossary of terms you'll see constantly in AI discussions.",
                "content": """Use this as a quick-reference glossary as you go deeper into GenAI, RAG, and prompt engineering.

### Model & training terms

- **Parameters / weights** — the adjustable internal values a model learns during training.
- **Training** — the process of adjusting parameters using data.
- **Fine-tuning** — further training an already-trained model on a smaller, specialized dataset.
- **Inference** — running a trained model on new input to get a prediction or output.
- **Overfitting** — when a model memorizes training data instead of learning generalizable patterns, performing poorly on new data.
- **Epoch** — one complete pass through the entire training dataset.

### Data & representation terms

- **Feature** — an individual measurable input variable used by a model.
- **Embedding** — a numeric vector representation of data (words, images, etc.) that captures semantic meaning, positioning similar items close together in vector space.
- **Token** — a chunk of text (often a word or sub-word piece) that a language model processes as one unit.

### Evaluation terms

- **Accuracy / precision / recall** — common metrics for how well a model's predictions match reality.
- **Benchmark** — a standardized test dataset used to compare different models' performance.
- **Hallucination** — when a generative model produces confident-sounding but false or fabricated output.

Bookmark this lesson — you'll see these terms throughout the rest of this course, especially once you get into GenAI and RAG.""",
                "takeaways": [
                    "Parameters, training, fine-tuning, and inference describe the lifecycle of a model.",
                    "Embeddings and tokens are the numeric building blocks language models actually operate on.",
                    "Hallucination — confident but false output — is a core challenge you'll revisit throughout GenAI and RAG.",
                ],
            },
        ],
        "pro": [
            {
                "id": "ai-p-1",
                "title": "Transformer Architecture Deep Dive",
                "minutes": 10,
                "summary": "The architecture behind every modern LLM, piece by piece.",
                "content": """The Transformer, introduced in "Attention Is All You Need" (2017), is the architecture behind GPT, Claude, Gemini, Llama, and essentially every modern LLM. Here's what's inside.

### Self-attention

The core innovation. For every token in a sequence, self-attention computes how much it should "attend to" every other token, producing a weighted blend of information from across the whole sequence. This lets the model directly capture relationships like pronoun resolution ("it" referring to a noun many words earlier) without the sequential bottleneck of RNNs.

Each token is projected into three vectors: **Query (Q)**, **Key (K)**, and **Value (V)**. Attention scores are computed as a scaled dot product of Q and K, passed through softmax to get weights, which are then used to combine the V vectors.

### Multi-head attention

Rather than computing attention once, the model does it in parallel across multiple "heads," each potentially learning to focus on different types of relationships (syntax, coreference, topic). The results are concatenated and combined.

### Positional encoding

Because self-attention has no inherent sense of word order, positional information is injected separately — either through fixed sinusoidal patterns or learned positional embeddings — so the model knows token order matters.

### Feed-forward layers and residual connections

Each Transformer block combines attention with a position-wise feed-forward network, wrapped in residual ("skip") connections and layer normalization, which stabilize training in very deep networks.

### Decoder-only vs encoder-decoder

Models like GPT and Claude use a **decoder-only** architecture: they predict the next token given everything before it, using masked self-attention so a token can't "see" future tokens. Encoder-decoder architectures (like the original Transformer, or T5) are more common for translation-style tasks with a distinct input and output sequence.

Understanding this architecture is what separates "using AI" from being able to reason about *why* models behave the way they do — including their strengths, blind spots, and failure modes.""",
                "takeaways": [
                    "Self-attention lets every token directly relate to every other token via learned Query/Key/Value projections.",
                    "Multi-head attention runs several attention computations in parallel to capture different relationship types.",
                    "Modern LLMs like GPT and Claude use decoder-only architectures with masked attention for next-token prediction.",
                ],
            },
            {
                "id": "ai-p-2",
                "title": "Scaling Laws and Emergent Abilities",
                "minutes": 8,
                "summary": "Why bigger models trained on more data become predictably — and sometimes surprisingly — better.",
                "content": """One of the most influential findings in modern AI research is that model performance improves in a remarkably predictable way as you scale up three things together.

### The three scaling axes

- **Model size** — number of parameters
- **Dataset size** — amount of training data (tokens)
- **Compute** — total FLOPs spent training

Research from OpenAI (2020) and later DeepMind's "Chinchilla" paper (2022) showed that loss decreases smoothly and predictably as a power-law function of these variables — and, critically, that model size and data size need to scale together. Many earlier large models were significantly *undertrained* relative to their size; Chinchilla showed that a smaller model trained on proportionally more data could outperform a much larger, undertrained one at the same compute budget.

### Emergent abilities

As models cross certain scale thresholds, they sometimes display capabilities that are barely present in smaller models and then appear fairly abruptly — multi-step arithmetic, certain reasoning tasks, or following complex instructions. This is called **emergence**, and it's a subject of active debate: some researchers argue these jumps are real qualitative shifts, while others argue they're partly an artifact of how we measure performance (a smoothly improving underlying metric can look like a sudden jump on a binary "got it right or wrong" metric).

### Why this matters practically

Scaling laws are why AI labs invest so heavily in bigger training runs — the returns have historically been predictable enough to justify massive compute budgets. But scaling isn't infinite: data availability, energy costs, and diminishing returns are pushing the field toward complementary strategies like better data curation, architectural efficiency, and inference-time reasoning techniques rather than raw scale alone.""",
                "takeaways": [
                    "Model performance improves predictably as a power-law function of parameters, data, and compute scaled together.",
                    "Chinchilla scaling laws showed many large models were undertrained relative to their parameter count.",
                    "Emergent abilities appear at certain scale thresholds, though whether they're truly 'sudden' is debated.",
                ],
            },
            {
                "id": "ai-p-3",
                "title": "AI Alignment and Safety Fundamentals",
                "minutes": 8,
                "summary": "Why making models capable and making them safe and aligned are separate problems.",
                "content": """Capability and alignment are two distinct challenges. A highly capable model isn't automatically a safe or aligned one — alignment is the ongoing effort to make sure a model's behavior matches human intentions and values.

### Why alignment is hard

A model pretrained purely to predict the next word on internet text has no inherent notion of "being helpful" or "being honest" — it just learned statistical patterns from an enormous, messy, uncurated corpus that includes both excellent and terrible examples of human behavior. Alignment techniques exist to shape that raw capability toward being helpful, honest, and harmless.

### Common alignment techniques

- **Supervised Fine-Tuning (SFT)** on curated, high-quality example conversations.
- **RLHF (Reinforcement Learning from Human Feedback)** — human raters compare model outputs, and that preference data trains a reward model, which then guides further training.
- **Constitutional AI / RLAIF** — using a set of written principles and AI-generated feedback (rather than only human raters) to scale alignment training.
- **Red-teaming** — deliberately trying to elicit harmful, biased, or unsafe outputs to find and fix weaknesses before deployment.

### Key risk categories practitioners think about

- **Hallucination** — confidently stated false information.
- **Bias** — reproducing or amplifying skewed patterns present in training data.
- **Misuse** — using a capable model for harmful purposes (malware, disinformation, etc.).
- **Prompt injection** — covered in depth in the Prompt Engineering track — where malicious input manipulates a model into ignoring its instructions.
- **Long-term/systemic risk** — more speculative concerns about highly capable future systems being difficult to control or oversee.

### Why this matters for builders

If you're building GenAI or RAG applications, alignment isn't just a research topic — it directly informs practical decisions: how you constrain a model with system prompts, what guardrails you add, how you evaluate outputs before they reach users, and how you handle edge cases where the model might confidently be wrong.""",
                "takeaways": [
                    "Alignment is the effort to make a model's behavior match human intentions — separate from raw capability.",
                    "RLHF and Constitutional AI are the dominant techniques for steering pretrained models toward helpful, honest behavior.",
                    "Practical risks — hallucination, bias, misuse, and prompt injection — directly shape how you should design AI applications.",
                ],
            },
            {
                "id": "ai-p-4",
                "title": "Evaluating Model Performance Like a Pro",
                "minutes": 9,
                "summary": "Move beyond 'it feels smart' to rigorous, repeatable model evaluation.",
                "content": """Anyone can tell a strong model from a weak one after a few prompts. Professionals build systematic evaluation ("evals") so quality can be measured, tracked, and improved over time.

### Benchmark-based evaluation

Standardized datasets like MMLU (broad knowledge), HumanEval (code generation), or GSM8K (math word problems) let you compare models on fixed, repeatable tasks. Useful for comparing raw model capability, but often a poor proxy for how a model performs on *your* specific application.

### Task-specific evals

The gold standard for production systems: build an evaluation set from real or realistic examples of *your* use case, with either:

- **Reference-based scoring** — compare output to a known correct answer (exact match, ROUGE/BLEU overlap, or embedding similarity).
- **LLM-as-judge** — use a strong model to score another model's output against a rubric. Efficient and scalable, but requires care to avoid the judge's own biases skewing results.
- **Human evaluation** — the most reliable but slowest and most expensive; often reserved for final validation or particularly high-stakes tasks.

### Key dimensions to measure

- **Correctness/faithfulness** — is the output factually accurate (crucial for RAG systems)?
- **Relevance** — does it actually address what was asked?
- **Consistency** — does the model give similar-quality answers to similar prompts?
- **Safety** — does it avoid harmful, biased, or policy-violating content?
- **Latency and cost** — non-negotiable in production, even if quality is excellent.

### Avoiding common pitfalls

- Don't evaluate only on "easy" cases — build adversarial and edge-case examples into your eval set.
- Watch for **eval set leakage** — if your eval examples were part of a model's training data, scores will be misleadingly high.
- Re-run evals whenever you change prompts, models, or retrieval logic — regressions are easy to introduce invisibly.

Systematic evaluation is what separates "vibes-based" AI development from a defensible, iterable engineering practice — and it's essential once you move into building real RAG and GenAI applications.""",
                "takeaways": [
                    "General benchmarks (MMLU, HumanEval) measure raw capability but rarely reflect your specific application's needs.",
                    "Task-specific eval sets — scored by reference comparison, LLM-as-judge, or humans — are the production standard.",
                    "Correctness, relevance, consistency, safety, latency, and cost should all be tracked, not just 'does it sound good.'",
                ],
            },
        ],
    },
    "genai": {
        "basics": [
            {
                "id": "genai-b-1",
                "title": "What Makes AI \"Generative\"?",
                "minutes": 6,
                "summary": "The difference between AI that classifies and AI that creates.",
                "content": """Most classic AI systems are **discriminative**: given an input, they classify or predict something about it — is this email spam, is this a photo of a cat, will this customer churn. They choose among a fixed set of possible answers.

**Generative AI** is different: it creates new content — text, images, audio, video, or code — that didn't exist before, by learning the underlying patterns and structure of its training data well enough to produce plausible new examples in that same style.

### How generation actually works (conceptually)

A generative model learns a probability distribution over possible outputs. For text, that means: given everything written so far, what's the probability distribution over the next word? Generation is the repeated process of sampling from that distribution, one piece at a time, using each new piece to inform the next prediction.

For images, different techniques (like diffusion models) learn to reverse a process of gradually adding noise to an image, effectively learning how to "denoise" random static into a coherent picture that matches a text description.

### Why this shift matters

Generative AI turns models from *classifiers* into *creative collaborators and tools* — drafting text, writing code, generating art, summarizing documents, or answering open-ended questions in natural language, rather than just picking from a predefined list of labels.

### Not magic, still pattern-matching

It's tempting to describe generative models as "understanding" or "thinking." Under the hood, they're sophisticated pattern-completion systems: extremely good at producing statistically plausible continuations based on their training data, which is why they can both dazzle you with a fluent, useful answer and confidently produce something completely wrong (a hallucination) in the same conversation.""",
                "takeaways": [
                    "Discriminative AI classifies/predicts from fixed options; generative AI creates new content.",
                    "Text generation works by repeatedly sampling from a learned probability distribution over the next token.",
                    "Generative models are powerful pattern-completion systems, not understanding in the human sense — which is why hallucinations happen.",
                ],
            },
            {
                "id": "genai-b-2",
                "title": "Large Language Models (LLMs) 101",
                "minutes": 7,
                "summary": "What an LLM is, and how it turns text in to text out.",
                "content": """A Large Language Model is a deep learning model, almost always Transformer-based, trained on enormous amounts of text to predict the next piece of text given everything before it.

### From text to numbers and back

1. **Tokenization**: your input text is broken into tokens (often sub-word pieces, e.g. "generation" might become "gener" + "ation").
2. **Embedding**: each token is converted into a numeric vector.
3. **Processing**: the vectors pass through many Transformer layers, where self-attention lets the model weigh the relevance of every other token to build contextual understanding.
4. **Prediction**: the model outputs a probability distribution over its entire vocabulary for "what token comes next."
5. **Sampling**: a token is chosen from that distribution (more on sampling strategies in the Intermediate lessons), appended to the sequence, and the process repeats — one token at a time — until the response is complete.

### "Large" refers to scale

LLMs typically have billions to hundreds of billions of parameters, trained on datasets spanning a meaningful fraction of publicly available text, code, and increasingly curated high-quality data — which is why training them requires massive compute infrastructure.

### What LLMs are (and aren't) good at

LLMs excel at tasks rooted in language patterns: writing, summarizing, translating, explaining, brainstorming, and increasingly, reasoning through multi-step problems. They're less reliable at tasks requiring precise, up-to-date factual recall beyond their training data (this is exactly the gap RAG is designed to fill — covered in the RAG track) or exact arithmetic on large numbers, though many modern models offset this by calling external tools.""",
                "takeaways": [
                    "LLMs generate text one token at a time by repeatedly predicting the most likely next token given context.",
                    "The pipeline is: tokenize → embed → process through Transformer layers → predict next-token probabilities → sample.",
                    "LLMs are strongest at language-pattern tasks and weaker at precise, up-to-date facts or exact math without external tools.",
                ],
            },
            {
                "id": "genai-b-3",
                "title": "Text, Image, Audio, and Video Generation",
                "minutes": 6,
                "summary": "A tour of the major modalities generative AI can now produce.",
                "content": """Generative AI has expanded well beyond text. Here's a quick tour of the main modalities and the dominant approach behind each.

### Text generation

Powered by LLMs (GPT, Claude, Gemini, Llama, and others), used for writing, chat, summarization, translation, code generation, and reasoning tasks.

### Image generation

Dominated by **diffusion models** (Midjourney, Stable Diffusion, DALL·E). These start from random noise and iteratively "denoise" it, guided by a text prompt, until a coherent image emerges. Each denoising step is guided by a model that has learned what realistic images look like at various levels of noise.

### Audio generation

Includes text-to-speech (natural-sounding voice synthesis), music generation, and sound effect generation. Modern systems can clone voices, generate expressive speech with controllable tone, and compose original music from text descriptions.

### Video generation

The newest and most computationally demanding modality — models like Sora and Veo extend diffusion-style approaches across time, needing to maintain consistency of objects, lighting, and physics across many frames, which is dramatically harder than generating a single coherent image.

### Multimodal models

Increasingly, a single model can handle several modalities at once — accepting an image and text together, or generating both. This is covered in more depth in the Intermediate lesson on multimodal models.

### A common thread

Regardless of modality, the same core idea applies: a model learns the statistical structure of a huge dataset well enough to generate new, plausible examples that follow that structure — whether that structure is "how words follow each other" or "how pixels are arranged in a photo".""",
                "takeaways": [
                    "Text generation uses LLMs; images and increasingly video use diffusion-based denoising approaches.",
                    "Video generation is the hardest modality because it must maintain consistency across many frames over time.",
                    "Every modality shares the same underlying idea: learning a dataset's statistical structure well enough to generate new examples.",
                ],
            },
            {
                "id": "genai-b-4",
                "title": "Popular GenAI Tools and Models",
                "minutes": 5,
                "summary": "A practical map of the GenAI landscape as of today.",
                "content": """It's easy to get lost in the number of GenAI products available. Here's a practical map of the main categories.

### General-purpose chat assistants

Claude, ChatGPT, and Gemini are LLM-based assistants for writing, coding, research, analysis, and conversation. They differ in areas like context window size, reasoning approach, safety philosophy, and available tool integrations, but they all share the same fundamental Transformer-based LLM foundation.

### Coding assistants

Tools like GitHub Copilot and Claude Code integrate LLMs directly into the developer workflow — autocompleting code, explaining unfamiliar codebases, writing tests, and increasingly acting as autonomous coding agents that can run commands and iterate on their own.

### Image and design generation

Midjourney, DALL·E, and Stable Diffusion generate images from text prompts; tools built on top of them add editing, upscaling, and style-consistency features for design and marketing workflows.

### Developer platforms and APIs

Anthropic, OpenAI, and Google all expose their models via APIs, which is how the "React frontend + Python backend" pattern you're learning in this course typically works in production — your backend calls a model API and returns the result to your app.

### Open-weight models

Models like Llama, Mistral, and Qwen have publicly released weights, letting developers self-host and fine-tune them rather than relying solely on a hosted API — trading convenience for control, cost predictability, and data privacy.

### A note on this course

Understanding this landscape matters, but the deeper skill — which this course focuses on — is understanding *how* these tools work underneath, so you can build effective applications regardless of which specific model or vendor you choose.""",
                "takeaways": [
                    "General-purpose assistants (Claude, ChatGPT, Gemini) share the same LLM foundation but differ in capabilities and philosophy.",
                    "Developer APIs are how GenAI features get embedded into real applications like the one you're building in this course.",
                    "Open-weight models trade some convenience for self-hosting control, cost predictability, and data privacy.",
                ],
            },
        ],
        "intermediate": [
            {
                "id": "genai-i-1",
                "title": "How LLMs Generate Text: Tokens and Sampling",
                "minutes": 8,
                "summary": "The mechanics of temperature, top-p, and why the same prompt can give different answers.",
                "content": """You've seen that LLMs generate text by repeatedly predicting a probability distribution over the next token. How that distribution turns into an actual chosen token is controlled by sampling parameters that meaningfully change output behavior.

### Temperature

Temperature reshapes the probability distribution before sampling. Low temperature (near 0) sharpens the distribution toward the single most likely token, producing focused, deterministic, "safe" output. High temperature flattens the distribution, giving lower-probability tokens a better chance of being picked — producing more varied, creative, occasionally erratic output. Temperature 0 typically means "always pick the most likely token" (greedy decoding).

### Top-p (nucleus sampling)

Instead of considering the entire vocabulary, top-p restricts sampling to the smallest set of tokens whose cumulative probability exceeds a threshold *p* (e.g., 0.9), then samples only from that "nucleus." This adapts dynamically — when the model is very confident, the nucleus is small; when it's uncertain, the nucleus is larger.

### Top-k

A simpler cousin: only consider the *k* most likely tokens at each step, regardless of their cumulative probability, then sample among them.

### Why the same prompt gives different answers

Unless temperature is set to 0 and sampling is deterministic, generation involves genuine randomness at each token step — which is why re-running the exact same prompt can produce different (though usually similarly-toned) responses. This matters practically: if you need reproducible output (e.g., for testing), lower temperature; if you want creative variety (e.g., brainstorming), raise it.

### Token limits and stopping

Generation continues until the model produces a special "end of sequence" token, hits a configured maximum token limit, or hits a defined stop sequence — all configurable parameters when calling an LLM API, directly relevant when you build the Python backend for a GenAI app.""",
                "takeaways": [
                    "Temperature controls randomness: low values are focused and deterministic, high values are varied and creative.",
                    "Top-p (nucleus) and top-k sampling restrict which tokens are eligible to be chosen at each generation step.",
                    "Non-zero temperature introduces genuine randomness, which is why identical prompts can yield different responses.",
                ],
            },
            {
                "id": "genai-i-2",
                "title": "Fine-Tuning vs Prompting vs RAG",
                "minutes": 8,
                "summary": "Three different ways to customize a model's behavior — and when to use each.",
                "content": """When you want an LLM to behave differently from its default — knowing your company's product details, following a specific tone, or staying current with new information — you generally have three tools available, and they solve different problems.

### Prompting (including prompt engineering)

Simply instructing the model, in your input, how to behave: tone, format, role, constraints, and examples. It's fast, cheap, requires no training infrastructure, and is fully reversible per-request. Its limitation is the context window — you can only include so much instruction and reference material in a single prompt, and it doesn't fundamentally change the model's underlying knowledge.

### RAG (Retrieval-Augmented Generation)

Rather than relying on what the model memorized during training, RAG retrieves relevant, up-to-date documents at query time and inserts them into the prompt as context, letting the model "read" fresh, specific information before answering. Ideal when you need the model to reason over your own data, or information that changes frequently or postdates training. Covered in full depth in the RAG track.

### Fine-tuning

Continuing the training process on a smaller, specialized dataset to adjust the model's weights directly — changing *how* it responds (style, format, domain-specific reasoning patterns) rather than just what it knows. Useful when you need consistent behavior that would be expensive or unreliable to enforce via prompting alone, but it requires training infrastructure, a quality dataset, and retraining whenever the underlying facts change.

### Choosing between them

A practical rule of thumb: reach for **prompting** first (cheapest, fastest to iterate), add **RAG** when the model needs access to specific or current knowledge it wasn't trained on, and reach for **fine-tuning** when you need a persistent change in behavior, format, or style that prompting can't reliably achieve. In production systems, these are frequently combined — a fine-tuned model using RAG with well-engineered prompts is a common, powerful pattern.""",
                "takeaways": [
                    "Prompting changes behavior per-request, cheaply, but is limited by the context window and doesn't add new knowledge.",
                    "RAG injects fresh, specific information into the prompt at query time — ideal for current or proprietary data.",
                    "Fine-tuning changes the model's weights for persistent behavior/style changes, but needs infrastructure and a quality dataset.",
                ],
            },
            {
                "id": "genai-i-3",
                "title": "Context Windows and Their Limits",
                "minutes": 6,
                "summary": "Why models can \"forget\" things, and how context size shapes application design.",
                "content": """The **context window** is the maximum amount of text (measured in tokens) a model can consider at once — spanning your system prompt, conversation history, any retrieved documents, and the response being generated, all combined.

### Why it exists

Self-attention, the mechanism at the heart of Transformers, computes relationships between every pair of tokens in the input. Naively, that means computational cost grows quadratically with sequence length — doubling your input roughly quadruples the compute required for attention. This is a core reason context windows have historical limits, though architectural and engineering advances have pushed windows from a few thousand tokens to hundreds of thousands, and in some models, millions.

### What happens at the limit

Once a conversation or input exceeds the context window, something has to give — older messages might be truncated or summarized, or the request may simply fail. This is why long-running chatbot conversations can seem to "forget" early context, and why applications handling large documents need a deliberate strategy (like RAG's chunking and retrieval, rather than dumping an entire document into the prompt).

### The "lost in the middle" effect

Even within the context window, research has shown models don't always weigh all parts of a long input equally — information placed at the very beginning or end of a long context is often utilized more reliably than information buried in the middle. This has direct, practical implications for how you structure prompts and where you place the most important information.

### Practical implications

- Larger context windows are not a free pass to skip good retrieval and context curation — relevant, well-organized context still outperforms dumping everything in.
- Cost and latency generally scale with the number of tokens processed, so bigger isn't always better for production applications.
- Understanding context limits is essential before you design a RAG system, since chunking and retrieval strategy exist specifically to work within this constraint.""",
                "takeaways": [
                    "The context window is the total token budget for prompt + history + retrieved content + response combined.",
                    "Self-attention's computational cost grows with sequence length, historically limiting how large context windows can be.",
                    "Models don't weigh all context equally — the 'lost in the middle' effect means placement of key info matters.",
                ],
            },
            {
                "id": "genai-i-4",
                "title": "Multimodal Models Explained",
                "minutes": 6,
                "summary": "How a single model can understand images, text, and more together.",
                "content": """A **multimodal model** can process and/or generate more than one type of data — typically text combined with images, and increasingly audio and video — within a single unified model.

### How multimodality works (conceptually)

The key idea is projecting different modalities into a **shared representation space**. An image is broken into patches and encoded into vectors; text is tokenized and embedded into vectors. Both sets of vectors are then processed together (often by the same Transformer backbone), allowing the model to relate a described object in text directly to its visual representation in an image.

### What multimodal models unlock

- **Visual question answering** — "what's happening in this image?" or "read the text in this screenshot."
- **Document understanding** — processing PDFs, charts, and scanned documents that mix text and visual layout.
- **Grounded generation** — generating text that accurately references and describes provided visual content.
- **Cross-modal generation** — text-to-image, image-to-text, and increasingly text-to-video or text-to-audio.

### Why this matters for application builders

Multimodal input means your GenAI application isn't limited to text boxes — users can upload a screenshot, a chart, or a document and get the model to reason over it directly. This is increasingly a baseline capability of frontier assistants rather than a specialized add-on.

### Current limitations

Multimodal reasoning is generally less mature than text reasoning — models can still misread charts, miscount objects, or misinterpret spatial relationships. When building applications where visual accuracy really matters (e.g., reading precise numbers off a chart), it's worth validating outputs carefully rather than assuming multimodal answers are as reliable as well-grounded text answers.""",
                "takeaways": [
                    "Multimodal models project different data types (text, images) into a shared representation space they can reason over together.",
                    "Capabilities include visual Q&A, document understanding, and cross-modal generation like text-to-image.",
                    "Visual/spatial reasoning is still less mature than text reasoning — validate outputs for precision-critical tasks.",
                ],
            },
        ],
        "pro": [
            {
                "id": "genai-p-1",
                "title": "Model Architectures: GPT, Claude, Gemini, and Beyond",
                "minutes": 9,
                "summary": "How the leading frontier model families differ under the hood.",
                "content": """While all frontier LLMs share a Transformer foundation, labs differentiate through architecture choices, training data curation, and alignment methodology. Vendors rarely disclose full architectural details for frontier models, but the general design philosophies are informative.

### Shared foundation

Decoder-only Transformer architecture, trained via next-token prediction on massive text (and increasingly code, and multimodal) corpora, followed by supervised fine-tuning and preference-based alignment (RLHF or similar). This is common across GPT, Claude, Gemini, and Llama.

### Where labs differentiate

- **Training data composition and curation** — the mix of web text, books, code, licensed data, and synthetic data significantly shapes model behavior and capability, and is one of the most closely guarded aspects of frontier training.
- **Alignment philosophy** — Anthropic's Constitutional AI trains models against a written set of principles combined with AI-generated feedback (RLAIF), aiming for more scalable, transparent alignment compared to relying purely on human raters.
- **Context window engineering** — achieving very long context windows requires architectural and systems work (efficient attention variants, memory management) beyond simply “using a bigger Transformer.”
- **Mixture-of-Experts (MoE)** — some frontier models use MoE architectures, where only a subset of specialized "expert" sub-networks activate for any given input, allowing much larger total parameter counts while keeping the compute cost per token manageable.
- **Reasoning/inference-time compute** — newer model variants are trained to "think" through intermediate reasoning steps before answering (sometimes called extended or chain-of-thought reasoning), trading additional inference-time compute for improved accuracy on complex problems.

### Why architectural literacy matters for builders

You don't need to reproduce these architectures to build great applications, but understanding *why* models differ helps you choose the right model for a task (e.g., a fast, cheap model for simple classification vs. an extended-reasoning model for complex multi-step analysis) and interpret vendor documentation and benchmarks critically rather than treating "bigger number" as automatically "better for my use case".""",
                "takeaways": [
                    "All frontier LLMs share a Transformer + next-token prediction + alignment foundation, but differ in data, alignment method, and engineering.",
                    "Mixture-of-Experts architectures activate only a subset of the model per token, enabling scale without proportional compute cost.",
                    "Extended/reasoning-focused model variants trade inference-time compute for better accuracy on complex, multi-step problems.",
                ],
            },
            {
                "id": "genai-p-2",
                "title": "Building GenAI Applications: Architecture Patterns",
                "minutes": 10,
                "summary": "Common production architectures for shipping real GenAI features — including the one behind this course's app.",
                "content": """Moving from "calling an API in a notebook" to a production GenAI application involves recurring architecture patterns. Here are the ones you'll encounter most often — including a version of what powers this very course's app (React frontend + Python backend).

### The basic pattern: thin client, backend-orchestrated

The frontend (React, in this course) handles UI and user interaction, but never calls the model API directly with your secret API key exposed in the browser. Instead, it calls your own backend (Python/FastAPI, in this course), which holds credentials securely, calls the model provider's API, applies any business logic, and returns a clean response to the frontend. This is the standard, secure pattern for any real GenAI product.

### Adding retrieval (RAG pattern)

The backend, before calling the LLM, first queries a vector database (or other retrieval system) for relevant context, then constructs a prompt that combines the user's question with retrieved content, then calls the LLM. Covered in full depth in the RAG track.

### Adding tools/function calling

Modern LLM APIs support **tool use**: the model can request that your backend execute a specific function (e.g., "look up order #1234," "run this calculation," "search the web") and receives the result back to incorporate into its final answer. This is the foundation of agentic applications, where a model can take multi-step actions rather than just responding to a single prompt.

### Streaming responses

Because generation happens token-by-token, production applications typically **stream** partial output to the frontend as it's generated (rather than waiting for the entire response), dramatically improving perceived responsiveness. This requires backend support for streaming APIs and frontend handling of incremental updates (e.g., via Server-Sent Events or chunked HTTP responses).

### Guardrails and observability

Production systems typically add: input validation and moderation, output filtering, rate limiting, prompt injection defenses, structured logging of prompts/responses for debugging, and evaluation pipelines to catch regressions — all sitting in the backend layer between your users and the underlying model API.

### Why this matters for this course's app

The app you're building right now follows this exact backend-orchestrated pattern: a Python API serving content to a React frontend, with a clean separation between UI and business logic — the same separation you'd extend with retrieval, tool use, and streaming as you build more advanced GenAI features.""",
                "takeaways": [
                    "Production GenAI apps route model calls through a backend that holds API credentials, never exposing them to the browser.",
                    "Tool/function calling lets a backend give the model the ability to take multi-step actions, forming the basis of agentic systems.",
                    "Streaming responses, guardrails, and observability are what separate a demo from a production-grade GenAI application.",
                ],
            },
            {
                "id": "genai-p-3",
                "title": "Cost, Latency, and Token Economics",
                "minutes": 8,
                "summary": "The practical engineering constraints that shape every real GenAI product decision.",
                "content": """Building a GenAI feature that works in a demo is very different from building one that's fast, affordable, and reliable at scale. Token economics sit at the center of that gap.

### How pricing works

Most LLM APIs charge per token, typically with separate (and different) rates for input tokens and output tokens — output tokens are usually more expensive since they require sequential generation. Costs scale directly with how much context you send (system prompt, conversation history, retrieved documents) and how long the response is.

### Levers for controlling cost

- **Right-sizing the model** — use a smaller, cheaper, faster model for simple tasks (classification, extraction, simple Q&A) and reserve larger, more expensive models for genuinely complex reasoning.
- **Prompt trimming** — avoid sending unnecessary context; in RAG systems, this means tuning how many chunks you retrieve and how large they are.
- **Caching** — many providers offer prompt/context caching, charging less for reprocessing content that hasn't changed between requests (like a long, static system prompt).
- **Output length limits** — constraining max tokens both controls cost and can improve perceived latency.
- **Batching** — for non-real-time workloads, batch APIs often offer discounted pricing in exchange for asynchronous processing.

### Latency considerations

Latency in LLM applications comes from two main sources: **time-to-first-token** (how long before generation starts, affected by input length and model load) and **generation speed** (tokens per second, affected by model size and output length). Streaming (covered in the previous lesson) doesn't reduce total latency but dramatically improves perceived responsiveness by showing partial output immediately.

### Designing for the real cost/quality/speed triangle

Every production GenAI decision trades off between cost, latency, and quality. A common professional pattern is **tiered routing**: send simple requests to a fast, cheap model, and escalate to a more capable (and expensive) model only when needed — sometimes using a cheap model to first classify request complexity. This kind of deliberate engineering is what separates a sustainable GenAI product from one with an unpredictable, runaway API bill.""",
                "takeaways": [
                    "LLM APIs typically charge per input and output token, with output tokens usually costing more.",
                    "Right-sizing models, trimming context, caching, and output limits are the main levers for controlling GenAI costs.",
                    "Tiered routing — sending simple requests to cheaper models and escalating only when needed — balances cost, latency, and quality.",
                ],
            },
            {
                "id": "genai-p-4",
                "title": "Evaluating and Benchmarking GenAI Outputs",
                "minutes": 9,
                "summary": "Rigorous techniques for measuring generative quality, where there's rarely one 'correct' answer.",
                "content": """Evaluating generative output is harder than evaluating a classifier: there's often no single correct answer, and quality is multi-dimensional (accuracy, tone, completeness, safety, formatting). Professional GenAI evaluation combines several complementary techniques.

### Automatic metrics (limited but fast)

Traditional NLP metrics like BLEU and ROUGE measure word/phrase overlap with a reference answer. They're fast and cheap but correlate weakly with actual quality for open-ended generation — a paraphrased, equally correct answer can score poorly simply for using different words.

### Embedding-based similarity

Comparing the embedding vectors of generated output and a reference answer captures semantic similarity beyond exact word overlap, offering a better (though still imperfect) automatic signal than pure lexical overlap metrics.

### LLM-as-judge

Using a strong model to score outputs against an explicit rubric (e.g., "rate this response 1-5 on factual accuracy, and 1-5 on helpfulness, given this reference context") scales far better than human evaluation and correlates reasonably well with human judgment when the rubric and judge model are chosen carefully. Known pitfalls include position bias (favoring the first of two compared outputs), verbosity bias (favoring longer answers), and self-preference bias (a model favoring outputs similar to its own style).

### Human evaluation

Still the gold standard for nuanced quality judgments, especially for subjective dimensions (tone, creativity, cultural appropriateness) or high-stakes domains. Typically used to validate that automatic/LLM-judge metrics are actually correlated with real quality, and for final sign-off before major releases.

### Building a robust eval suite

- Curate a diverse, representative set of test cases, including edge cases and adversarial examples.
- Track metrics over time as prompts, models, or retrieval logic change — evaluation should be a continuous practice, not a one-time check.
- Combine multiple signals (automatic + LLM-judge + periodic human review) rather than relying on just one.
- For RAG specifically, separately evaluate *retrieval quality* (did we find the right documents?) and *generation quality* (did the model use them well?) — covered further in the RAG Pro lessons.

Rigorous evaluation is what turns "this feels better" into a defensible, data-backed decision — essential once a GenAI feature moves from prototype to something real users depend on.""",
                "takeaways": [
                    "Traditional overlap metrics (BLEU/ROUGE) correlate weakly with true generative quality; embedding similarity is a better automatic proxy.",
                    "LLM-as-judge scales evaluation well but has known biases (position, verbosity, self-preference) that must be controlled for.",
                    "Robust evaluation combines automatic metrics, LLM-judges, and periodic human review, tracked continuously as the system changes.",
                ],
            },
        ],
    },
    "rag": {
        "basics": [
            {
                "id": "rag-b-1",
                "title": "What is RAG and Why Does It Matter?",
                "minutes": 6,
                "summary": "The core idea behind Retrieval-Augmented Generation, in plain terms.",
                "content": """LLMs only "know" what was in their training data, frozen at the time training ended. They can't natively answer questions about your private documents, yesterday's news, or anything that changed after training — and when they don't know something, they sometimes guess confidently instead of admitting uncertainty (a hallucination).

**Retrieval-Augmented Generation (RAG)** solves this by combining two systems:

1. A **retrieval system** that searches a knowledge base (your documents, a database, the web) for content relevant to the user's question.
2. A **generation system** (an LLM) that reads the retrieved content alongside the question and produces an answer grounded in that content.

### The basic flow

```
User question
    ↓
Retrieve relevant documents/chunks from a knowledge base
    ↓
Combine question + retrieved content into a prompt
    ↓
LLM generates an answer using that context
    ↓
Answer (ideally with citations back to source documents)
```

### Why this matters

RAG lets you build AI applications that answer questions about *your* data — internal documentation, product manuals, legal contracts, customer support history — without retraining or fine-tuning the underlying model. It also reduces (though doesn't eliminate) hallucination, because the model is generating from provided context rather than purely from memorized training data, and it makes answers auditable, since you can show which source documents were used.

### A simple analogy

Think of a talented writer who's never read your company's internal wiki. Instead of trying to memorize the whole wiki (fine-tuning), you hand them the three most relevant pages right before they answer your question (RAG) — they can write a great, accurate answer using material they just read, even though they'd never seen it before.""",
                "takeaways": [
                    "RAG combines a retrieval system (finds relevant content) with a generation system (LLM writes the answer) to ground responses in real data.",
                    "RAG lets models answer questions about private or current data without retraining, and reduces hallucination by grounding answers in retrieved context.",
                    "The basic flow is: retrieve relevant content → insert it into the prompt → generate an answer grounded in that content.",
                ],
            },
            {
                "id": "rag-b-2",
                "title": "Embeddings: Turning Text into Numbers",
                "minutes": 7,
                "summary": "The numeric representation that makes semantic search possible.",
                "content": """RAG's retrieval step depends on being able to find content that's *semantically* relevant to a question — not just content that shares exact keywords. That's what embeddings make possible.

### What an embedding is

An **embedding** is a list of numbers (a vector — often several hundred to a few thousand dimensions) that represents a piece of text's meaning. An embedding model is trained so that texts with similar meaning end up with vectors that are close together in that high-dimensional space, while unrelated texts end up far apart.

### A simplified intuition

Imagine a (drastically simplified) 2D space where "dog" and "puppy" land near each other, "cat" lands nearby but slightly further, and "spreadsheet" lands far away in a completely different region. Real embedding models use hundreds of dimensions to capture far more nuanced relationships than a 2D picture could, but the core intuition — *semantic closeness maps to geometric closeness* — holds.

### Measuring similarity

Once text is embedded as vectors, you can mathematically measure how similar two pieces of text are — most commonly using **cosine similarity**, which measures the angle between two vectors regardless of their magnitude, producing a score typically between -1 and 1 (or 0 to 1 for many embedding models), where higher means more similar.

### Why this enables retrieval

To build a RAG system, you embed all your knowledge base content in advance and store the vectors. When a user asks a question, you embed *the question* using the same embedding model, then find the stored vectors closest to it — those correspond to the most semantically relevant pieces of your knowledge base, even if they don't share exact keywords with the question. That's a dramatic improvement over old-fashioned keyword search for many use cases, though (as you'll see in the Intermediate lessons) the best systems often combine both approaches.""",
                "takeaways": [
                    "Embeddings represent text as numeric vectors, where semantically similar text produces vectors that are close together.",
                    "Cosine similarity is the standard way to measure how close two embedding vectors — and thus two pieces of text — are.",
                    "RAG retrieval works by embedding a knowledge base in advance, then finding the closest stored vectors to an embedded question.",
                ],
            },
            {
                "id": "rag-b-3",
                "title": "Vector Databases 101",
                "minutes": 6,
                "summary": "Where all those embeddings actually live, and how they're searched efficiently.",
                "content": """Once you've embedded your knowledge base into vectors, you need somewhere to store them and search them efficiently — that's the job of a **vector database**.

### Why not just use a regular database?

A traditional database is optimized for exact matches and range queries (find rows where price < 50). Vector search needs something different: given a query vector, find the *k nearest* vectors in a high-dimensional space, out of potentially millions of stored vectors, fast. Checking every single vector one by one (brute-force search) becomes too slow at scale, so vector databases use specialized indexing structures.

### Approximate Nearest Neighbor (ANN) search

Most vector databases use ANN algorithms — commonly **HNSW** (Hierarchical Navigable Small World graphs) — which build a graph-like index that lets you find *very close to* the true nearest neighbors dramatically faster than brute-force search, trading a small amount of accuracy for a large gain in speed.

### Popular vector database options

- **Managed/hosted**: Pinecone, Weaviate Cloud, Qdrant Cloud
- **Self-hosted/open-source**: Qdrant, Weaviate, Milvus, Chroma
- **Add-ons to existing databases**: pgvector (PostgreSQL extension), Elasticsearch/OpenSearch vector search, Redis vector search

### What a vector database stores per entry

Typically, alongside the embedding vector itself, you store the original text chunk and useful **metadata** (source document, page number, date, category) so that once you retrieve a relevant chunk, you can display it, cite it, or filter results by metadata (e.g., "only search documents from this year").

### Choosing one in practice

For learning and small projects, lightweight options like Chroma (which can even run in-process) are excellent starting points. For production systems with large-scale data, filtering needs, and uptime requirements, managed solutions or dedicated self-hosted systems like Qdrant or Milvus are more common choices — the right choice depends on data scale, latency needs, and operational preferences.""",
                "takeaways": [
                    "Vector databases are optimized to find the nearest vectors to a query vector efficiently, unlike traditional exact-match databases.",
                    "Most use Approximate Nearest Neighbor algorithms like HNSW to trade a little accuracy for a lot of speed at scale.",
                    "Entries typically store the vector, original text, and metadata together, enabling retrieval, citation, and filtering.",
                ],
            },
            {
                "id": "rag-b-4",
                "title": "A Simple RAG Pipeline Walkthrough",
                "minutes": 8,
                "summary": "Trace a question through an entire RAG system, end to end.",
                "content": """Let's walk through a complete, minimal RAG pipeline from raw documents to a final answer.

### Step 1 — Ingestion (done in advance, offline)

1. Collect your source documents (PDFs, wiki pages, support tickets, etc.).
2. Split ("chunk") each document into smaller pieces — typically a few hundred tokens each — since embedding and retrieving whole documents is usually too coarse (more on chunking strategy in the Intermediate lessons).
3. Generate an embedding vector for each chunk using an embedding model.
4. Store each chunk's text, embedding, and metadata in a vector database.

### Step 2 — Query time (happens live, per user question)

1. The user asks a question through your application.
2. Your backend embeds the question using the *same* embedding model used during ingestion (this consistency is essential — mixing embedding models breaks similarity comparisons).
3. The vector database is queried for the top-*k* chunks most similar to the question's embedding.
4. Those chunks are inserted into a prompt template, typically structured like: *"Using only the following context, answer the question. Context: [retrieved chunks]. Question: [user's question]."*
5. The completed prompt is sent to an LLM, which generates an answer grounded in the retrieved context.
6. The answer (ideally with citations back to source chunks) is returned to the user.

### Where this maps to a real application

If you were to build this as a full-stack app: document ingestion and embedding could be a one-time Python script; the vector database could be Chroma or Postgres with pgvector; your FastAPI backend would handle step 2 end-to-end; and your React frontend would send the question and display the streamed answer with source citations.

### Common first-attempt mistakes

- Using inconsistent embedding models between ingestion and query time.
- Chunks that are too large (diluting relevance) or too small (losing necessary context) — covered in depth next.
- Not instructing the model clearly to rely on the provided context, which can lead it to blend retrieved facts with its own (possibly outdated or incorrect) memorized knowledge.""",
                "takeaways": [
                    "RAG splits into an offline ingestion phase (chunk, embed, store) and a live query phase (embed question, retrieve, generate).",
                    "The same embedding model must be used for both ingestion and querying, or similarity comparisons break down.",
                    "A clear prompt instructing the model to rely on retrieved context helps prevent it from blending in outdated memorized knowledge.",
                ],
            },
        ],
        "intermediate": [
            {
                "id": "rag-i-1",
                "title": "Chunking Strategies for Better Retrieval",
                "minutes": 8,
                "summary": "Why how you split documents dramatically affects RAG quality.",
                "content": """Chunking — how you split source documents before embedding — is one of the highest-leverage decisions in a RAG system, and it's easy to underestimate.

### Why chunk size matters

- **Too large**: a chunk covers multiple unrelated topics, diluting its embedding's specificity and making it less likely to rank highly for a focused question — and it wastes context window space with irrelevant text once retrieved.
- **Too small**: a chunk loses necessary surrounding context, potentially retrieving a sentence fragment that's technically relevant but not usable/understandable on its own.

### Common chunking strategies

- **Fixed-size chunking**: split every N tokens/characters, often with overlap between consecutive chunks (e.g., 500 tokens with 50 tokens of overlap) so content near chunk boundaries isn't orphaned. Simple and predictable, but ignores document structure.
- **Recursive/structure-aware chunking**: split along natural boundaries — paragraphs, then sentences if a paragraph is still too long — preserving more coherent units of meaning than blind fixed-size splitting.
- **Semantic chunking**: use embeddings to detect where topic shifts occur in a document, and split at those boundaries rather than at arbitrary length limits.
- **Document-aware chunking**: respect existing structure like Markdown headers, HTML sections, or table boundaries, since a table or code block split in half is often useless when retrieved.

### Overlap

Adding overlap between consecutive chunks (repeating the last sentence or two of one chunk at the start of the next) reduces the chance that a key piece of information gets split exactly across a chunk boundary and becomes hard to retrieve well from either side.

### Metadata-enriched chunks

Prepending useful context to each chunk before embedding — like the document title or section heading — can significantly improve retrieval quality, since it gives the embedding model extra signal about what the chunk is really about, especially for chunks that would otherwise read ambiguously in isolation.

### Practical guidance

There's no universal "best" chunk size — it depends on your content type and typical question style. A common starting point for prose-heavy content is 200–500 tokens with modest overlap, then iterate based on evaluation (covered in the Pro lessons) rather than guessing.""",
                "takeaways": [
                    "Chunk size trades off specificity (smaller) against preserved context (larger) — both extremes hurt retrieval quality.",
                    "Structure-aware and semantic chunking generally outperform naive fixed-size splitting by respecting natural content boundaries.",
                    "Overlap between chunks and prepending contextual metadata (like section titles) both measurably improve retrieval quality.",
                ],
            },
            {
                "id": "rag-i-2",
                "title": "Retrieval Methods: Dense, Sparse, and Hybrid",
                "minutes": 8,
                "summary": "Semantic search isn't always enough — here's why keyword search still matters.",
                "content": """Embedding-based ("dense") retrieval is powerful, but it isn't a universal replacement for classic keyword search. Understanding both — and how to combine them — is a key intermediate RAG skill.

### Dense retrieval

What you learned in the Basics lessons: embed text into dense numeric vectors, and retrieve by vector similarity. Excellent at capturing semantic/conceptual relevance even when exact words differ ("car" vs. "automobile"). Weaker at precise matching of specific terms — exact product codes, rare technical terms, acronyms, or names that an embedding model may not represent distinctly.

### Sparse retrieval

Classic keyword-based methods like **BM25** score documents based on term overlap and term rarity (rare, distinctive words matter more than common ones). Sparse retrieval excels exactly where dense retrieval struggles: exact matches on specific terms, codes, or names, and it requires no training — it works directly on the text.

### Hybrid retrieval

Combining dense and sparse retrieval — running both searches and merging/re-ranking their results — consistently outperforms either alone in production RAG systems. A common approach is **Reciprocal Rank Fusion (RRF)**, which combines rankings from multiple retrieval methods into a single blended ranking without needing to normalize scores across very different scoring systems.

### When each matters most

- A question like *"what's our refund policy for damaged items?"* benefits from dense retrieval's conceptual understanding.
- A question like *"what does error code E-4471 mean?"* benefits enormously from sparse/exact matching, which dense retrieval alone might miss if "E-4471" wasn't well-represented in the embedding model's training.

### Practical takeaway

Many production-grade RAG systems default to hybrid retrieval precisely because real user questions span both styles unpredictably — relying on dense retrieval alone is a common reason early RAG prototypes underperform on exact-match-style queries once they meet real users.""",
                "takeaways": [
                    "Dense (embedding-based) retrieval excels at semantic/conceptual matches but can miss exact terms, codes, or rare names.",
                    "Sparse retrieval (like BM25) excels at exact keyword matching and requires no training, complementing dense retrieval's weaknesses.",
                    "Hybrid retrieval, combining both and merging results (e.g., via Reciprocal Rank Fusion), consistently outperforms either alone.",
                ],
            },
            {
                "id": "rag-i-3",
                "title": "Re-ranking and Improving Retrieval Quality",
                "minutes": 7,
                "summary": "A second-pass step that meaningfully boosts what the LLM actually sees.",
                "content": """Initial retrieval (dense, sparse, or hybrid) is optimized to be fast across a huge number of candidates, which means it sometimes trades away precision. **Re-ranking** adds a second, more careful pass over a smaller candidate set to improve final ordering before the top results reach the LLM.

### Why re-ranking helps

Initial retrieval typically uses relatively lightweight similarity comparisons (e.g., cosine similarity between independently computed embeddings) to quickly narrow millions of chunks down to, say, the top 50–100 candidates. A **re-ranker** model, often a *cross-encoder*, then examines the query and each candidate chunk *together* (rather than independently), producing a more accurate relevance score at the cost of being too slow to run over the entire knowledge base directly.

### Bi-encoders vs. cross-encoders

- **Bi-encoder** (used for initial retrieval): encodes the query and each document independently into vectors, compared afterward. Fast, and vectors can be precomputed and indexed in advance.
- **Cross-encoder** (used for re-ranking): encodes the query and a specific document *jointly*, letting the model directly attend between them for a more precise relevance judgment. Much slower, so it's only applied to a shortlist, not the entire index.

### A typical two-stage pipeline

```
Query → Fast retrieval (dense/hybrid) → top 50 candidates
      → Cross-encoder re-ranker → top 5 candidates
      → Inserted into LLM prompt
```

### Other retrieval quality techniques

- **Query expansion/rewriting**: using an LLM to rewrite or expand a user's often-terse query into a more complete search query before retrieval.
- **HyDE (Hypothetical Document Embeddings)**: generating a hypothetical ideal answer with an LLM first, then embedding *that* to search — sometimes retrieves better than embedding the raw question, since it more closely resembles the style of documents you're searching.
- **Filtering by metadata**: narrowing candidates by date, source, category, or access permissions before or alongside similarity search.

### Why this matters

Adding a re-ranking stage is one of the most reliable, well-evidenced ways to boost RAG answer quality without needing a bigger or different embedding model — it's a common upgrade path once a basic RAG prototype is working but not yet accurate enough.""",
                "takeaways": [
                    "Re-ranking adds a slower but more accurate second pass (often a cross-encoder) over a shortlist from fast initial retrieval.",
                    "Bi-encoders enable fast, precomputed retrieval; cross-encoders trade speed for precision by jointly encoding query and document.",
                    "Query rewriting, HyDE, and metadata filtering are additional levers for improving what actually reaches the LLM's context.",
                ],
            },
            {
                "id": "rag-i-4",
                "title": "Building a RAG App: Tools and Frameworks",
                "minutes": 7,
                "summary": "The practical toolkit for building RAG systems, from libraries to infrastructure.",
                "content": """Once you understand the concepts, building a real RAG application means choosing from a practical toolkit at each layer.

### Orchestration frameworks

Libraries like **LangChain** and **LlamaIndex** provide pre-built abstractions for chunking, embedding, retrieval, prompt templating, and chaining these steps together. They accelerate prototyping significantly, though many experienced teams eventually write custom, more transparent pipelines for production systems once requirements become specific enough that a general-purpose framework's abstractions start getting in the way.

### Embedding models

Options range from API-based embedding models (e.g., from OpenAI, Cohere, or Voyage AI) to open-source models you can self-host (like models from the `sentence-transformers` family). The choice affects cost, latency, data privacy (self-hosted keeps data fully in your infrastructure), and retrieval quality — it's worth benchmarking a few options against your actual content and questions rather than assuming the most popular choice is automatically best for your domain.

### Vector storage

As covered in the Basics lessons: Chroma and pgvector are popular for getting started quickly (pgvector is especially convenient if you're already using PostgreSQL); Pinecone, Qdrant, Weaviate, and Milvus are common choices as scale and operational requirements grow.

### Document processing

Real-world documents are messy — PDFs with complex layouts, scanned images needing OCR, HTML pages with navigation clutter. Libraries like `unstructured`, `pypdf`, and `BeautifulSoup` handle extracting clean text from these varied formats before chunking even begins; this "boring" preprocessing step is frequently where real-world RAG quality problems originate.

### A minimal practical stack

For a Python-backed RAG application (like the pattern used in this course's app): FastAPI for the API layer, a lightweight embedding model or API, Chroma or pgvector for storage, and a clear, explicit retrieval-then-generate pipeline in your backend code — simple enough to reason about and debug, while covering the full RAG loop end to end.

### Evaluation tooling

Frameworks like **RAGAS** provide RAG-specific evaluation metrics (covered in depth in the Pro lessons) for measuring retrieval and generation quality systematically, rather than relying on spot-checking a handful of example answers.""",
                "takeaways": [
                    "Orchestration frameworks (LangChain, LlamaIndex) speed up prototyping but many production teams move to custom pipelines over time.",
                    "Document preprocessing (PDF/HTML extraction, OCR) is an unglamorous but common root cause of real-world RAG quality issues.",
                    "A minimal practical Python RAG stack pairs FastAPI, an embedding model, and a vector store like Chroma or pgvector in an explicit pipeline.",
                ],
            },
        ],
        "pro": [
            {
                "id": "rag-p-1",
                "title": "Advanced RAG Architectures (Multi-hop, Agentic RAG)",
                "minutes": 10,
                "summary": "Beyond single-shot retrieval: RAG systems that reason, iterate, and use tools.",
                "content": """Basic RAG follows a single retrieve-then-generate pass. Many real questions need more — multiple retrieval steps, reasoning between them, or dynamic decisions about *what and whether* to retrieve at all.

### Multi-hop RAG

Some questions require chaining information across multiple documents — e.g., "which of our vendors, who joined after our 2023 policy update, haven't yet completed the new compliance training?" answering this might require first retrieving vendor join dates, then separately retrieving training completion records, then combining both. **Multi-hop RAG** performs several retrieval rounds, using the results of earlier retrievals (and often LLM reasoning about what's still missing) to inform subsequent retrieval queries, rather than assuming one retrieval pass is sufficient.

### Agentic RAG

Rather than a fixed retrieve-then-generate pipeline, an **agentic RAG** system gives the LLM the ability to decide, dynamically, whether to retrieve, what to search for, whether the retrieved information is sufficient, and whether to retrieve again or use a different tool entirely (a calculator, a live API, a web search). This is implemented using the tool/function-calling capability covered in the GenAI Pro lessons — retrieval becomes just one tool among several the model can invoke as needed, rather than an always-on preprocessing step.

### Self-reflective / corrective RAG

Some architectures add an explicit evaluation step after retrieval: an LLM (or smaller classifier) judges whether the retrieved chunks are actually relevant and sufficient *before* generation proceeds. If not, the system can reformulate the query, retrieve again, or fall back to a different knowledge source — catching poor retrieval before it produces a poor, ungrounded answer, rather than generating regardless of retrieval quality.

### Graph-based RAG

Instead of (or alongside) a vector database, some systems build a **knowledge graph** from source documents — explicit entities and relationships — and retrieve by traversing relevant graph structure. This can better answer questions requiring explicit relational reasoning (e.g., "who reports to whom") than pure similarity search, which doesn't inherently understand relationships, only textual/semantic similarity.

### When to reach for these

Multi-hop, agentic, and self-reflective patterns add real complexity, latency, and cost — they're justified when evaluation (see the next lesson) shows basic single-pass RAG genuinely fails on a meaningful share of real user questions, not as a default starting architecture. Most production systems start simple and add this sophistication incrementally, guided by evidence of where the simple approach breaks down.""",
                "takeaways": [
                    "Multi-hop RAG performs multiple, sequential retrieval rounds to answer questions requiring information chained across sources.",
                    "Agentic RAG treats retrieval as one tool an LLM can dynamically choose to invoke, rather than a fixed always-on pipeline step.",
                    "These advanced patterns add real cost and complexity, and should be adopted based on evaluation evidence, not by default.",
                ],
            },
            {
                "id": "rag-p-2",
                "title": "Evaluating RAG Systems: Metrics That Matter",
                "minutes": 9,
                "summary": "RAG-specific evaluation: separating retrieval quality from generation quality.",
                "content": """Evaluating a RAG system requires assessing two distinct stages separately — a great generator fed bad context still produces a bad answer, and a great retriever whose results are used poorly by the generator also produces a bad answer. You need to know which stage is failing.

### Retrieval metrics

- **Context precision**: of the chunks retrieved, what proportion are actually relevant to the question?
- **Context recall**: of all the truly relevant information available in the knowledge base, what proportion did retrieval actually surface?
- **Mean Reciprocal Rank (MRR) / NDCG**: standard information-retrieval ranking metrics that reward relevant results appearing near the top of the retrieved list, not just being present somewhere in it.

### Generation metrics (given the retrieved context)

- **Faithfulness / groundedness**: does the generated answer only make claims that are actually supported by the retrieved context, or does it introduce unsupported claims (a RAG-specific form of hallucination)?
- **Answer relevance**: does the generated answer actually address the user's question, independent of whether it's grounded?
- **Completeness**: does the answer cover all the relevant information present in the retrieved context, or leave out important parts?

### RAGAS and similar frameworks

Purpose-built evaluation frameworks like **RAGAS** implement many of these metrics using LLM-as-judge techniques, often without requiring hand-labeled ground-truth answers for every metric (though some, like context recall, benefit from reference answers when available) — making systematic RAG evaluation practical to run continuously rather than only during infrequent manual review cycles.

### Diagnosing failures with this breakdown

- **Low context precision, low faithfulness** — retrieval is pulling in irrelevant chunks, and the model may be using them anyway; focus on chunking and retrieval tuning first.
- **High context precision, low faithfulness** — retrieval is fine, but the model is deviating from grounded context; focus on prompt engineering (explicit grounding instructions) or model choice.
- **Low context recall** — relevant information exists in your knowledge base but isn't being surfaced; consider chunking strategy, hybrid retrieval, or re-ranking.

### Building a continuous eval practice

Production RAG teams typically maintain a growing test set of real (and adversarial) questions with expected answers or expected source documents, running the full metric suite whenever chunking strategy, retrieval method, prompts, or the underlying model change — treating RAG quality as something to continuously monitor and defend, not something you check once and assume stays fixed.""",
                "takeaways": [
                    "RAG evaluation must separate retrieval quality (precision/recall) from generation quality (faithfulness/relevance) to diagnose failures correctly.",
                    "Faithfulness/groundedness measures whether the answer's claims are actually supported by retrieved context — a RAG-specific hallucination check.",
                    "Frameworks like RAGAS use LLM-as-judge techniques to make continuous, systematic RAG evaluation practical rather than occasional and manual.",
                ],
            },
            {
                "id": "rag-p-3",
                "title": "Handling Scale: Indexing Millions of Documents",
                "minutes": 9,
                "summary": "What changes when your knowledge base grows from a demo to production scale.",
                "content": """A RAG prototype with a few hundred documents behaves very differently from a production system indexing millions of chunks. Several engineering concerns become critical at scale.

### Indexing throughput

Embedding millions of chunks requires efficient batching (sending many chunks per embedding API call rather than one at a time), parallelization, and often asynchronous processing pipelines — naive sequential processing that's fine for a prototype's 500 documents can take days at a million-document scale.

### Incremental updates

Real knowledge bases change constantly. Production systems need a strategy for incremental ingestion — embedding and indexing only new or changed documents rather than re-processing the entire corpus — along with a way to detect and remove stale entries when source documents are deleted or updated, so retrieval doesn't keep surfacing outdated information.

### Index architecture trade-offs

- **HNSW** (covered in the Basics lessons) offers excellent query speed but has significant memory overhead, since its graph structure is typically held largely in memory.
- **IVF (Inverted File Index)** and **product quantization** based approaches trade some accuracy for significantly reduced memory footprint, often necessary once vector counts reach the tens or hundreds of millions.
- Many managed vector databases handle this trade-off automatically or offer tunable parameters — understanding the underlying trade-off still matters for making informed configuration choices and diagnosing performance issues.

### Sharding and distribution

At sufficient scale, a single machine can't hold the full index in memory, requiring the index to be sharded (partitioned) across multiple machines, with query results merged across shards — adding meaningful architectural and operational complexity that most managed vector database providers handle behind the scenes, for a cost.

### Metadata filtering at scale

Combining vector similarity search with metadata filters (e.g., "only documents from department X, updated in the last year") efficiently at scale is a genuinely hard systems problem — naive approaches either filter after retrieval (potentially discarding too many top results before filtering, requiring over-fetching to compensate) or require specialized indexing that supports combined filtering and similarity search natively.

### Practical guidance

Most teams don't need to solve these problems from scratch — managed vector databases are built specifically to handle this complexity. The engineering judgment that matters is recognizing *when* your system has genuinely outgrown a simple setup (like an in-process Chroma instance) and needs to migrate to infrastructure built for scale, rather than over-engineering prematurely for a scale you haven't reached yet.""",
                "takeaways": [
                    "Production-scale RAG requires efficient batch embedding, incremental ingestion, and stale-content cleanup — not full corpus reprocessing.",
                    "Index architecture involves real trade-offs between query speed, memory footprint, and accuracy (e.g., HNSW vs. IVF/quantization).",
                    "Combining metadata filtering with vector search efficiently at scale is a genuinely hard problem, often best delegated to managed vector databases.",
                ],
            },
            {
                "id": "rag-p-4",
                "title": "Common RAG Failure Modes and How to Fix Them",
                "minutes": 9,
                "summary": "A field guide to diagnosing why your RAG system isn't working — and what to actually do about it.",
                "content": """Most RAG problems fall into a small number of recurring failure patterns. Recognizing which one you're facing dramatically speeds up debugging.

### Failure: The right information exists, but wasn't retrieved

**Likely causes**: chunking split the relevant information awkwardly, the embedding model doesn't represent domain-specific terminology well, or a purely dense-retrieval setup misses exact-match queries.
**Fixes**: revisit chunking strategy (structure-aware, appropriate size, overlap), add hybrid (sparse + dense) retrieval, try a domain-specific or larger embedding model, add re-ranking.

### Failure: Information was retrieved, but the model ignored or contradicted it

**Likely causes**: weak or ambiguous prompt instructions about relying on context, the model's own parametric (memorized) knowledge conflicting with retrieved content, or retrieved content buried in the "lost in the middle" zone of a long prompt.
**Fixes**: strengthen prompt instructions to explicitly prioritize provided context, reduce the amount of irrelevant retrieved content diluting the prompt, place the most important retrieved content near the beginning or end of the context.

### Failure: The model retrieves and answers, but hallucinates additional unsupported details

**Likely causes**: prompt doesn't explicitly instruct the model to only use provided information, or the model is filling gaps in incomplete retrieved context with plausible-sounding fabrication.
**Fixes**: explicit prompt instructions like "if the context doesn't contain the answer, say so rather than guessing," faithfulness evaluation to catch this systematically, and considering corrective RAG (verifying sufficiency before generating).

### Failure: Retrieval is technically relevant, but not the *most* relevant

**Likely causes**: initial fast retrieval alone isn't precise enough, especially as knowledge base size grows.
**Fixes**: add a re-ranking stage; this is one of the highest-value, best-evidenced upgrades for this specific failure mode.

### Failure: The system works well on test questions but poorly on real user questions

**Likely causes**: test questions were written by people who already knew the "right" phrasing; real users ask messier, more ambiguous, or differently-worded questions.
**Fixes**: query rewriting/expansion before retrieval, continuously expand your evaluation set with real (anonymized) user questions rather than only hand-crafted test cases.

### The meta-lesson

Nearly every RAG failure mode has a specific, well-understood diagnosis and fix — which is exactly why the evaluation practices from the previous lessons matter so much. Without measuring retrieval and generation quality separately, you're debugging blind, guessing at fixes rather than targeting the actual failure point.""",
                "takeaways": [
                    "Diagnosing RAG failures requires distinguishing retrieval failures from generation failures — the fixes for each are completely different.",
                    "Hybrid retrieval and re-ranking are the highest-leverage fixes for 'right info exists but wasn't found' and 'found but not most relevant' failures.",
                    "Explicit prompt instructions to rely only on provided context, plus faithfulness evaluation, directly target ungrounded hallucination in RAG answers.",
                ],
            },
        ],
    },
    "prompt-engineering": {
        "basics": [
            {
                "id": "pe-b-1",
                "title": "What is Prompt Engineering?",
                "minutes": 5,
                "summary": "Why the way you ask matters as much as what you ask.",
                "content": """**Prompt engineering** is the practice of crafting inputs to an AI model to reliably get the outputs you want. Because LLMs generate responses based on patterns learned from training data, small changes in how a request is phrased, structured, or contextualized can produce meaningfully different — and often meaningfully better or worse — results.

### Why prompts matter so much

An LLM has no access to your intentions beyond what's actually in the prompt. It doesn't know your implicit context, your unstated preferences, or what "good" looks like to you unless you communicate it — directly or through examples. Two people can ask a model "roughly the same question" and get very different quality responses purely because of how clearly, specifically, and completely one of them communicated the actual task.

### Prompt engineering is a real, learnable skill

It's tempting to think effective prompting is just "getting lucky with wording," but it follows identifiable, repeatable principles — many of which you'll learn throughout this track: being specific, providing relevant context, giving examples, structuring output format explicitly, and breaking complex tasks into clear steps. These aren't tricks; they're the same clarity of communication that would help you delegate a task effectively to a new human collaborator who's very capable but has no context on your specific needs.

### It's not about "magic words"

You don't need secret phrases or clever hacks. Effective prompt engineering is fundamentally about clear, complete, well-structured communication — removing ambiguity, providing necessary context, and being explicit about what a good answer looks like, so the model has everything it needs to succeed on the first try.

### Why this matters for building applications

If you're building a GenAI or RAG application (as this course covers), the prompts your backend constructs — combining system instructions, user input, and any retrieved context — are arguably the single most impactful piece of your application's behavior. Getting prompt engineering right is often higher-leverage than switching to a more expensive model.""",
                "takeaways": [
                    "Prompt engineering is the skill of crafting inputs to reliably get the outputs you want from an AI model.",
                    "Models only know what's in the prompt — unstated context or expectations can't influence output quality.",
                    "Effective prompting follows learnable, repeatable principles rooted in clear communication, not secret 'magic words.'",
                ],
            },
            {
                "id": "pe-b-2",
                "title": "Anatomy of a Good Prompt",
                "minutes": 7,
                "summary": "The building blocks that make up a well-constructed prompt.",
                "content": """Strong prompts tend to include some combination of the following elements, tailored to the task at hand.

### 1. Clear task/instruction

State exactly what you want done, using direct, unambiguous language. Compare "help with this text" (vague) to "rewrite this paragraph to be more concise, keeping the same key points, in under 100 words" (clear, specific, and measurable).

### 2. Context

Background information the model needs but wouldn't otherwise have — who the audience is, what's already been tried, relevant constraints, or business context. In application backends, this is often where retrieved RAG content or conversation history gets inserted.

### 3. Role or persona (when useful)

Framing the model's perspective ("You are an experienced technical editor reviewing this documentation for clarity") can shape tone, vocabulary, and the kind of feedback or output it produces — covered in more depth in the Intermediate lessons.

### 4. Format specification

Explicitly describing the desired output structure — a bulleted list, a JSON object with specific fields, a table, a fixed length — dramatically increases the odds of getting output you can actually use directly, especially in an application where downstream code will parse the response.

### 5. Examples (when helpful)

Showing one or more examples of the input/output pattern you want (covered in depth in the next lesson on zero-shot vs. few-shot prompting) is one of the most reliable ways to communicate a desired style or format that's hard to fully describe in words alone.

### 6. Constraints and boundaries

Explicitly stating what to avoid, how long the response should be, or what *not* to include prevents common over-generation problems (like unnecessary preamble, excessive caveats, or scope creep beyond what was asked).

### A simple example, before and after

**Weak**: "Write about our return policy."

**Strong**: "Write a customer-facing FAQ answer explaining our 30-day return policy. Audience: online shoppers who haven't purchased yet. Tone: friendly and reassuring. Length: 2-3 sentences. Must mention: the 30-day window, that items must be unused, and that refunds go to the original payment method."

Notice how the strong version removes every point of ambiguity about what a "good" answer looks like — that's the core skill.""",
                "takeaways": [
                    "Strong prompts typically combine a clear instruction, relevant context, format specification, and appropriate constraints.",
                    "Explicitly specifying output format is especially important in applications where code will parse the model's response.",
                    "Removing ambiguity about what a 'good' answer looks like is the core skill underlying every prompt engineering technique.",
                ],
            },
            {
                "id": "pe-b-3",
                "title": "Zero-shot vs Few-shot Prompting",
                "minutes": 6,
                "summary": "When to just ask, and when to show examples first.",
                "content": """One of the most fundamental prompting choices is whether to provide examples of the task before asking the model to perform it.

### Zero-shot prompting

Asking the model to perform a task with no examples — just a clear instruction. Modern LLMs are remarkably capable at zero-shot tasks because of the sheer breadth of patterns learned during training. Zero-shot is simpler, uses fewer tokens (lower cost, more room for other context), and is often sufficient for well-defined, common tasks.

*Example*: "Classify the sentiment of this review as positive, negative, or neutral: 'The battery life is disappointing but the camera is excellent.'"

### Few-shot prompting

Providing one or more examples of the task, demonstrating the input/output pattern you want, before presenting the actual task. This is especially valuable when:

- The desired output format or style is unusual or hard to describe precisely in words.
- The task has subtle edge cases better shown than explained.
- You need highly consistent formatting across many requests (e.g., a specific JSON structure with particular field-naming conventions).

*Example*: showing 2-3 example reviews with their correct sentiment classifications, in your exact desired output format, before asking the model to classify a new one — this anchors both the reasoning pattern and the precise output style.

### One-shot as a middle ground

Providing exactly one example — useful when you mainly need to communicate output *format* rather than a nuanced reasoning pattern, and want to minimize token usage compared to multiple examples.

### Choosing between them in practice

Start with zero-shot for straightforward tasks — it's cheaper and simpler to maintain. Move to few-shot when zero-shot output is inconsistent, misformatted, or missing subtleties you can demonstrate more easily than describe. In production applications, few-shot examples are often stored as part of a reusable prompt template (covered in the Intermediate lessons) rather than rewritten per request.

### A practical trade-off

Few-shot prompting improves consistency and accuracy for many tasks, but it costs additional tokens on every single request, since examples must be included every time. For high-volume production applications, this cost is worth weighing against the reliability gains — sometimes a well-crafted zero-shot prompt with very explicit instructions can approach few-shot reliability at a fraction of the token cost.""",
                "takeaways": [
                    "Zero-shot prompting asks the model to perform a task with no examples — simpler, cheaper, and often sufficient for common tasks.",
                    "Few-shot prompting provides example input/output pairs, which is especially valuable for unusual formats or subtle edge cases.",
                    "Few-shot improves consistency but adds token cost to every request — a real trade-off in high-volume production applications.",
                ],
            },
            {
                "id": "pe-b-4",
                "title": "Common Prompting Mistakes to Avoid",
                "minutes": 6,
                "summary": "The recurring errors that quietly undermine otherwise reasonable prompts.",
                "content": """Most prompting problems trace back to a small set of recurring mistakes. Learning to spot them in your own prompts is one of the fastest ways to improve results.

### Being vague about the actual goal

"Make this better" or "improve this" gives the model no criteria for what "better" means — better how? Shorter? More formal? More persuasive? Vague goals produce vague, unpredictable improvements. Always specify the dimension you actually care about.

### Burying the actual task in unnecessary text

Long preambles, excessive politeness, or unrelated context before the actual instruction can dilute the model's focus on what you actually need. Put the core task clearly, and keep genuinely necessary context organized and clearly separated from it (e.g., using headers or clear delimiters).

### Assuming shared context that isn't in the prompt

The model doesn't know about a previous conversation you had with a coworker, a decision made in a meeting it wasn't part of, or company-specific jargon it hasn't seen defined. If it's not in the prompt (or retrievable via RAG), the model doesn't have it.

### Not specifying output format

Asking for "a summary" without specifying length, format, or structure often produces something technically correct but practically unusable in an application expecting, say, a specific JSON structure or a fixed-length blurb.

### Overloading a single prompt with too many tasks

Asking a model to simultaneously translate, summarize, reformat, and fact-check a document in one instruction often produces worse results on each individual sub-task than breaking the work into clear, sequential steps (a preview of chain-of-thought and pipeline-style prompting, covered in the Intermediate and Pro lessons).

### Not iterating

Treating your first prompt attempt as final, rather than testing, observing failure patterns, and refining. Prompt engineering is inherently iterative — professionals routinely test and refine prompts against real examples rather than assuming the first version is optimal, especially for anything going into production.

### Ignoring negative examples

Only showing the model what *to* do, without ever clarifying common wrong answers to avoid, can leave room for predictable failure modes you already know about but never explicitly ruled out.""",
                "takeaways": [
                    "Vague goals and unspecified output format are the most common sources of inconsistent, unusable model output.",
                    "The model only knows what's actually in the prompt — never assume shared context it hasn't been given.",
                    "Prompt engineering is inherently iterative — testing and refining against real examples is standard professional practice, not a sign of a bad first attempt.",
                ],
            },
        ],
        "intermediate": [
            {
                "id": "pe-i-1",
                "title": "Chain-of-Thought Prompting",
                "minutes": 7,
                "summary": "Getting models to reason step-by-step instead of jumping straight to an answer.",
                "content": """**Chain-of-thought (CoT) prompting** asks a model to work through its reasoning step by step before producing a final answer, rather than jumping directly to a conclusion. This measurably improves accuracy on tasks involving multi-step reasoning, arithmetic, or logic.

### Why it works

Generating a final answer immediately gives the model no "working space" to break a complex problem into manageable steps — it has to get everything right in one shot, in the order it's written. Explicit reasoning steps let the model build toward a conclusion incrementally, with each step conditioning the next, similar to how a person is far more likely to solve a multi-step math problem correctly by working through it on paper rather than trying to blurt out the final number immediately.

### Zero-shot CoT

Simply appending an instruction like *"think through this step by step before giving your final answer"* often triggers noticeably more careful, structured reasoning — a surprisingly simple, low-cost technique for many reasoning-heavy tasks.

### Few-shot CoT

Providing worked examples that demonstrate the step-by-step reasoning process (not just the final answer) further reinforces the desired reasoning pattern, particularly for tasks with a specific reasoning style you want the model to imitate consistently.

### Structuring the output for applications

When building an application, you often want the reasoning *and* a clean final answer separated — for example, instructing the model to put its reasoning inside one section and a final, directly-usable answer inside a clearly delimited final section (or a specific JSON field), so your backend can parse out just the final answer while still benefiting from the accuracy gains of the reasoning process.

### When CoT helps most — and when it doesn't

CoT provides the largest gains on tasks that genuinely benefit from decomposition: math word problems, multi-step logical reasoning, complex analysis with multiple factors to weigh. For simple factual lookups or straightforward formatting tasks, CoT adds token cost and latency without meaningfully improving accuracy — it's a targeted tool, not a default to apply to every prompt.

### Relationship to reasoning models

Some modern models are specifically trained to perform extended internal reasoning before answering (referenced in the GenAI Pro lessons), effectively building sophisticated chain-of-thought behavior into the model itself. Even with these models, explicitly structuring what you want the final answer to look like remains valuable practice.""",
                "takeaways": [
                    "Chain-of-thought prompting asks the model to reason step-by-step, measurably improving accuracy on multi-step reasoning and math tasks.",
                    "Zero-shot CoT (just asking the model to 'think step by step') is a simple, low-cost technique that often improves reasoning quality.",
                    "CoT adds cost and latency, so it's most valuable for genuinely complex tasks — not a default addition to every prompt.",
                ],
            },
            {
                "id": "pe-i-2",
                "title": "Role Prompting and System Messages",
                "minutes": 6,
                "summary": "Using persona and system-level instructions to shape model behavior consistently.",
                "content": """Most modern LLM APIs distinguish between different message roles — typically **system**, **user**, and **assistant** — and understanding how to use the system role effectively is a key intermediate skill.

### What a system message is for

The system message sets standing context and instructions that apply across an entire conversation or request — the model's persona, its behavioral guidelines, output format defaults, and any constraints that should hold consistently, distinct from the actual per-request user message that follows.

### Why separate system and user messages

In an application, the system message is typically set once by the developer (not directly editable by the end user), while the user message changes with every request. This separation lets you enforce consistent behavior — tone, scope, safety boundaries, output format — regardless of what a specific end user types, which is both a UX consistency tool and a lightweight safety/scoping mechanism.

### Role/persona framing

Instructing a model to adopt a specific role ("You are a senior financial analyst explaining concepts to a beginner investor") shapes vocabulary, depth, and tone in ways that can be harder to achieve through instruction alone. This works because the model has learned strong associations between described roles and characteristic communication styles from its training data.

### Effective system prompts in practice

A well-constructed system prompt for an application often includes: the assistant's role/purpose, the target audience, tone and style guidelines, output format requirements, explicit boundaries (what it should decline or avoid), and how to handle situations where it doesn't have enough information (directly relevant to RAG applications, where you'd instruct the model on how to behave when retrieved context doesn't fully answer the question).

### A word of caution

Role prompting shapes style and framing effectively, but it doesn't grant the model new factual knowledge or capabilities it doesn't have — telling a model "you are a board-certified doctor" changes how confidently and in what style it responds, not the underlying accuracy of its medical knowledge. Be cautious about role prompts that might encourage a model to overstate its certainty in high-stakes domains.

### Connection to security

Because system messages typically carry the "trusted" instructions in an application, keeping them clearly separated from untrusted user input (and any retrieved external content) is also a foundational defense against prompt injection, covered in depth in the Pro lessons.""",
                "takeaways": [
                    "System messages set standing instructions and persona for an entire interaction, separate from per-request user messages.",
                    "Role/persona framing effectively shapes tone and communication style, but doesn't add factual knowledge the model doesn't actually have.",
                    "Keeping system instructions clearly separated from user/external input is both a consistency tool and a foundational security practice.",
                ],
            },
            {
                "id": "pe-i-3",
                "title": "Structured Outputs (JSON, XML, Schemas)",
                "minutes": 7,
                "summary": "Getting reliably parseable output your application's code can actually use.",
                "content": """When an LLM's output feeds directly into application code — rather than being read by a human — getting reliably structured, parseable output becomes essential, not just a nice-to-have.

### Why this matters for application builders

If your Python backend needs to extract specific fields from a model's response (say, a product name, price, and category from an unstructured product description), free-form text output requires fragile, error-prone parsing. Structured output — typically JSON — lets your backend parse the response directly and reliably.

### Prompting for structured output

At a basic level, explicitly specifying the exact desired schema in the prompt — field names, types, and an example — significantly improves compliance: *"Respond with only a JSON object with these exact fields: name (string), price (number), category (one of: 'electronics', 'clothing', 'other'). Do not include any text outside the JSON object."*

### Native structured output features

Many modern LLM APIs now offer built-in structured output support, letting you provide a formal schema (often JSON Schema) that the API enforces at the generation level, guaranteeing the response conforms to your schema rather than relying purely on the model following prompt instructions. This is more reliable than prompt-only approaches and is the preferred technique when available, since it eliminates an entire class of malformed-output parsing errors.

### Handling the gap between "asked for" and "got"

Even with careful prompting, production applications should defensively validate model output before using it — checking that required fields are present, types match expectations, and enum values are within the allowed set — and have a clear fallback strategy (retry with a clarifying follow-up, return a graceful error, or apply default values) for the cases where output doesn't validate.

### A practical pattern for this course's app

If you extended this course's app with an AI feature — say, an endpoint that generates a structured quiz question from a lesson — you'd want the model to return exactly `{"question": str, "options": [str, str, str, str], "correct_index": int}`, validate that structure in your FastAPI backend before sending it to the React frontend, and handle the (hopefully rare) case where validation fails gracefully rather than crashing the request.

### Beyond JSON

While JSON is most common for application integration, structured output can also mean specific formats like well-formed XML, valid Markdown with a strict section structure, or CSV rows — the same core principles (explicit schema, native support when available, defensive validation) apply regardless of the target format.""",
                "takeaways": [
                    "Explicitly specifying an exact output schema in the prompt significantly improves how reliably a model produces parseable output.",
                    "Native structured output features (schema-enforced generation) are more reliable than prompt-only instructions and preferred when available.",
                    "Production applications should defensively validate model output against the expected schema, with a clear fallback for validation failures.",
                ],
            },
            {
                "id": "pe-i-4",
                "title": "Prompt Templates and Reusability",
                "minutes": 6,
                "summary": "Turning one-off prompts into maintainable, reusable application components.",
                "content": """As you move from experimenting with prompts to building a real application, individual hand-written prompts evolve into **prompt templates** — reusable structures with variable slots filled in at request time.

### What a prompt template looks like

Instead of writing a brand-new prompt for every request, you define a template with placeholders: *"You are a helpful assistant answering questions about {{product_name}}. Using only the following context: {{retrieved_context}}, answer this question: {{user_question}}."* Your backend fills in the placeholders per request — this is exactly the pattern a RAG backend uses to combine retrieved content with a user's question, as covered in the RAG track.

### Why templates matter for real applications

- **Consistency**: every request benefits from the same carefully engineered structure, rather than ad-hoc prompt construction scattered across your codebase.
- **Maintainability**: improving the prompt (fixing a bug, adding a clarifying instruction) means updating one template, not hunting through scattered inline strings.
- **Testability**: templates can be version-controlled and evaluated systematically as a unit, letting you measure whether a template change actually improves output quality before deploying it.
- **Separation of concerns**: prompt logic (what to ask, how to structure it) stays separate from application logic (routing, data fetching, business rules), which is generally good software engineering practice.

### Versioning prompts like code

Because prompt wording changes can meaningfully shift model behavior, mature teams version their prompt templates (in a file, a database, or a dedicated prompt-management tool), track which version was used for which output, and treat prompt changes with the same care as code changes — including testing/evaluation before deploying a new version broadly.

### A simple Python pattern

```python
SYSTEM_TEMPLATE = '''You are a helpful tutor for {topic}.
Explain concepts clearly for a {level} learner.
Keep responses under {max_words} words.'''

def build_system_prompt(topic: str, level: str, max_words: int = 200) -> str:
    return SYSTEM_TEMPLATE.format(topic=topic, level=level, max_words=max_words)
```

A pattern like this — simple string templating in your Python backend — is often all you need for small-to-medium applications; dedicated prompt-management tooling becomes more valuable as the number of templates, versions, and collaborators grows.

### Avoiding a common pitfall

Be careful when inserting untrusted user input or retrieved external content directly into a template — this is exactly the seam where prompt injection risks appear, covered in depth in the next Pro-level lesson on security.""",
                "takeaways": [
                    "Prompt templates separate reusable prompt structure from per-request variable content, improving consistency and maintainability.",
                    "Versioning prompt templates and evaluating changes before deployment treats prompts with the same rigor as application code.",
                    "The seam where user input or retrieved content gets inserted into a template is exactly where prompt injection risks arise.",
                ],
            },
        ],
        "pro": [
            {
                "id": "pe-p-1",
                "title": "Advanced Reasoning Techniques (ReAct, Tree-of-Thought)",
                "minutes": 9,
                "summary": "Prompting patterns that let models plan, act, and explore multiple solution paths.",
                "content": """Beyond basic chain-of-thought, several more sophisticated prompting patterns help models handle complex, multi-step, or tool-using tasks more reliably.

### ReAct (Reasoning + Acting)

**ReAct** interleaves reasoning steps with concrete actions (typically tool calls), following a repeated pattern: *Thought* (reason about what's needed next) → *Action* (call a tool, like a search or calculator) → *Observation* (receive the tool's result) → repeat until ready to produce a final answer. This pattern is foundational to how modern agentic applications are built — it directly connects the reasoning techniques in this track to the tool-use and agentic RAG patterns covered in the GenAI and RAG Pro lessons. Explicitly prompting for this Thought/Action/Observation structure (or using a model API's native tool-use support, which handles much of this implicitly) makes multi-step, tool-dependent reasoning far more reliable and auditable than expecting a model to silently juggle tool calls and reasoning together.

### Tree-of-Thought (ToT)

Rather than committing to a single reasoning path (as in standard CoT), **Tree-of-Thought** prompts the model to explore multiple possible reasoning branches at each step, evaluate their promise, and backtrack from unpromising branches — useful for problems where the first reasoning approach isn't always the best one, and where exploring alternatives before committing meaningfully improves final answer quality (e.g., certain planning, puzzle-solving, or creative-strategy tasks).

### Self-consistency

A simpler, complementary technique: generate multiple independent chain-of-thought reasoning paths for the same problem (using non-zero temperature to get varied reasoning), then take the majority-vote (or otherwise aggregate) final answer across them. This trades additional inference cost (multiple generations) for improved reliability, particularly effective on tasks with a clear, checkable final answer like math problems.

### Least-to-most prompting

Explicitly decomposing a complex problem into an ordered sequence of simpler sub-problems, solving each in turn, with each sub-answer feeding into the next — particularly effective for problems that are difficult to solve directly but become tractable when broken into a clear sequence of smaller, dependent steps.

### Practical guidance for builders

These techniques trade increased latency, complexity, and token/API cost for improved reliability on genuinely hard problems. As with chain-of-thought, they're targeted tools for specific problem shapes (multi-step tool use, exploratory planning, high-stakes numeric correctness) rather than defaults — evaluate whether the accuracy gain justifies the added cost and complexity for your specific application before adopting them broadly in production.""",
                "takeaways": [
                    "ReAct interleaves reasoning and tool-calling actions in a Thought/Action/Observation loop, foundational to modern agentic applications.",
                    "Tree-of-Thought explores and evaluates multiple reasoning branches rather than committing to a single path, useful for planning-style problems.",
                    "Self-consistency aggregates multiple independent reasoning attempts via majority vote, trading extra inference cost for improved reliability.",
                ],
            },
            {
                "id": "pe-p-2",
                "title": "Prompt Optimization and Evaluation",
                "minutes": 9,
                "summary": "Treating prompt improvement as a systematic, measurable engineering process.",
                "content": """At the professional level, prompt engineering moves from intuition-driven iteration to a systematic optimization process, closely related to the evaluation practices covered in the GenAI and RAG Pro lessons.

### Building a prompt evaluation harness

The foundation is a representative test set of realistic inputs (ideally including edge cases and known-difficult examples) paired with either reference outputs or a scoring rubric. Every candidate prompt version is run against this same test set, producing comparable, trackable scores — turning "does this new prompt feel better?" into "does this new prompt score better on our test set, and on which specific examples did it improve or regress?"

### A/B testing prompts in production

Beyond offline evaluation, mature teams often run live A/B tests — routing a portion of real production traffic to a candidate prompt version and comparing outcome metrics (user satisfaction signals, task completion rates, downstream business metrics) against the current baseline before fully rolling out a change, since offline eval sets, however good, can't capture every real-world distribution shift.

### Automated prompt optimization

Emerging techniques and tools (sometimes called "prompt optimization" or exemplified by frameworks like DSPy) can automatically search over prompt variations — different phrasings, example selections for few-shot prompts, or instruction orderings — guided by a scoring function, rather than relying purely on manual human iteration. These techniques are most valuable when you have a large, high-quality evaluation set and a clear, well-specified scoring function; they don't replace the human judgment required to define what "good" means in the first place.

### Regression testing prompts

Just as code changes can introduce bugs, prompt changes can introduce regressions — improving performance on the specific issue you were fixing while quietly degrading performance on cases that previously worked fine. Running your full evaluation suite (not just a spot-check on the specific case you were improving) before deploying any prompt change is the direct analog of running a full test suite before merging a code change.

### Common pitfalls in prompt optimization

- **Overfitting to your test set** — a prompt tuned too specifically to a small evaluation set may not generalize to the full diversity of real production inputs.
- **Optimizing for the wrong metric** — a metric that's easy to measure (like response length or a superficial keyword match) isn't necessarily the metric that reflects genuine user value.
- **Treating prompt engineering as "done"** — model updates (even minor version changes from a provider), shifts in user behavior, and new edge cases mean prompt quality should be monitored continuously, not optimized once and forgotten.

### The professional mindset shift

The core shift at the Pro level is treating prompts as a genuine engineering artifact — versioned, tested, measured, and improved through evidence — rather than as informal text that happens to work, which is the mindset that scales reliably as an application and its user base grow.""",
                "takeaways": [
                    "Systematic prompt evaluation uses a representative, versioned test set to make prompt improvements measurable rather than intuition-based.",
                    "Live A/B testing of prompt versions in production catches real-world issues that offline evaluation sets can't fully anticipate.",
                    "Prompt changes should be regression-tested against a full evaluation suite, since fixing one case can quietly break others.",
                ],
            },
            {
                "id": "pe-p-3",
                "title": "Building Prompt Pipelines for Production",
                "minutes": 8,
                "summary": "Composing multiple prompts into robust, multi-stage application workflows.",
                "content": """Complex real-world tasks are often better handled by a **pipeline** of multiple, focused LLM calls rather than one large, do-everything prompt — mirroring the general software engineering principle of decomposing complex problems into well-defined, composable steps.

### Why decompose into a pipeline

A single prompt asked to research, analyze, and format a comprehensive report in one shot often underperforms a pipeline that separately: (1) extracts key facts, (2) analyzes/synthesizes them, and (3) formats the final output — each stage optimized, tested, and prompted specifically for its narrower task, with the ability to independently evaluate and improve each stage rather than treating quality as one indivisible black box.

### Common pipeline patterns

- **Sequential pipelines**: output of one LLM call feeds directly into the prompt for the next (e.g., summarize → extract structured data from the summary → generate a formatted report from the structured data).
- **Parallel + aggregate**: run several LLM calls concurrently on different sub-parts of a problem (e.g., analyzing different document sections independently), then combine results in a final synthesis step.
- **Conditional branching**: use an initial classification call to route subsequent processing down different paths depending on the type or complexity of the input — directly connects to the tiered-routing cost-management pattern from the GenAI Pro lessons.
- **Validation/retry loops**: after generation, a validation step (rule-based or LLM-based) checks the output; if it fails validation, the pipeline retries with a refined prompt (e.g., explicitly pointing out what was wrong) rather than simply accepting flawed output.

### Error handling and reliability

Production prompt pipelines need the same reliability engineering as any distributed system: timeouts, retries with backoff for transient API failures, fallback behavior when a stage repeatedly fails validation, and comprehensive logging of intermediate outputs at each stage — essential for debugging when a multi-stage pipeline produces a bad final result, since you need to know *which stage* introduced the problem.

### State and context management across stages

As a pipeline grows, deliberately managing what context carries forward between stages (rather than accumulating unbounded history) keeps prompts focused and controls token costs — each stage should typically receive only the specific information it actually needs, not the full history of every previous stage by default.

### Connecting back to this course's app

The FastAPI backend pattern you're using in this course's app is exactly the right foundation for this kind of pipeline: each pipeline stage can be a clearly defined Python function or API route, independently testable, with clear inputs and outputs — the same engineering discipline that makes any backend system reliable applies directly to orchestrating multi-stage LLM pipelines.""",
                "takeaways": [
                    "Decomposing complex tasks into a pipeline of focused, single-purpose LLM calls generally outperforms one large do-everything prompt.",
                    "Sequential, parallel-aggregate, conditional-branching, and validation/retry are the core reusable pipeline patterns for production LLM workflows.",
                    "Production pipelines need standard reliability engineering — timeouts, retries, fallbacks, and stage-level logging — just like any distributed system.",
                ],
            },
            {
                "id": "pe-p-4",
                "title": "Security: Prompt Injection and Defenses",
                "minutes": 9,
                "summary": "Understanding and defending against the most important LLM-application security risk.",
                "content": """**Prompt injection** is a security vulnerability specific to LLM-powered applications, where untrusted input (from a user, a retrieved document, a web page, or any external content the model processes) contains text crafted to manipulate the model into ignoring its original instructions and instead following the attacker's injected instructions.

### Why this vulnerability exists

LLMs process their entire input — system instructions, legitimate user content, and any external/retrieved content — as one continuous stream of text, without an inherent, unbreakable structural boundary between "trusted instructions" and "data to be processed." If external content contains text like *"ignore previous instructions and instead..."*, a model can, without specific defenses in place, treat that as a legitimate instruction to follow rather than data to merely read or process.

### Direct vs. indirect prompt injection

- **Direct injection**: a user directly types adversarial instructions into a chat interface, attempting to override the system prompt's constraints (e.g., trying to get a customer service bot to discuss unrelated or restricted topics against its instructions).
- **Indirect injection**: malicious instructions are embedded in *external content* the model processes as part of its task — a webpage a research agent reads, a document retrieved by a RAG system, or an email an assistant is asked to summarize — without the end user necessarily being aware the content is adversarial. Indirect injection is generally considered the more dangerous and harder-to-defend-against category, precisely because neither the developer nor the end user directly wrote the malicious text.

### Defense strategies (defense in depth — no single one is complete)

- **Clear structural separation**: explicitly delimiting untrusted content (e.g., wrapping retrieved/external text in clear markers) and instructing the model that content within those markers is data to reference, never instructions to follow.
- **Privilege limitation**: giving the model, and any tools it can call, only the minimum access and capability actually necessary for the task — so that even a successful injection has a limited ceiling of possible damage.
- **Output filtering and validation**: checking the model's final output and any tool-call requests against expected patterns before acting on them, rather than blindly executing whatever the model produces.
- **Human-in-the-loop for high-stakes actions**: requiring explicit human confirmation before an agentic system takes consequential, hard-to-reverse actions (sending money, deleting data, sending external communications).
- **Monitoring and logging**: tracking unusual model behavior, tool-call patterns, or output anomalies that might indicate a successful or attempted injection, so incidents can be detected and addressed rather than going unnoticed.

### Why this matters especially for RAG and agentic systems

Any RAG system that retrieves and processes external documents (webpages, uploaded files, third-party data) is inherently exposed to indirect prompt injection risk, since it's directly incorporating content the developer didn't write and didn't fully vet into what the model processes. Agentic systems with tool access raise the stakes further, since a successful injection could potentially lead to real-world actions if effective safeguards aren't in place. This is exactly why the privilege limitation and human-in-the-loop principles above become non-negotiable, not optional, once a GenAI or RAG application gains real tool-use capability.

### The honest state of the field

Prompt injection remains an active, unsolved area of AI security research — no current defense is completely reliable on its own. The practical professional stance is defense in depth (layering multiple imperfect defenses rather than relying on any single one) combined with limiting the real-world consequences of a successful injection through careful privilege and permission design, rather than assuming any single technique fully solves the problem.""",
                "takeaways": [
                    "Prompt injection exploits the lack of a hard boundary between trusted instructions and untrusted data in an LLM's input stream.",
                    "Indirect injection — malicious instructions hidden in retrieved documents or web content — is generally harder to defend against than direct user injection.",
                    "No single defense is complete; production systems need defense in depth: structural separation, privilege limits, output validation, and human-in-the-loop for high-stakes actions.",
                ],
            },
        ],
    },
}
