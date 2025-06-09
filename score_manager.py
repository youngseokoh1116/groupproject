import json
import matplotlib.pyplot as plt

plt.rc("font", family="Malgun Gothic")

def save_result(username, score):
    data = {"user": username, "score": score}
    with open("quiz_results.json", "a", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
        f.write("\n")

def plot_scores():
    
    scores = []
    with open("quiz_results.json", "r", encoding="utf-8") as f:
        for i in f:
            try:
                entry = json.loads(i)
                scores.append(entry["score"])
            except:
                continue

    if not scores:
        return

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(range(1, len(scores)+1), scores, marker="o", linestyle="-", color="blue")
    ax.set_title("퀴즈 점수 추이")
    ax.set_xlabel("시도 횟수")
    ax.set_ylabel("점수")
    ax.grid(True)

    plt.tight_layout()
    plt.show()