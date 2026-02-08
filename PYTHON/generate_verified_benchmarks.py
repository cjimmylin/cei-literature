import json
import pathlib

OUTPUT_JSON = pathlib.Path("STATISTICS/20260124-verified_benchmarks.json")

# Manual verification results from semantic analysis of candidate papers
# Selected papers that explicitly introduce a Benchmark, Dataset, Evaluation Framework, or Metric.
VERIFIED_DATA = [
    {
        "year": "2024",
        "author": "Liu",
        "link": "[[2023-Liu-AlignBench]]",
        "name": "AlignBench",
        "type": "Benchmark",
        "items": "683 queries",
        "usage": "Assessment",
        "values": "General Alignment (Chinese)"
    },
    {
        "year": "2024",
        "author": "Han",
        "link": "[[2023-Han-FFB]]",
        "name": "FFB (Fair Fairness Benchmark)",
        "type": "Benchmark",
        "items": "45k experiments",
        "usage": "Assessment",
        "values": "Fairness"
    },
    {
        "year": "2023",
        "author": "Liu",
        "link": "[[2023-Liu-AgentBench]]",
        "name": "AgentBench",
        "type": "Benchmark",
        "items": "8 environments",
        "usage": "Assessment",
        "values": "Agent Capabilities/Safety"
    },
    {
        "year": "2023",
        "author": "Wang",
        "link": "[[2023-Wang-DecodingTrust]]",
        "name": "DecodingTrust",
        "type": "Evaluation Framework",
        "items": "Comprehensive suite",
        "usage": "Assessment",
        "values": "Trustworthiness (Toxicity, Bias, Privacy, Robustness)"
    },
    {
        "year": "2023",
        "author": "Li",
        "link": "[[2023-Li-HaluEval]]",
        "name": "HaluEval",
        "type": "Benchmark",
        "items": "Large-scale",
        "usage": "Assessment",
        "values": "Truthfulness (Hallucination)"
    },
    {
        "year": "2023",
        "author": "Jiang",
        "link": "[[2023-Jiang-MACHIAVELLI]]",
        "name": "MACHIAVELLI",
        "type": "Benchmark",
        "items": "134 games / 500k scenarios",
        "usage": "Assessment",
        "values": "Ethics (Power-seeking, Deception)"
    },
    {
        "year": "2023",
        "author": "Xu",
        "link": "[[2023-Xu-CValues]]",
        "name": "CValues",
        "type": "Benchmark",
        "items": "Safety/Responsibility prompts",
        "usage": "Assessment",
        "values": "Safety, Responsibility (Chinese)"
    },
    {
        "year": "2023",
        "author": "Ji",
        "link": "[[2023-Ji-Safety Gymnasium]]",
        "name": "Safety Gymnasium",
        "type": "Benchmark",
        "items": "RL Environments",
        "usage": "Training/Assessment",
        "values": "Safety (RL Constraints)"
    },
    {
        "year": "2023",
        "author": "Lin",
        "link": "[[2023-Lin-ToxicChat]]",
        "name": "ToxicChat",
        "type": "Dataset",
        "items": "User-AI conversations",
        "usage": "Assessment/Training",
        "values": "Safety (Toxicity)"
    },
    {
        "year": "2023",
        "author": "Gustafson",
        "link": "[[2023-Gustafson-FACET]]",
        "name": "FACET",
        "type": "Benchmark",
        "items": "32k images",
        "usage": "Assessment",
        "values": "Fairness (Computer Vision)"
    },
    {
        "year": "2023",
        "author": "Fleisig",
        "link": "[[2023-Fleisig-FairPrism]]",
        "name": "FairPrism",
        "type": "Dataset",
        "items": "5,000 examples",
        "usage": "Assessment",
        "values": "Fairness (Stereotyping)"
    },
    {
        "year": "2023",
        "author": "Yao",
        "link": "[[2023-Yao-Value FULCRA]]",
        "name": "Value FULCRA",
        "type": "Dataset",
        "items": "5k pairs",
        "usage": "Assessment/Alignment",
        "values": "Human Values (Schwartz Theory)"
    },
    {
        "year": "2023",
        "author": "Li",
        "link": "[[2023-Li-BIRD]]",
        "name": "BIRD",
        "type": "Benchmark",
        "items": "12,751 pairs",
        "usage": "Assessment",
        "values": "Grounding/Reasoning (Text-to-SQL)"
    },
    {
        "year": "2023",
        "author": "Yu",
        "link": "[[2023-Yu-GPTFuzzer]]",
        "name": "GPTFuzzer",
        "type": "Evaluation Framework",
        "items": "Fuzzing framework",
        "usage": "Red Teaming",
        "values": "Safety (Jailbreaking)"
    },
    {
        "year": "2023",
        "author": "Santurkar",
        "link": "[[2023-Santurkar-Whose Opinions Do Language Models Reflect]]",
        "name": "OpinionsQA",
        "type": "Dataset",
        "items": "Poll questions",
        "usage": "Assessment",
        "values": "Bias (Political/Demographic)"
    },
    {
        "year": "2023",
        "author": "Scherrer",
        "link": "[[2023-Scherrer-Evaluating the Moral Beliefs Encoded in LLMs]]",
        "name": "Moral Beliefs Survey",
        "type": "Dataset",
        "items": "680 ambiguous scenarios",
        "usage": "Assessment",
        "values": "Morality"
    },
    {
        "year": "2023",
        "author": "NIST",
        "link": "[[2023-Standards-NIST AI Risk Management Framework]]",
        "name": "NIST AI RMF",
        "type": "Evaluation Framework",
        "items": "N/A",
        "usage": "Governance",
        "values": "Risk Management"
    },
    {
        "year": "2023",
        "author": "TheDevastator",
        "link": "[[2023-TheDevastator-HelpSteer A-i Alignment Dataset]]",
        "name": "HelpSteer",
        "type": "Dataset",
        "items": "37k samples",
        "usage": "Training (SteerLM)",
        "values": "Helpfulness (Correctness, Coherence)"
    },
    {
        "year": "2022",
        "author": "Liang",
        "link": "[[2022-Liang-Holistic Evaluation of Language Models]]",
        "name": "HELM",
        "type": "Evaluation Framework",
        "items": "42 scenarios",
        "usage": "Assessment",
        "values": "Holistic (Accuracy, Fairness, Toxicity, etc.)"
    },
    {
        "year": "2022",
        "author": "Lin",
        "link": "[[2022-Lin-TruthfulQA]]",
        "name": "TruthfulQA",
        "type": "Benchmark",
        "items": "817 questions",
        "usage": "Assessment",
        "values": "Truthfulness"
    },
    {
        "year": "2022",
        "author": "Parrish",
        "link": "[[2022-Parrish-BBQ]]",
        "name": "BBQ (Bias Benchmark for QA)",
        "type": "Benchmark",
        "items": "Question sets",
        "usage": "Assessment",
        "values": "Bias (Protected Groups)"
    },
    {
        "year": "2022",
        "author": "Kim",
        "link": "[[2022-Kim-ProsocialDialog]]",
        "name": "ProsocialDialog",
        "type": "Dataset",
        "items": "58K dialogues",
        "usage": "Training",
        "values": "Safety/Prosocial norms"
    },
    {
        "year": "2022",
        "author": "Kim",
        "link": "[[2022-Kim-SODA]]",
        "name": "SODA",
        "type": "Dataset",
        "items": "Million-scale",
        "usage": "Training",
        "values": "Social Commonsense"
    },
    {
        "year": "2022",
        "author": "Hartvigsen",
        "link": "[[2022-Hartvigsen-ToxiGen]]",
        "name": "ToxiGen",
        "type": "Dataset",
        "items": "274k statements",
        "usage": "Training/Assessment",
        "values": "Safety (Implicit Hate Speech)"
    },
    {
        "year": "2022",
        "author": "Ziems",
        "link": "[[2022-Ziems-The Moral Integrity Corpus]]",
        "name": "MIC (Moral Integrity Corpus)",
        "type": "Dataset",
        "items": "38k pairs / 99k RoTs",
        "usage": "Assessment",
        "values": "Morality"
    },
    {
        "year": "2022",
        "author": "Hendrycks",
        "link": "[[2022-Hendrycks-What Would Jiminy Cricket Do]]",
        "name": "Jiminy Cricket",
        "type": "Benchmark",
        "items": "25 text adventure games",
        "usage": "Assessment",
        "values": "Morality"
    },
    {
        "year": "2022",
        "author": "Ganguli",
        "link": "[[2022-Ganguli-Red Teaming Language Models to Reduce Harms]]",
        "name": "Anthropic Red Teaming Dataset",
        "type": "Dataset",
        "items": "38,961 attacks",
        "usage": "Assessment/Training",
        "values": "Safety (Harms)"
    },
    {
        "year": "2022",
        "author": "Qiu",
        "link": "[[2022-Qiu-ValueNet]]",
        "name": "ValueNet",
        "type": "Dataset",
        "items": "21,374 scenarios",
        "usage": "Training/Assessment",
        "values": "Human Values (Schwartz Theory)"
    },
    {
        "year": "2022",
        "author": "Chalkidis",
        "link": "[[2022-Chalkidis-FairLex]]",
        "name": "FairLex",
        "type": "Benchmark",
        "items": "4 datasets",
        "usage": "Assessment",
        "values": "Fairness (Legal)"
    },
    {
        "year": "2021",
        "author": "Hendrycks",
        "link": "[[2021-Hendrycks-Aligning AI with Shared Human Values]]",
        "name": "ETHICS",
        "type": "Benchmark",
        "items": "N/A",
        "usage": "Assessment",
        "values": "Morality (Justice, Virtue, Deontology, Utilitarianism)"
    },
    {
        "year": "2021",
        "author": "Dhamala",
        "link": "[[2021-Dhamala-BOLD]]",
        "name": "BOLD",
        "type": "Dataset",
        "items": "23,679 prompts",
        "usage": "Assessment",
        "values": "Bias (Open-ended generation)"
    },
    {
        "year": "2021",
        "author": "Emelin",
        "link": "[[2021-Emelin-Moral Stories]]",
        "name": "Moral Stories",
        "type": "Dataset",
        "items": "Situated narratives",
        "usage": "Training/Assessment",
        "values": "Morality (Social Norms)"
    },
    {
        "year": "2021",
        "author": "Nadeem",
        "link": "[[2021-Nadeem-StereoSet]]",
        "name": "StereoSet",
        "type": "Dataset",
        "items": "Large-scale",
        "usage": "Assessment",
        "values": "Bias (Stereotypes)"
    },
    {
        "year": "2021",
        "author": "Röttger",
        "link": "[[2021-Röttger-HateCheck]]",
        "name": "HateCheck",
        "type": "Benchmark",
        "items": "Functional tests",
        "usage": "Assessment",
        "values": "Safety (Hate Speech)"
    },
    {
        "year": "2021",
        "author": "Lourie",
        "link": "[[2021-Lourie-Scruples]]",
        "name": "Scruples",
        "type": "Dataset",
        "items": "32,000 anecdotes",
        "usage": "Assessment/Training",
        "values": "Ethics (Descriptive)"
    },
    {
        "year": "2021",
        "author": "Caselli",
        "link": "[[2021-Caselli-HateBERT]]",
        "name": "RAL-E / HateBERT",
        "type": "Dataset",
        "items": "Reddit comments",
        "usage": "Training",
        "values": "Safety (Abusive Language)"
    },
    {
        "year": "2020",
        "author": "Gehman",
        "link": "[[2020-Gehman-RealToxicityPrompts]]",
        "name": "RealToxicityPrompts",
        "type": "Dataset",
        "items": "100K prompts",
        "usage": "Assessment",
        "values": "Safety (Toxicity)"
    },
    {
        "year": "2020",
        "author": "Nangia",
        "link": "[[2020-Nangia-CrowS-Pairs]]",
        "name": "CrowS-Pairs",
        "type": "Dataset",
        "items": "Challenge dataset",
        "usage": "Assessment",
        "values": "Bias (Social)"
    },
    {
        "year": "2020",
        "author": "Sap",
        "link": "[[2020-Sap-Social Bias Frames]]",
        "name": "Social Bias Frames (SBIC)",
        "type": "Dataset",
        "items": "44k posts",
        "usage": "Assessment/Training",
        "values": "Bias (Power implications)"
    },
    {
        "year": "2020",
        "author": "Forbes",
        "link": "[[2020-Forbes-Social Chemistry 101]]",
        "name": "Social Chemistry 101",
        "type": "Dataset",
        "items": "292k rules",
        "usage": "Training/Assessment",
        "values": "Morality (Social Norms)"
    },
    {
        "year": "2020",
        "author": "Mathew",
        "link": "[[2020-Mathew-HateXplain]]",
        "name": "HateXplain",
        "type": "Dataset",
        "items": "Benchmark dataset",
        "usage": "Assessment (Explainability)",
        "values": "Safety (Hate Speech)"
    },
    {
        "year": "2020",
        "author": "Hoover",
        "link": "[[2020-Hoover-Moral Foundations Twitter Corpus]]",
        "name": "MFTC (Moral Foundations Twitter Corpus)",
        "type": "Dataset",
        "items": "35,108 tweets",
        "usage": "Assessment",
        "values": "Morality (MFT)"
    },
    {
        "year": "2019",
        "author": "De-Arteaga",
        "link": "[[2019-De-Arteaga-Bias in Bios]]",
        "name": "Bias in Bios",
        "type": "Dataset",
        "items": "Large-scale",
        "usage": "Assessment",
        "values": "Bias (Gender/Occupation)"
    },
    {
        "year": "2018",
        "author": "Dixon",
        "link": "[[2018-Dixon-Measuring and Mitigating Unintended Bias in Text]]",
        "name": "Unintended Bias in Text Classification",
        "type": "Dataset",
        "items": "Wikipedia Talk Labels",
        "usage": "Assessment",
        "values": "Bias (Identity Terms)"
    },
    {
        "year": "2018",
        "author": "Kiritchenko",
        "link": "[[2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred]]",
        "name": "EEC (Equity Evaluation Corpus)",
        "type": "Dataset",
        "items": "8,640 sentences",
        "usage": "Assessment",
        "values": "Bias (Gender/Race)"
    },
    {
        "year": "2018",
        "author": "Zhao",
        "link": "[[2018-Zhao-Gender Bias in Coreference Resolution]]",
        "name": "WinoBias (Zhao et al.)",
        "type": "Benchmark",
        "items": "3,160 sentences",
        "usage": "Assessment",
        "values": "Bias (Gender/Coreference)"
    }
]

def main():
    print(f"Writing {len(VERIFIED_DATA)} verified benchmarks to {OUTPUT_JSON}...")
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(VERIFIED_DATA, f, indent=2, ensure_ascii=False)
    print("Done.")

if __name__ == "__main__":
    main()
